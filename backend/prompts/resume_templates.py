"""
Prompt templates for resume conversion to different standards
"""

RESUME_STANDARDS = {
    "us_ats": "US ATS",
    "europass": "European (EUROPASS)",
    "indian_corporate": "Indian Corporate",
    "uk_professional": "UK Professional"
}


def get_prompt_template(standard: str) -> str:
    """
    Get prompt template for the specified resume standard.
    
    Args:
        standard: One of 'us_ats', 'europass', 'indian_corporate', 'uk_professional'
    
    Returns:
        Prompt template string
    """
    templates = {
        "us_ats": _get_us_ats_prompt(),
        "europass": _get_europass_prompt(),
        "indian_corporate": _get_indian_corporate_prompt(),
        "uk_professional": _get_uk_professional_prompt()
    }
    
    if standard not in templates:
        raise ValueError(f"Unknown standard: {standard}")
    
    return templates[standard]


def _get_us_ats_prompt() -> str:
    """US ATS-friendly resume prompt"""
    return """You are an expert resume writer specializing in ATS (Applicant Tracking System) optimization.

Convert the following resume text into a structured, ATS-friendly format.

CRITICAL REQUIREMENTS:
- Use standard section headings: "Professional Summary", "Work Experience", "Education", "Skills"
- Use bullet points with quantified achievements (numbers, percentages, metrics)
- Use action verbs (Managed, Developed, Increased, Reduced, etc.)
- NO emojis, symbols, or special characters
- Professional, concise language
- Focus on achievements and impact, not just responsibilities
- Use reverse chronological order for experience
- Include relevant keywords naturally

OUTPUT FORMAT (valid JSON only):
{
  "personal_info": {
    "full_name": "string",
    "email": "string",
    "phone": "string",
    "location": "string",
    "linkedin": "string (optional)",
    "website": "string (optional)"
  },
  "summary": "string (2-3 sentences, ATS-optimized)",
  "experience": [
    {
      "title": "string",
      "company": "string",
      "location": "string",
      "start_date": "MM/YYYY",
      "end_date": "MM/YYYY or 'Present'",
      "achievements": ["string (quantified bullet points)"]
    }
  ],
  "education": [
    {
      "degree": "string",
      "institution": "string",
      "location": "string",
      "graduation_date": "YYYY",
      "gpa": "string (optional)",
      "honors": "string (optional)"
    }
  ],
  "skills": ["string (technical and soft skills)"]
}

Resume text to convert:
{resume_text}

Return ONLY valid JSON. No markdown, no explanations, no code blocks."""


def _get_europass_prompt() -> str:
    """EUROPASS format resume prompt"""
    return """You are an expert resume writer specializing in EUROPASS format resumes for European job markets.

Convert the following resume text into a structured EUROPASS-compatible format.

CRITICAL REQUIREMENTS:
- Follow EUROPASS structure and conventions
- Use clear, professional language suitable for European employers
- Include dates in DD/MM/YYYY or MM/YYYY format
- Quantify achievements with metrics
- NO emojis, symbols, or special characters
- Professional tone appropriate for European business culture
- Include language proficiency if mentioned
- Use reverse chronological order

OUTPUT FORMAT (valid JSON only):
{
  "personal_info": {
    "full_name": "string",
    "email": "string",
    "phone": "string",
    "address": "string",
    "nationality": "string (optional)",
    "date_of_birth": "DD/MM/YYYY (optional)",
    "linkedin": "string (optional)"
  },
  "summary": "string (professional summary, 2-3 sentences)",
  "experience": [
    {
      "title": "string",
      "company": "string",
      "location": "string (City, Country)",
      "start_date": "MM/YYYY",
      "end_date": "MM/YYYY or 'Present'",
      "description": "string (brief description)",
      "achievements": ["string (quantified bullet points)"]
    }
  ],
  "education": [
    {
      "degree": "string",
      "field_of_study": "string (optional)",
      "institution": "string",
      "location": "string (City, Country)",
      "graduation_date": "YYYY",
      "grade": "string (optional)"
    }
  ],
  "skills": [
    {
      "category": "string (e.g., 'Technical Skills', 'Languages')",
      "items": ["string"]
    }
  ]
}

Resume text to convert:
{resume_text}

Return ONLY valid JSON. No markdown, no explanations, no code blocks."""


def _get_indian_corporate_prompt() -> str:
    """Indian Corporate format resume prompt"""
    return """You are an expert resume writer specializing in Indian corporate resume formats.

Convert the following resume text into a structured format suitable for Indian corporate job applications.

CRITICAL REQUIREMENTS:
- Follow Indian corporate resume conventions
- Include relevant details like current CTC, expected CTC if mentioned (optional)
- Use professional Indian business English
- Quantify achievements with numbers and percentages
- NO emojis, symbols, or special characters
- Professional, formal tone
- Include notice period if mentioned (optional)
- Use DD/MM/YYYY date format
- Highlight technical skills prominently

OUTPUT FORMAT (valid JSON only):
{
  "personal_info": {
    "full_name": "string",
    "email": "string",
    "phone": "string",
    "location": "string (City, State)",
    "linkedin": "string (optional)",
    "current_ctc": "string (optional)",
    "expected_ctc": "string (optional)",
    "notice_period": "string (optional)"
  },
  "summary": "string (professional summary, 2-3 sentences)",
  "experience": [
    {
      "title": "string",
      "company": "string",
      "location": "string",
      "start_date": "MM/YYYY",
      "end_date": "MM/YYYY or 'Present'",
      "achievements": ["string (quantified bullet points with metrics)"]
    }
  ],
  "education": [
    {
      "degree": "string",
      "institution": "string",
      "location": "string",
      "graduation_date": "YYYY",
      "percentage": "string (optional)",
      "university": "string (optional)"
    }
  ],
  "skills": {
    "technical": ["string"],
    "soft_skills": ["string (optional)"]
  }
}

Resume text to convert:
{resume_text}

Return ONLY valid JSON. No markdown, no explanations, no code blocks."""


def _get_uk_professional_prompt() -> str:
    """UK Professional format resume prompt"""
    return """You are an expert resume writer specializing in UK professional CV formats.

Convert the following resume text into a structured format suitable for UK professional job applications.

CRITICAL REQUIREMENTS:
- Follow UK CV conventions and professional standards
- Use British English spelling and terminology
- Include dates in DD/MM/YYYY or MM/YYYY format
- Quantify achievements with metrics and percentages
- NO emojis, symbols, or special characters
- Professional, polished tone
- Use reverse chronological order
- Include professional qualifications if mentioned
- Focus on achievements and impact

OUTPUT FORMAT (valid JSON only):
{
  "personal_info": {
    "full_name": "string",
    "email": "string",
    "phone": "string",
    "address": "string (optional)",
    "location": "string (City, UK)",
    "linkedin": "string (optional)",
    "professional_qualifications": "string (optional)"
  },
  "summary": "string (professional profile, 2-3 sentences)",
  "experience": [
    {
      "title": "string",
      "company": "string",
      "location": "string",
      "start_date": "MM/YYYY",
      "end_date": "MM/YYYY or 'Present'",
      "achievements": ["string (quantified bullet points with impact)"]
    }
  ],
  "education": [
    {
      "degree": "string",
      "institution": "string",
      "location": "string",
      "graduation_date": "YYYY",
      "grade": "string (e.g., 'First Class Honours', '2:1', optional)",
      "qualifications": "string (optional)"
    }
  ],
  "skills": ["string (technical and professional skills)"]
}

Resume text to convert:
{resume_text}

Return ONLY valid JSON. No markdown, no explanations, no code blocks."""

