# FastAPI AI Backend Starter

A clean, modular FastAPI backend providing four core endpoints: `/health`, `/chat`, `/quiz`, and `/summarise`. Built with Pydantic request/response validation.

## Project Structure

```
endpoint04112026/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       ├── chat.py
│       ├── health.py
│       ├── quiz.py
│       └── summarise.py
├── docs/
│   └── api-test-report.md
├── main.py
├── README.md
└── requirements.txt
```

## Setup & Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application server:
```bash
python main.py
```
or via Uvicorn CLI:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

3. Open Swagger UI in your browser:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

### 1. `GET /health`
Returns system status, service version, and current UTC timestamp. Does not invoke any downstream AI model.
- **Response**:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2026-11-04T13:30:00.000000Z"
}
```

### 2. `POST /chat`
Receives a user message and returns a structured response object.
- **Request Body**:
```json
{
  "message": "Hello world"
}
```
- **Validation**: `message` must be between 1 and 2000 characters.
- **Response**:
```json
{
  "answer": "Received: Hello world",
  "received_message": "Hello world",
  "timestamp": "2026-11-04T13:30:00.000000Z"
}
```

### 3. `POST /quiz`
Receives a topic and desired number of questions, returning a list of quiz question objects.
- **Request Body**:
```json
{
  "topic": "Python",
  "num_questions": 3
}
```
- **Validation**: `topic` between 1 and 100 characters; `num_questions` between 1 and 20.
- **Response**:
```json
{
  "topic": "Python",
  "total_questions": 3,
  "questions": [
    {
      "id": 1,
      "question": "Sample question 1 about Python?",
      "options": [
        "Python Answer option 1",
        "Python Answer option 2",
        "Python Answer option 3",
        "Python Answer option 4"
      ],
      "answer": "Python Answer option 1"
    }
  ]
}
```

### 4. `POST /summarise`
Receives a text input and maximum bullet point limit, returning a structured summary.
- **Request Body**:
```json
{
  "text": "FastAPI is a modern web framework for Python. It offers high performance and easy data validation.",
  "max_bullets": 3
}
```
- **Validation**: `text` between 5 and 10000 characters; `max_bullets` between 1 and 10.
- **Response**:
```json
{
  "summary": "Summary: FastAPI is a modern web framework for Python",
  "bullets": [
    "Key point: FastAPI is a modern web framework for Python",
    "Key point: It offers high performance and easy data validation"
  ],
  "bullet_count": 2,
  "original_length": 99
}
```

API verification and Swagger UI manual test details can be found in [docs/api-test-report.md](docs/api-test-report.md).
