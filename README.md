# Resumate - AI-Powered Resume Converter

A production-ready MVP for converting resumes using AI.

## Project Structure

```
resumate/
├── frontend/          # Next.js 14 (App Router) + TypeScript + Tailwind
├── backend/           # FastAPI (Python) + Async endpoints
├── .gitignore
└── README.md
```

## Tech Stack

### Frontend
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui

### Backend
- FastAPI (Python)
- Async endpoints
- OpenAI API integration

## Getting Started

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:3000`

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on `http://localhost:8000`

### Environment Variables

Create `.env.local` in `frontend/` and `.env` in `backend/` with:

**Frontend (.env.local):**
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

**Backend (.env):**
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Deployment

### Frontend (Vercel)
The frontend is configured for Vercel deployment. Push to your repository and connect to Vercel.

### Backend (Docker)
```bash
cd backend
docker build -t resumate-backend .
docker run -p 8000:8000 --env-file .env resumate-backend
```

## Development

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

## Testing

### Running Cypress Tests

Make sure both frontend and backend servers are running before running tests:

1. **Start the servers:**
   ```bash
   # Terminal 1 - Frontend
   cd frontend
   npm run dev

   # Terminal 2 - Backend
   cd backend
   uvicorn main:app --reload
   ```

2. **Run Cypress tests:**
   ```bash
   cd frontend
   
   # Open Cypress Test Runner (interactive)
   npm run cypress:open
   
   # Run tests headlessly
   npm run cypress:run
   
   # Or use the test script
   npm run test:e2e
   ```

### Test Coverage

The Cypress test suite includes:

- **Frontend Tests** (`frontend.cy.ts`): UI rendering, responsive design, accessibility
- **Backend API Tests** (`backend-api.cy.ts`): Health check, API endpoints, CORS configuration
- **Integration Tests** (`integration.cy.ts`): Frontend-backend communication
- **Smoke Tests** (`smoke.cy.ts`): Basic functionality verification

All tests verify:
- ✅ Frontend loads correctly
- ✅ Backend API responds
- ✅ Health check endpoint works
- ✅ CORS is configured properly
- ✅ Mobile responsiveness
- ✅ No console errors


