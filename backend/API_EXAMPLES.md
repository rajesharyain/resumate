# Resume Parsing API Examples

## Endpoint: `POST /api/parse-resume`

Parse a resume from an uploaded file (PDF, DOCX) or text input.

### Request Formats

#### 1. File Upload (PDF)

```bash
curl -X POST http://localhost:8000/api/parse-resume \
  -F "file=@resume.pdf"
```

**Form Data:**
- `file`: PDF or DOCX file (max 2MB)

#### 2. File Upload (DOCX)

```bash
curl -X POST http://localhost:8000/api/parse-resume \
  -F "file=@resume.docx"
```

#### 3. Text Input

```bash
curl -X POST http://localhost:8000/api/parse-resume \
  -F "text=John Doe\nSoftware Engineer\n5 years of experience..."
```

**Form Data:**
- `text`: Plain text resume content

### Success Response

**Status Code:** `200 OK`

**Response Body (File Upload):**
```json
{
  "success": true,
  "text": "John Doe\nSoftware Engineer\n...",
  "source": "file_upload",
  "file_name": "resume.pdf",
  "file_type": "pdf",
  "file_size": 145678
}
```

**Response Body (Text Input):**
```json
{
  "success": true,
  "text": "John Doe\nSoftware Engineer\n...",
  "source": "text_input",
  "file_name": null,
  "file_type": null
}
```

### Error Responses

#### 1. File Too Large

**Status Code:** `400 Bad Request`

```json
{
  "detail": "File size (2.5MB) exceeds maximum allowed size (2MB)"
}
```

#### 2. Unsupported File Type

**Status Code:** `400 Bad Request`

```json
{
  "detail": "Unsupported file type. Supported formats: PDF, DOCX"
}
```

#### 3. Empty Input

**Status Code:** `400 Bad Request`

```json
{
  "detail": "Either a file or text input must be provided"
}
```

#### 4. Parsing Error

**Status Code:** `400 Bad Request`

```json
{
  "detail": "Failed to parse PDF: [error message]"
}
```

#### 5. No Text Extracted

**Status Code:** `400 Bad Request`

```json
{
  "detail": "No text could be extracted from the file. The file may be empty or corrupted."
}
```

### JavaScript/TypeScript Example

```typescript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

const response = await fetch('http://localhost:8000/api/parse-resume', {
  method: 'POST',
  body: formData,
});

const result = await response.json();
console.log(result.text); // Extracted text
```

### Python Example

```python
import requests

# File upload
with open('resume.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post(
        'http://localhost:8000/api/parse-resume',
        files=files
    )
    result = response.json()
    print(result['text'])

# Text input
data = {'text': 'John Doe\nSoftware Engineer...'}
response = requests.post(
    'http://localhost:8000/api/parse-resume',
    data=data
)
result = response.json()
print(result['text'])
```

