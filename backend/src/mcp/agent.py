"""
AI Agent for Google Gemini - Todo Assistant
"""
import json
from typing import List, Dict, Any
from uuid import UUID
from sqlmodel import Session

import google.generativeai as genai
from google.generativeai.types import Tool, FunctionDeclaration

from core.config import settings
from mcp.tools import add_task, list_tasks, complete_task, update_task, delete_task

class ChatAgent:
    def __init__(self, session: Session, user_id: UUID):
        self.session = session
        self.user_id = user_id
        
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name=settings.GEMINI_MODEL or "gemini-1.5-flash",
            tools=self._define_tools(),
            system_instruction=self._get_system_prompt(),
            generation_config={"temperature": 0.7}
        )

    def _get_system_prompt(self) -> str:
        return """You are a helpful Todo Assistant.
You manage user's tasks using the provided tools.
Be friendly, clear and always confirm actions.
If something goes wrong with a tool, explain it nicely to the user."""

    def _define_tools(self) -> list[Tool]:
        return [Tool(function_declarations=[
            FunctionDeclaration(
                name="add_task",
                description="Add a new task with title and optional description.",
                parameters={
                    "type": "OBJECT",
                    "properties": {
                        "title": {"type": "STRING", "description": "Task title"},
                        "description": {"type": "STRING", "description": "Optional task details"}
                    },
                    "required": ["title"]
                }
            ),
            FunctionDeclaration(
                name="list_tasks",
                description="List all tasks. Optional: filter by completed status.",
                parameters={
                    "type": "OBJECT",
                    "properties": {
                        "completed": {"type": "BOOLEAN", "description": "true = completed, false = pending"}
                    }
                }
            ),
            FunctionDeclaration(
                name="complete_task",
                description="Mark a task as completed by title or ID.",
                parameters={
                    "type": "OBJECT",
                    "properties": {
                        "task_identifier": {"type": "STRING", "description": "Task title (partial match) or exact ID"}
                    },
                    "required": ["task_identifier"]
                }
            ),
            FunctionDeclaration(
                name="update_task",
                description="Update task title or description.",
                parameters={
                    "type": "OBJECT",
                    "properties": {
                        "task_identifier": {"type": "STRING", "description": "Task title or ID"},
                        "title": {"type": "STRING", "description": "New title (optional)"},
                        "description": {"type": "STRING", "description": "New description (optional)"}
                    },
                    "required": ["task_identifier"]
                }
            ),
            FunctionDeclaration(
                name="delete_task",
                description="Delete a task permanently.",
                parameters={
                    "type": "OBJECT",
                    "properties": {
                        "task_identifier": {"type": "STRING", "description": "Task title (partial match) or exact ID"}
                    },
                    "required": ["task_identifier"]
                }
            )
        ])]

    def process_message(self, history: List[Dict[str, str]]) -> str:
        chat = self.model.start_chat(history=[
            {"role": "user" if msg["role"] in ("user", "human") else "model", "parts": [msg["content"]]}
            for msg in history[:-1]  # last message separately
        ])

        # Send the latest user message
        response = chat.send_message(history[-1]["content"])

        # Handle function calling
        while response.candidates[0].content.parts and response.candidates[0].content.parts[0].function_call:
            fc = response.candidates[0].content.parts[0].function_call
            func_name = fc.name
            args = dict(fc.args) if fc.args else {}

            tool_result = {"success": False, "message": "Unknown tool"}

            try:
                if func_name == "add_task":
                    tool_result = add_task(self.session, self.user_id, **args)
                elif func_name == "list_tasks":
                    tool_result = list_tasks(self.session, self.user_id, **args)
                elif func_name == "complete_task":
                    tool_result = complete_task(self.session, self.user_id, **args)
                elif func_name == "update_task":
                    tool_result = update_task(self.session, self.user_id, **args)
                elif func_name == "delete_task":
                    tool_result = delete_task(self.session, self.user_id, **args)
            except Exception as e:
                tool_result = {"success": False, "message": str(e)}

            # Send back the function response
            response = chat.send_message(
                genai.protos.Part(
                    function_response=genai.protos.FunctionResponse(
                        name=func_name,
                        response={"result": tool_result}
                    )
                )
            )

        return response.text