# Resumate - AI-Powered Resume Converter

A production-ready MVP for converting resumes using AI. Upload or paste your resume, and convert it to different global standards (US ATS, EUROPASS, Indian Corporate, UK Professional) with AI-powered formatting.

## 🚀 Quick Start

### One-Command Setup

```bash
# Install all dependencies
npm run setup

# Copy environment files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local

# Edit backend/.env and add your OPENAI_API_KEY
# Edit frontend/.env.local if needed (defaults work for local dev)

# Start both frontend and backend
npm run dev
```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📁 Project Structure

```
resumate/
├── frontend/          # Next.js 14 (App Router) + TypeScript + Tailwind
│   ├── app/          # Next.js app router pages
│   ├── components/   # React components
│   ├── lib/          # Utilities and API client
│   └── cypress/      # E2E tests
├── backend/          # FastAPI (Python) + Async endpoints
│   ├── routers/      # API route handlers
│   ├── prompts/      # AI prompt templates
│   ├── middleware/   # Rate limiting and middleware
│   └── tests/        # Backend tests
├── Dockerfile        # Backend Docker configuration
├── docker-compose.yml # Docker Compose for local deployment
└── package.json      # Root-level scripts
```

## 🛠 Tech Stack

### Frontend
- **Next.js 14** (App Router)
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **shadcn/ui** for UI components
- **Cypress** for E2E testing

### Backend
- **FastAPI** (Python) with async endpoints
- **OpenAI API** for AI-powered conversion
- **WeasyPrint** for PDF generation
- **python-docx** for DOCX generation
- **slowapi** for rate limiting
- **Pydantic** for data validation

## ⚙️ Environment Variables

### Backend (.env)

Copy `backend/.env.example` to `backend/.env` and configure:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional (defaults shown)
PORT=8000
HOST=0.0.0.0
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001
ENVIRONMENT=development
```

### Frontend (.env.local)

Copy `frontend/.env.example` to `frontend/.env.local` and configure:

```env
# Optional (defaults shown)
NEXT_PUBLIC_API_URL=http://localhost:8000
NODE_ENV=development
```

## 🎯 Features

- ✅ **Resume Parsing**: Upload PDF/DOCX or paste text
- ✅ **AI Conversion**: Convert to 4 global standards
- ✅ **Resume Editor**: Live preview with real-time updates
- ✅ **Download**: Export as PDF or DOCX
- ✅ **Rate Limiting**: API protection against abuse
- ✅ **Error Handling**: Graceful error handling throughout
- ✅ **Mobile Responsive**: Works on all devices
- ✅ **Production Ready**: Docker, deployment configs, tests

## 📦 Installation

### Manual Setup

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
uvicorn main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
# Edit .env.local if needed
npm run dev
```

### Using Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build backend only
docker build -t resumate-backend .
docker run -p 8000:8000 --env-file backend/.env resumate-backend
```

## 🚢 Deployment

### Frontend (Vercel)

1. Push code to GitHub
2. Connect repository to Vercel
3. Configure environment variables in Vercel dashboard
4. Deploy

The `vercel.json` file is already configured.

### Backend (Docker)

1. Build the Docker image:
   ```bash
   docker build -t resumate-backend .
   ```

2. Run the container:
   ```bash
   docker run -d \
     -p 8000:8000 \
     --env-file .env \
     --name resumate-backend \
     resumate-backend
   ```

3. Or use Docker Compose:
   ```bash
   docker-compose up -d
   ```

### Backend (Cloud Platforms)

The backend can be deployed to:
- **Railway**: Connect GitHub repo, set environment variables
- **Render**: Connect GitHub repo, set environment variables
- **AWS ECS/Fargate**: Use Docker image
- **Google Cloud Run**: Use Docker image
- **Azure Container Instances**: Use Docker image

## 🧪 Testing

### Frontend (Cypress)

```bash
cd frontend

# Interactive mode
npm run cypress:open

# Headless mode
npm run cypress:run
```

### Backend (Pytest)

```bash
cd backend
pytest
```

## 🔒 Rate Limiting

The API implements rate limiting to prevent abuse:

- **Convert Resume**: 10 requests/hour per IP
- **Download**: 20 requests/hour per IP
- **Parse Resume**: 50 requests/hour per IP
- **Default**: 100 requests/hour per IP

Rate limit errors return HTTP 429 with a clear message.

## 🐛 Error Handling

The application handles errors gracefully:

- **OpenAI API Errors**: Specific error messages for rate limits, timeouts, quota issues
- **Validation Errors**: Clear messages for invalid input
- **Network Errors**: User-friendly error messages
- **File Errors**: Size and type validation

## 📚 API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎨 UI Features

- **Skeleton Loaders**: Smooth loading states
- **Responsive Design**: Works on mobile, tablet, and desktop
- **Real-time Preview**: Live updates as you edit
- **Error States**: Clear error messages
- **Loading States**: Visual feedback during operations

## 📝 Scripts

### Root Level

- `npm run dev` - Start both frontend and backend
- `npm run setup` - Install all dependencies
- `npm run build` - Build frontend for production
- `npm start` - Start in production mode

### Frontend

- `npm run dev` - Development server
- `npm run build` - Production build
- `npm start` - Production server
- `npm run cypress:open` - Open Cypress
- `npm run cypress:run` - Run Cypress tests

### Backend

- `uvicorn main:app --reload` - Development server
- `uvicorn main:app` - Production server
- `pytest` - Run tests

## 🔧 Development

### Code Quality

- TypeScript for type safety
- Pydantic for data validation
- ESLint for code linting
- Clean code comments
- No unused dependencies

### Project Standards

- Consistent code formatting
- Clear error messages
- Comprehensive error handling
- Production-ready configuration
- Security best practices

## 📄 License

MIT

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📞 Support

For issues and questions, please open an issue on GitHub.

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


