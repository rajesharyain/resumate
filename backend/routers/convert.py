"""
Resume conversion router - AI-powered conversion to different standards
"""
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Literal
import os
import json
from openai import OpenAI
from prompts.resume_templates import get_prompt_template, RESUME_STANDARDS

router = APIRouter(prefix="/api", tags=["convert"])

# Initialize OpenAI client
openai_client = None


def get_openai_client():
    """Get or create OpenAI client"""
    global openai_client
    if openai_client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(
                status_code=500,
                detail="OPENAI_API_KEY not configured"
            )
        openai_client = OpenAI(api_key=api_key)
    return openai_client


class ConvertResumeRequest(BaseModel):
    resume_text: str = Field(..., description="The extracted resume text to convert")
    standard: Literal["us_ats", "europass", "indian_corporate", "uk_professional"] = Field(
        ..., description="Resume standard to convert to"
    )


def parse_json_response(response_text: str) -> dict:
    """
    Parse JSON from OpenAI response, handling markdown code blocks if present.
    """
    # Remove markdown code blocks if present
    text = response_text.strip()
    if text.startswith("```json"):
        text = text[7:]  # Remove ```json
    elif text.startswith("```"):
        text = text[3:]  # Remove ```
    
    if text.endswith("```"):
        text = text[:-3]  # Remove closing ```
    
    text = text.strip()
    
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to parse AI response as JSON: {str(e)}"
        )


@router.post("/convert-resume")
async def convert_resume(request: ConvertResumeRequest):
    """
    Convert parsed resume text into a structured resume based on selected standard.
    
    Supported standards:
    - us_ats: US ATS-friendly format
    - europass: European (EUROPASS) format
    - indian_corporate: Indian Corporate format
    - uk_professional: UK Professional format
    
    Returns structured JSON with personal_info, summary, experience, education, and skills.
    """
    try:
        # Validate input
        if not request.resume_text or not request.resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Resume text cannot be empty"
            )
        
        # Get prompt template for the selected standard
        try:
            prompt_template = get_prompt_template(request.standard)
        except ValueError as e:
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )
        
        # Format prompt with resume text
        prompt = prompt_template.format(resume_text=request.resume_text.strip())
        
        # Get OpenAI client
        client = get_openai_client()
        
        # Call OpenAI API
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Using cost-effective model
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert resume conversion assistant. Always return valid JSON only, no markdown, no explanations."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,  # Lower temperature for more consistent, structured output
                response_format={"type": "json_object"}  # Force JSON output
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"OpenAI API error: {str(e)}"
            )
        
        # Extract response content
        response_text = response.choices[0].message.content
        
        if not response_text:
            raise HTTPException(
                status_code=500,
                detail="Empty response from OpenAI"
            )
        
        # Parse JSON response
        try:
            structured_resume = parse_json_response(response_text)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to parse AI response: {str(e)}"
            )
        
        # Validate response structure
        required_fields = ["personal_info", "summary", "experience", "education", "skills"]
        for field in required_fields:
            if field not in structured_resume:
                raise HTTPException(
                    status_code=500,
                    detail=f"AI response missing required field: {field}"
                )
        
        return {
            "success": True,
            "standard": request.standard,
            "standard_name": RESUME_STANDARDS.get(request.standard, request.standard),
            "resume": structured_resume
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during resume conversion: {str(e)}"
        )


@router.get("/resume-standards")
async def get_resume_standards():
    """Get list of available resume standards"""
    return {
        "standards": [
            {
                "value": key,
                "name": value
            }
            for key, value in RESUME_STANDARDS.items()
        ]
    }

