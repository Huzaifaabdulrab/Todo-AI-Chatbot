"""
Simple API routes for frontend compatibility.
This module provides endpoints that match what the frontend expects.
"""
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import Annotated

from src.api.dependencies import get_current_user
from src.models.user import User
from src.core.database import get_session
from src.api.chat import ChatRequest

router = APIRouter()

@router.post("/chat")
async def simple_chat(
    request: ChatRequest,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)]
):
    """Simple endpoint to handle chat messages for frontend compatibility."""
    from src.api.chat import chat as chat_endpoint
    return await chat_endpoint(request, current_user, session)

@router.get("/chat/sessions")
async def get_chat_sessions_compat(
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)]
):
    from src.api.conversation import list_user_conversations
    return await list_user_conversations(current_user, session)