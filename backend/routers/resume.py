"""
Resume parsing router
"""
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import pdfplumber
import docx
from io import BytesIO
from typing import Optional

router = APIRouter(prefix="/api", tags=["resume"])

# Maximum file size: 2MB
MAX_FILE_SIZE = 2 * 1024 * 1024


def parse_pdf(file_content: bytes) -> str:
    """Extract text from PDF file"""
    try:
        with pdfplumber.open(BytesIO(file_content)) as pdf:
            text_parts = []
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
            return "\n\n".join(text_parts)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to parse PDF: {str(e)}"
        )


def parse_docx(file_content: bytes) -> str:
    """Extract text from DOCX file"""
    try:
        doc = docx.Document(BytesIO(file_content))
        paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
        return "\n".join(paragraphs)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to parse DOCX: {str(e)}"
        )


@router.post("/parse-resume")
async def parse_resume(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None)
):
    """
    Parse resume from uploaded file or text input.
    
    Supports:
    - PDF files (.pdf)
    - DOCX files (.docx)
    - Plain text input
    
    Returns extracted text.
    """
    try:
        # Validate input: either file or text must be provided
        if not file and not text:
            raise HTTPException(
                status_code=400,
                detail="Either a file or text input must be provided"
            )
        
        # Handle text input
        if text:
            if len(text.strip()) == 0:
                raise HTTPException(
                    status_code=400,
                    detail="Text input cannot be empty"
                )
            return {
                "success": True,
                "text": text.strip(),
                "source": "text_input",
                "file_name": None,
                "file_type": None
            }
        
        # Handle file upload
        if file:
            # Validate file size
            file_content = await file.read()
            file_size = len(file_content)
            
            if file_size > MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=400,
                    detail=f"File size ({file_size / 1024 / 1024:.2f}MB) exceeds maximum allowed size (2MB)"
                )
            
            if file_size == 0:
                raise HTTPException(
                    status_code=400,
                    detail="Uploaded file is empty"
                )
            
            # Validate file type
            file_extension = file.filename.split('.')[-1].lower() if file.filename else ""
            content_type = file.content_type or ""
            
            extracted_text = None
            
            # Parse based on file type
            if file_extension == "pdf" or "pdf" in content_type:
                extracted_text = parse_pdf(file_content)
            elif file_extension in ["docx", "doc"] or "wordprocessingml" in content_type or "msword" in content_type:
                if file_extension == "doc":
                    raise HTTPException(
                        status_code=400,
                        detail="DOC format is not supported. Please convert to DOCX or PDF."
                    )
                extracted_text = parse_docx(file_content)
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Unsupported file type. Supported formats: PDF, DOCX"
                )
            
            if not extracted_text or not extracted_text.strip():
                raise HTTPException(
                    status_code=400,
                    detail="No text could be extracted from the file. The file may be empty or corrupted."
                )
            
            return {
                "success": True,
                "text": extracted_text.strip(),
                "source": "file_upload",
                "file_name": file.filename,
                "file_type": file_extension,
                "file_size": file_size
            }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while parsing the resume: {str(e)}"
        )

