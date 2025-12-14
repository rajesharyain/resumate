# Resume Download Feature

## Overview
Implemented resume download functionality allowing users to export their resumes as PDF or DOCX files with proper formatting preserved.

## Backend Implementation

### Endpoints

#### `POST /api/download/pdf`
Generates and downloads resume as PDF file.

**Request:**
```json
{
  "resume": {
    "personal_info": { ... },
    "summary": "...",
    "experience": [ ... ],
    "education": [ ... ],
    "skills": [ ... ]
  },
  "standard": "us_ats"
}
```

**Response:**
- Content-Type: `application/pdf`
- File download with appropriate filename

#### `POST /api/download/docx`
Generates and downloads resume as DOCX file.

**Request:** Same as PDF endpoint

**Response:**
- Content-Type: `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- File download with appropriate filename

### PDF Generation

- **Library:** WeasyPrint (HTML to PDF)
- **Method:** HTML generation → PDF conversion
- **Features:**
  - Preserves formatting
  - Print-friendly styling
  - Standard-specific templates
  - Professional layout

### DOCX Generation

- **Library:** python-docx
- **Method:** Programmatic document creation
- **Features:**
  - Maintains section order
  - Professional formatting
  - Bullet points for achievements
  - Clean structure

### HTML Templates

Each standard has its own HTML template:
- **US ATS:** Clean, ATS-friendly format
- **EUROPASS:** Blue accents, European style
- **Indian Corporate:** Indigo accents, CTC fields
- **UK Professional:** Slate/gray, UK CV format

### Files Created

- `backend/routers/download.py` - Download endpoints and generation logic
- `backend/requirements.txt` - Updated with weasyprint and jinja2

## Frontend Implementation

### Download Buttons

- **Location:** Preview card header (both desktop and mobile)
- **Buttons:**
  - PDF download button
  - DOCX download button
- **States:**
  - Normal: Shows file icon and format name
  - Loading: Shows spinner and "Generating..." text
  - Disabled: When other download is in progress

### Download Flow

1. User clicks download button (PDF or DOCX)
2. Button shows loading state
3. API call to backend endpoint
4. File blob received
5. Browser downloads file automatically
6. Button returns to normal state

### Error Handling

- **Validation:** Checks if name is entered before download
- **Error Display:** Shows error message in preview card
- **User Feedback:** Clear error messages
- **Graceful Degradation:** Buttons disabled during download

### Mobile Support

- Download buttons visible on mobile preview
- Responsive button sizing
- Touch-friendly interface

### Files Modified

- `frontend/app/editor/page.tsx` - Added download buttons and handlers
- `frontend/lib/api.ts` - Added download API functions

## Usage

1. **Edit Resume:**
   - Fill in resume information in editor
   - Ensure name is entered (required for filename)

2. **Download:**
   - Click "PDF" button to download as PDF
   - Click "DOCX" button to download as DOCX
   - Wait for file generation
   - File downloads automatically

## File Naming

Files are named: `resume_{standard}_{name}.{ext}`

Example:
- `resume_us_ats_John_Doe.pdf`
- `resume_europass_Jane_Smith.docx`

## Error Handling

### Backend Errors
- Missing resume data → 400 Bad Request
- PDF generation failure → 500 with error message
- DOCX generation failure → 500 with error message

### Frontend Errors
- Missing name → Validation message
- Network errors → Error display
- API errors → User-friendly error message

## Dependencies

### Backend
- `weasyprint==62.3` - HTML to PDF conversion
- `jinja2==3.1.4` - Template engine (for future use)
- `python-docx==1.1.2` - DOCX generation (already installed)

## Technical Details

### PDF Generation
- HTML → WeasyPrint → PDF bytes
- Preserves CSS styling
- Print-optimized layout
- Standard-specific colors and formatting

### DOCX Generation
- python-docx Document object
- Structured sections
- Bullet points for achievements
- Professional formatting

### Security
- HTML escaping applied to user input
- XSS prevention
- Safe file naming

## Testing

To test downloads:

1. Start backend server
2. Navigate to `/editor`
3. Fill in resume information
4. Click download buttons
5. Verify files download correctly
6. Open files and verify formatting

## Next Steps

Potential enhancements:
- Download progress indicator
- Batch download (both formats)
- Custom filename option
- Preview before download
- Print stylesheet optimization
- Additional export formats (TXT, JSON)

