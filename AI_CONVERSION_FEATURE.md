# AI-Powered Resume Conversion Feature

## Overview
Implemented AI-powered resume conversion that transforms parsed resume text into structured resumes based on different global standards using OpenAI's Chat Completion API.

## Backend Implementation

### Endpoint: `POST /api/convert-resume`

**Request Body:**
```json
{
  "resume_text": "Extracted resume text...",
  "standard": "us_ats" | "europass" | "indian_corporate" | "uk_professional"
}
```

**Response:**
```json
{
  "success": true,
  "standard": "us_ats",
  "standard_name": "US ATS",
  "resume": {
    "personal_info": { ... },
    "summary": "...",
    "experience": [ ... ],
    "education": [ ... ],
    "skills": [ ... ]
  }
}
```

### Prompt Templates

Located in `backend/prompts/resume_templates.py`:

1. **US ATS** (`us_ats`)
   - ATS-optimized format
   - Standard section headings
   - Quantified achievements
   - Action verbs
   - Keywords naturally integrated

2. **EUROPASS** (`europass`)
   - European format conventions
   - DD/MM/YYYY date format
   - Language proficiency support
   - European business culture tone

3. **Indian Corporate** (`indian_corporate`)
   - Indian corporate conventions
   - CTC fields (optional)
   - Notice period (optional)
   - Technical skills emphasis
   - DD/MM/YYYY date format

4. **UK Professional** (`uk_professional`)
   - UK CV conventions
   - British English
   - Professional qualifications
   - DD/MM/YYYY date format

### AI Rules Enforced

- ✅ ATS-friendly formatting
- ✅ No emojis or special characters
- ✅ Professional tone
- ✅ Quantified bullet points (numbers, percentages, metrics)
- ✅ Action verbs
- ✅ Structured JSON output

### Files Created

- `backend/routers/convert.py` - Conversion endpoint
- `backend/prompts/resume_templates.py` - Prompt templates
- `backend/prompts/__init__.py` - Prompts package

## Frontend Implementation

### Features

1. **Resume Standard Dropdown**
   - Select from 4 standards
   - Loads dynamically from API
   - Disabled during conversion

2. **Conversion Button**
   - Converts extracted text to selected standard
   - Shows loading state
   - Error handling

3. **Structured Display**
   - Personal Information section
   - Professional Summary
   - Experience with achievements
   - Education details
   - Skills (supports both array and categorized formats)
   - Raw JSON view (collapsible)

4. **Copy Functionality**
   - Copy structured JSON to clipboard
   - Visual feedback

### Files Modified

- `frontend/app/parse/page.tsx` - Added conversion UI
- `frontend/lib/api.ts` - Added conversion API functions
- `frontend/components/ui/select.tsx` - Select component

## Usage Flow

1. **Parse Resume**
   - Upload file or paste text
   - Click "Parse Resume"
   - View extracted text

2. **Select Standard**
   - Choose from dropdown (US ATS, EUROPASS, Indian Corporate, UK Professional)

3. **Convert**
   - Click "Convert to [Standard]"
   - Wait for AI processing
   - View structured resume

4. **View Results**
   - Structured sections displayed
   - Copy JSON if needed
   - Expand raw JSON view

## API Examples

### Convert Resume

```bash
curl -X POST http://localhost:8000/api/convert-resume \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "John Doe\nSoftware Engineer...",
    "standard": "us_ats"
  }'
```

### Get Available Standards

```bash
curl http://localhost:8000/api/resume-standards
```

## Response Structure

All standards return JSON with this structure:

```json
{
  "personal_info": {
    "full_name": "string",
    "email": "string",
    "phone": "string",
    "location": "string",
    ...
  },
  "summary": "string",
  "experience": [
    {
      "title": "string",
      "company": "string",
      "location": "string",
      "start_date": "string",
      "end_date": "string",
      "achievements": ["string"]
    }
  ],
  "education": [
    {
      "degree": "string",
      "institution": "string",
      "location": "string",
      "graduation_date": "string",
      ...
    }
  ],
  "skills": ["string"] | [{ "category": "string", "items": ["string"] }]
}
```

## Error Handling

- Missing OpenAI API key
- Invalid resume text
- Invalid standard selection
- OpenAI API errors
- JSON parsing errors
- Missing required fields in response

## Environment Variables

Required in `backend/.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Model Configuration

- **Model:** `gpt-4o-mini` (cost-effective)
- **Temperature:** 0.3 (consistent, structured output)
- **Response Format:** JSON object (when supported)

## Testing

To test the conversion:

1. Start backend with OpenAI API key configured
2. Parse a resume (upload or paste text)
3. Select a standard
4. Click "Convert"
5. Verify structured output

## Next Steps

- Add export to PDF/DOCX
- Add resume templates/previews
- Add validation for structured data
- Add ability to edit converted resume
- Add multiple standard comparison view

