from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.api.chat import router as chat_router, ChatRequest
from src.api.conversation import router as conversation_router
from src.api.tasks import router as tasks_router
from src.api.auth import router as auth_router
from src.api.dependencies import get_current_user
from src.models.user import User
from sqlmodel import Session
from src.core.database import get_session
from typing import Annotated

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(tasks_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(chat_router, prefix="/api/chat")    
app.include_router(conversation_router, prefix="/api/conversations")

# Include the simple routes for frontend compatibility
from src.api.simple_routes import router as simple_router
app.include_router(simple_router, prefix="/api", tags=["simple"])

@app.get("/")
def read_root():
    return {"Hello": "World"}