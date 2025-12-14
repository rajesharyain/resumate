"""
FastAPI backend for Resumate - AI-Powered Resume Converter
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
from routers import resume, convert

# Load environment variables
load_dotenv()

# CORS origins - update for production
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown events"""
    # Startup
    print("🚀 Resumate Backend starting up...")
    yield
    # Shutdown
    print("👋 Resumate Backend shutting down...")


app = FastAPI(
    title="Resumate API",
    description="AI-Powered Resume Converter API",
    version="1.0.0",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(resume.router)
app.include_router(convert.router)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "resumate-api",
        "version": "1.0.0",
    }


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Resumate API",
        "docs": "/docs",
        "health": "/health",
    }

