# Actionable Tasks: Fix Chatbot CRUD Operations

**Feature**: Fix Chatbot CRUD Operations  
**Feature Branch**: `001-fix-chatbot-crud`  
**Created**: 2026-02-12  
**Status**: Ready for Implementation  

## Overview

This document breaks down the implementation of fixes for the chatbot CRUD operations. The primary goal is to resolve API endpoint mismatches, implement full CRUD functionality via the chatbot interface, and ensure consistent behavior between form-based and chat-based task operations.

## Dependencies

User stories can be implemented in sequence with later stories depending on earlier ones:
- US2 (read tasks) depends on foundational fixes from US1 (create tasks)
- US3 (update tasks) depends on US1 and US2
- US4 (delete tasks) depends on US1, US2, and US3

## Parallel Execution Examples

- **Backend tasks** (API fixes, MCP agent config) can be developed in parallel with **frontend tasks** (UI fixes, error handling)
- **Different CRUD operations** (after foundational tasks) can be developed in parallel

---

## Phase 1: Setup

### Goal
Prepare the development environment and ensure all necessary configurations are in place.

- [ ] T001 Set up development environment with Python 3.11, Node.js 18+, and PostgreSQL
- [ ] T002 Verify that GEMINI_API_KEY is properly configured in environment variables
- [ ] T003 Ensure backend and frontend can connect to the database and communicate with each other

---

## Phase 2: Foundational Tasks

### Goal
Address core infrastructure issues that block user story implementation.

- [X] T004 [P] Fix API endpoint mismatch in frontend chat service (resolve double /api issue in chatApi.js)
- [X] T005 [P] Verify backend chat API endpoint registration and confirm exact path
- [X] T006 [P] Ensure MCP agent is properly configured to handle all CRUD function calls
- [X] T007 [P] Verify database connection and transaction handling for all task operations

---

## Phase 3: User Story 1 - Create Tasks via Chat Interface (Priority: P1)

### Goal
Enable users to create tasks through the chatbot interface with natural language processing.

### Independent Test
Opening the chatbot tab, entering a task description (e.g., "Create a task to buy groceries"), and verifying that the task appears in the task list and is persisted in the database.

- [X] T008 [US1] Update frontend chat API service to use correct endpoint path in src/services/chatApi.js
- [X] T009 [US1] Verify that the MCP agent properly calls the add_task function when users request task creation
- [X] T010 [US1] Ensure the add_task tool in backend/src/mcp/tool.py correctly creates tasks via TasksService
- [X] T011 [US1] Test that tasks created via chat have the same schema as form-created tasks
- [X] T012 [US1] Verify that chat-created tasks appear in the task list alongside form-created tasks
- [X] T013 [US1] Implement proper error handling in the chat task creation flow
- [X] T014 [US1] Add logging to track task creation success/failure from chat interface

---

## Phase 4: User Story 2 - Read/List Tasks via Chat Interface (Priority: P2)

### Goal
Allow users to list/view their tasks through the chatbot interface using natural language.

### Independent Test
Opening the chatbot tab, asking to see tasks (e.g., "Show me my tasks"), and verifying that the chatbot responds with the user's task list.

- [X] T015 [US2] Implement list_tasks function in the MCP agent to handle read operations
- [X] T016 [US2] Update the frontend to properly display task lists returned from the chat interface
- [X] T017 [US2] Ensure the list_tasks tool in backend/src/mcp/tool.py correctly retrieves tasks via TasksService
- [X] T018 [US2] Test that tasks listed via chat match the format of form-based task listings
- [X] T019 [US2] Verify that the chatbot can distinguish between list requests and other commands
- [X] T020 [US2] Add proper error handling for cases when user has no tasks

---

## Phase 5: User Story 3 - Update/Edit Tasks via Chat Interface (Priority: P3)

### Goal
Allow users to update/edit their tasks through the chatbot interface using natural language.

### Independent Test
Asking the chatbot to update a specific task (e.g., "Update the meeting task to next week") and verifying that the task is updated in the database and reflects the changes in the task list.

- [X] T021 [US3] Implement update_task function in the MCP agent to handle update operations
- [X] T022 [US3] Update the frontend to properly handle task update confirmations from the chat interface
- [X] T023 [US3] Ensure the update_task tool in backend/src/mcp/tool.py correctly modifies tasks via TasksService
- [X] T024 [US3] Test that tasks updated via chat maintain consistency with form-based updates
- [X] T025 [US3] Verify that the chatbot can identify specific tasks to update based on user description
- [X] T026 [US3] Add proper error handling for cases when requested task doesn't exist

---

## Phase 6: User Story 4 - Delete Tasks via Chat Interface (Priority: P4)

### Goal
Allow users to delete their tasks through the chatbot interface using natural language.

### Independent Test
Asking the chatbot to delete a specific task (e.g., "Delete the doctor appointment task") and verifying that the task is removed from the database and no longer appears in the task list.

- [X] T027 [US4] Implement delete_task function in the MCP agent to handle deletion operations
- [X] T028 [US4] Update the frontend to properly handle task deletion confirmations from the chat interface
- [X] T029 [US4] Ensure the delete_task tool in backend/src/mcp/tool.py correctly removes tasks via TasksService
- [X] T030 [US4] Test that tasks deleted via chat are properly removed from the UI
- [X] T031 [US4] Verify that the chatbot can identify specific tasks to delete based on user description
- [X] T032 [US4] Add proper error handling and confirmation prompts for task deletions

---

## Phase 7: Polish & Cross-Cutting Concerns

### Goal
Finalize implementation with quality improvements and verification.

- [X] T033 Verify that all acceptance scenarios from user stories are satisfied
- [X] T034 Test end-to-end flow: create task via chat → verify in task list → update via chat → verify changes → delete via chat
- [X] T035 Ensure consistency between chat-created and form-created tasks in UI
- [X] T036 Verify that all edge cases from spec are handled appropriately
- [X] T037 Conduct performance testing to ensure task operations via chat meet 3-second requirement
- [X] T038 Update documentation with any changes made during implementation
- [X] T039 Perform final integration test of all components working together

---

## Implementation Strategy

### MVP Scope
The minimum viable product includes:
- Fixing the API endpoint mismatch (T004)
- Enabling basic task creation via chat (T008-T012)
- Basic error handling (T013)

### Incremental Delivery
1. **Phase 1-2**: Environment setup and foundational fixes
2. **Phase 3**: Core task creation functionality
3. **Phase 4**: Task listing functionality
4. **Phase 5**: Task update functionality
5. **Phase 6**: Task deletion functionality
6. **Phase 7**: Polish and verification