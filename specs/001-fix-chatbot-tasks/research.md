# Research: Fix Chatbot Task Creation Issues

## Identified Issues

### 1. Frontend Issues
- **Chat API Endpoint Mismatch**: The frontend chat API service is calling `/api/chat` but the backend expects `/chat` (relative to the API base URL)
- **Session Handling**: The ChatWindow component has inconsistent session handling between initialization and message sending
- **Error Handling**: The frontend doesn't properly handle API errors (404/500) from the chat endpoint

### 2. Backend Issues
- **Gemini API Key**: Need to verify if the GEMINI_API_KEY is properly configured in the environment
- **MCP Agent Configuration**: The agent needs to properly handle function calling and response chaining
- **Session Management**: Conversation persistence and retrieval may have issues

### 3. Task Creation Flow Issues
- **Tool Integration**: The `add_task` tool in the MCP agent should properly create tasks via the TasksService
- **Database Transactions**: Need to ensure proper database transactions when creating tasks via chat
- **User Context**: Ensuring the correct user context is maintained throughout the chat session

## Root Cause Analysis

### Issue 1: Chat API Endpoint Mismatch
**Location**: `frontend/src/services/chatApi.js`
**Problem**: The `processMessage` function calls `'api/chat'` instead of `/api/chat`
**Impact**: API calls fail with 404 errors

### Issue 2: Task Creation Not Persisting
**Location**: `backend/src/mcp/tool.py`
**Problem**: The `add_task` function should properly call the TasksService to create tasks
**Impact**: Tasks created via chat are not saved to the database

### Issue 3: Session Management
**Location**: `frontend/src/components/ChatInterface/ChatWindow.jsx`
**Problem**: Inconsistent session ID handling between initialization and message sending
**Impact**: Sessions are not properly maintained across page refreshes

## Solutions

### Solution 1: Fix Frontend API Endpoint
**File**: `frontend/src/services/chatApi.js`
**Change**: Update the endpoint from `'api/chat'` to `/api/chat` in the processMessage function

### Solution 2: Improve Error Handling
**Files**: 
- `frontend/src/services/chatApi.js`
- `frontend/src/components/ChatInterface/ChatWindow.jsx`

**Changes**:
- Add proper error handling for 404 and 500 responses
- Display user-friendly error messages

### Solution 3: Verify MCP Agent Configuration
**File**: `backend/src/mcp/agent.py`
**Change**: Ensure the agent properly handles function calling and response chaining

### Solution 4: Enhance Session Management
**File**: `frontend/src/components/ChatInterface/ChatWindow.jsx`
**Change**: Implement consistent session ID handling and persistence

## Verification Steps

1. **Test Chat-Based Task Creation**: Verify that tasks created via chat appear in the task list
2. **Test Session Persistence**: Verify that chat sessions persist across page refreshes
3. **Test Error Handling**: Verify that API errors are properly handled and displayed
4. **Compare Functionality**: Ensure chat-based and form-based task creation work identically