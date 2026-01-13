# ADK Agent Server with Session, Memory, and Example Services

An ADK agent application demonstrating session management, memory services, and streaming responses through a FastAPI server and web-based client interface.

## Overview

This lab demonstrates:
- ADK agent with session and memory services
- FastAPI server exposing agent functionality via HTTP endpoints
- Streaming Server-Sent Events (SSE) for real-time session updates
- Web-based client interface for agent interaction
- Support for in-memory, Vertex AI, and database-backed services

## Architecture

```
┌─────────────────┐
│  client.html    │  Web-based UI
│  (Browser)      │  Opens in browser
└────────┬────────┘
         │ HTTP/SSE
         ▼
┌─────────────────┐
│ server.py       │  FastAPI Server
│                 │  - Home page (/)
│  ADK Components │  - Session management
│  - Agent        │  - Streaming chat
│  - Runner       │  - Memory service
│  - Sessions     │
│  - Memory       │
└─────────────────┘
```

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the API server

```bash
python server.py
```

Server runs at `http://localhost:8000`

### 3. Access the application

**Option A: Via Server Home Page (Recommended)**

Open `http://localhost:8000` in your browser. The home page provides a link to launch the client application.

**Option B: Direct Client Access**

The client can be served independently in two ways:

1. **Using Python's built-in server:**
   ```bash
   python -m http.server 8080
   ```
   Then open `http://localhost:8080/client.html`

2. **Opening directly in browser:**
   Simply open `client.html` in your browser. Update the API server URL in the client if needed.

## API Endpoints

### `GET /`
Home page with link to client application.

### `POST /sessions`
Create a new session.

**Request:**
```json
{
  "user_id": "user_123",
  "initial_state": {"key": "value"}
}
```

**Response:**
```json
{
  "session_id": "abc-123",
  "user_id": "user_123"
}
```

### `POST /chat`
Send a message to the agent and receive streaming updates.

**Request:**
```json
{
  "user_id": "user_123",
  "session_id": "abc-123",
  "message": "Hello!"
}
```

**Response:** Server-Sent Events (SSE) stream containing:
- Session card updates (real-time session state)
- Final response from the agent

### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Files

- **server.py**: FastAPI server with ADK integration
  - Home page handler with link to client
  - Session management endpoints
  - Streaming chat endpoint with SSE
  - Support for multiple service providers (in-memory, Vertex AI, database)
  
- **client.html**: Web-based client interface
  - Interactive chat UI
  - Session state visualization
  - Real-time streaming updates
  - Can be served independently or accessed via server home page

- **agent.py**: ADK agent definition with tools and instructions

- **utilities.py**: Helper functions
  - Session and event logging
  - Home page generation
  - URL manipulation utilities

- **scripts/setup_session.py**: Session initialization script

## Configuration

The server supports multiple service providers via environment variables:

```bash
# Session Service Provider
SESSION_SERVICE_PROVIDER=in_memory  # Options: in_memory, vertex, db

# Memory Service Provider  
MEMORY_SERVICE_PROVIDER=in_memory   # Options: in_memory, vertex

# For Vertex AI services
GOOGLE_CLOUD_PROJECT=your-project
GOOGLE_CLOUD_LOCATION=us-central1

# For database services
DATABASE_URL=sqlite:///./test.db
```

## Key Features

1. **Streaming Responses**: Real-time agent responses via Server-Sent Events
2. **Session Visualization**: Live updates of session state and events
3. **Flexible Service Providers**: Switch between in-memory, Vertex AI, and database backends
4. **Web-Based Interface**: Modern, responsive client UI
5. **Direct Browser Access**: Client can run standalone without server

## Key ADK Patterns Illustrated

1. **Session Service Configuration**:
   ```python
   session_service = InMemorySessionService()
   # Or for production:
   # session_service = VertexAiSessionService(project=..., location=...)
   # session_service = DatabaseSessionService(db_url=...)
   ```

2. **Runner with Services**:
   ```python
   runner = Runner(
       app_name=APP_NAME,
       agent=root_agent,
       session_service=session_service,
       memory_service=memory_service
   )
   ```

3. **Streaming Agent Execution**:
   ```python
   async for event in runner.run_async(
       user_id=user_id,
       session_id=session_id,
       new_message=user_message
   ):
       # Process and stream events to client
   ```

## Requirements

```
google-adk      # Google Agent Development Kit
fastapi         # Web framework
uvicorn         # ASGI server
python-dotenv   # Environment configuration
```

## Notes

- **Client Flexibility**: The client.html can be opened directly in a browser or served via any simple HTTP server (e.g., `python -m http.server 8080`)
- **Service Providers**: Supports in-memory services for development and Vertex AI/database services for production
- **Streaming Updates**: Uses Server-Sent Events for real-time session state visualization
- **Session Persistence**: Choose appropriate service provider based on your persistence needs
- For production deployments, use Vertex AI or database-backed session and memory services
