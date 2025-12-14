# Resumate Backend

FastAPI backend for the Resumate AI-Powered Resume Converter.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file from `env.example`:
```bash
cp env.example .env
# Edit .env and add your OPENAI_API_KEY
```

4. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

## Docker

Build the image:
```bash
docker build -t resumate-backend .
```

Run the container:
```bash
docker run -p 8000:8000 --env-file .env resumate-backend
```

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `API_HOST`: Host to bind to (default: 0.0.0.0)
- `API_PORT`: Port to bind to (default: 8000)

