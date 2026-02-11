# Data Model: Fix Chatbot Task Creation Issues

## Entities

### Task
- **Purpose**: Represents a user's task with properties like title, description, status, creation timestamp, and user association
- **Fields**:
  - id: UUID (primary key, auto-generated)
  - user_id: UUID (foreign key to User, indexed)
  - title: string (max 200 chars, required)
  - description: string (max 2000 chars, optional)
  - is_completed: boolean (default: false)
  - created_at: datetime (auto-generated)
  - updated_at: datetime (auto-generated)
- **Relationships**: Many tasks belong to one user (owner)

### ChatSession (Conversation)
- **Purpose**: Represents an active chat session with properties like session ID, user association, and message history
- **Fields**:
  - id: UUID (primary key, auto-generated)
  - user_id: UUID (foreign key to User, indexed)
  - title: string (max 100 chars, optional, auto-generated from first message)
  - created_at: datetime (auto-generated)
  - updated_at: datetime (auto-generated)
- **Relationships**: One conversation has many messages, belongs to one user (owner)

### Message
- **Purpose**: Represents a single message in a chat conversation
- **Fields**:
  - id: UUID (primary key, auto-generated)
  - conversation_id: UUID (foreign key to Conversation, indexed)
  - role: string (user or assistant, max 20 chars)
  - content: string (max 10000 chars)
  - created_at: datetime (auto-generated)
- **Relationships**: Many messages belong to one conversation

### APIResponse
- **Purpose**: Represents the response from API calls with properties like status code, message, and data payload
- **Structure**:
  - message: Message object
  - conversation_id: string
- **Used in**: Chat API responses

## State Transitions

### Task States
- **Created**: Task is initially created with is_completed = false
- **Completed**: Task is updated with is_completed = true via toggle completion
- **Updated**: Task title or description is modified
- **Deleted**: Task is removed from the system

### ChatSession States
- **Active**: Session is created and ready for messages
- **Updated**: Session receives new messages and updates timestamp
- **Renamed**: Session title is updated (auto-generated or user-defined)
- **Archived**: Session is no longer active but retained for history

## Validation Rules

### Task Validation
- Title must be 1-200 characters
- Description must be 0-2000 characters
- User must be authenticated to create/update/delete tasks
- Task must belong to the authenticated user

### ChatSession Validation
- Session must belong to the authenticated user
- Message content must be 1-10000 characters
- Session must exist before adding messages