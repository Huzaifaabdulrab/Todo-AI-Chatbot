# Quickstart Guide: Chatbot Task Creation Fix

## Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for backend)
- PostgreSQL database
- Google Gemini API key

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your configuration:
```env
DATABASE_URL=postgresql://username:password@localhost/dbname
JWT_SECRET=your-super-secret-jwt-secret
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-1.5-flash
```

5. Start the backend server:
```bash
python -m src.main
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env.local` file with your configuration:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
```

4. Start the frontend development server:
```bash
npm run dev
```

## Testing the Fix

1. Open your browser to `http://localhost:3000`
2. Sign in to your account
3. Navigate to the chatbot interface
4. Try creating a task via chat (e.g., "Create a task to buy groceries")
5. Verify that the task appears in the task list
6. Refresh the page and verify that the chat session persists
7. Test error handling by temporarily disabling the backend and observing error messages

## Common Issues and Fixes

### Issue: API calls returning 404 errors
**Solution**: Check that the frontend is calling the correct API endpoints and that the backend routes are properly registered.

### Issue: Tasks not saving to database
**Solution**: Verify that the MCP agent is properly calling the `add_task` tool and that the database transaction is being committed.

### Issue: Session not persisting
**Solution**: Check that the session ID is properly stored and retrieved in the frontend component and that the backend is maintaining conversation state.