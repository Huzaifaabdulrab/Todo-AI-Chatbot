# Actionable Tasks: Fix Chatbot API Endpoint Mismatch

**Feature**: Fix Chatbot API Endpoint Mismatch  
**Feature Branch**: `001-fix-chatbot-tasks`  
**Created**: 2026-02-12  
**Status**: Ready for Implementation  

## Overview

This document breaks down the implementation of fixes for the chatbot API endpoint mismatch that's causing 404 errors. The primary goal is to align frontend API calls with backend endpoints to ensure proper communication.

## Dependencies

All tasks are foundational and must be completed before other chatbot functionality can work properly.

## Parallel Execution Examples

- No parallel execution possible as these are sequential fixes to the API communication layer

---

## Phase 1: Setup

### Goal
No setup tasks required for this focused fix.

---

## Phase 2: Foundational Tasks

### Goal
Fix the API endpoint mismatch that's causing 404 errors between frontend and backend.

- [X] T001 Fix frontend API baseURL or request path to remove double /api in src/services/chatApi.js
- [X] T002 Verify backend chat endpoint path and update frontend call to match exactly in src/services/chatApi.js
- [X] T003 Add logging/error details for next steps (session/500) in src/services/chatApi.js

---

## Phase 3: User Story 1 - Create Tasks via Chat Interface (Priority: P1)

### Goal
Enable users to create tasks through the chatbot interface after fixing the API communication layer.

### Independent Test
Opening the chatbot tab, entering a task description, and verifying that the task appears in the task list and is persisted in the database.

- [X] T004 [US1] Test that API calls now succeed after endpoint fixes in src/services/chatApi.js

---

## Phase 4: Polish & Cross-Cutting Concerns

### Goal
Finalize implementation with verification.

- [X] T005 Verify that 404 errors are resolved and API communication works properly
- [X] T006 Test end-to-end flow: send message via chat → verify API response received

---

## Implementation Strategy

### MVP Scope
The minimum viable product includes:
- Fixing the API endpoint mismatch (T001-T002)
- Basic API communication verification (T004)

### Incremental Delivery
1. **Phase 2**: API endpoint fixes
2. **Phase 3**: Basic functionality verification
3. **Phase 4**: End-to-end testing