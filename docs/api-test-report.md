# API Test Report

This document records the manual Swagger UI tests, automated test coverage, and validation error behavior for the FastAPI backend service.

---

## 1. Service Overview

- **Framework**: FastAPI
- **Base URL**: `http://127.0.0.1:8000`
- **Interactive Documentation (Swagger UI)**: `http://127.0.0.1:8000/docs`
- **Alternative Documentation (ReDoc)**: `http://127.0.0.1:8000/redoc`
- **OpenAPI Schema**: `http://127.0.0.1:8000/openapi.json`

---

## 2. Endpoints Under Test

| Method | Endpoint | Description | Request Model | Response Model |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/health` | Service health status, version, and UTC timestamp. Does not invoke AI models. | None | `HealthResponse` |
| `POST` | `/chat` | Processes incoming chat messages and provides structured answer objects. | `ChatRequest` | `ChatResponse` |
| `POST` | `/quiz` | Generates quiz questions for a specified topic and question count. | `QuizRequest` | `QuizResponse` |
| `POST` | `/summarise` | Produces summary structure and bullet points up to a requested limit. | `SummariseRequest` | `SummariseResponse` |

---

## 3. Swagger UI Manual Tests

### Test 1: POST /chat (Valid Request)
- **Tool**: Swagger UI (`/docs`)
- **Action**: Expand `POST /chat`, click **Try it out**, enter payload, click **Execute**.
- **Request URL**: `http://127.0.0.1:8000/chat`
- **Request Body**:
```json
{
  "message": "Explain FastAPI dependency injection"
}
```
- **Expected Status Code**: `200 OK`
- **Response Headers**: `content-type: application/json`
- **Actual Response Body**:
```json
{
  "answer": "Received: Explain FastAPI dependency injection",
  "received_message": "Explain FastAPI dependency injection",
  "timestamp": "2026-11-04T13:30:00.000000Z"
}
```
- **Result**: PASS

---

### Test 2: POST /chat (Invalid Request - Empty Message)
- **Tool**: Swagger UI (`/docs`)
- **Action**: Enter payload violating `min_length=1`, click **Execute**.
- **Request URL**: `http://127.0.0.1:8000/chat`
- **Request Body**:
```json
{
  "message": ""
}
```
- **Expected Status Code**: `422 Unprocessable Entity`
- **Actual Response Body**:
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "message"
      ],
      "msg": "String should have at least 1 character",
      "input": "",
      "ctx": {
        "min_length": 1
      }
    }
  ]
}
```
- **Result**: PASS

---

### Test 3: POST /quiz (Valid Request)
- **Tool**: Swagger UI (`/docs`)
- **Request URL**: `http://127.0.0.1:8000/quiz`
- **Request Body**:
```json
{
  "topic": "Python Asynchronous Programming",
  "num_questions": 2
}
```
- **Expected Status Code**: `200 OK`
- **Actual Response Body**:
```json
{
  "topic": "Python Asynchronous Programming",
  "total_questions": 2,
  "questions": [
    {
      "id": 1,
      "question": "Sample question 1 about Python Asynchronous Programming?",
      "options": [
        "Python Asynchronous Programming Answer option 1",
        "Python Asynchronous Programming Answer option 2",
        "Python Asynchronous Programming Answer option 3",
        "Python Asynchronous Programming Answer option 4"
      ],
      "answer": "Python Asynchronous Programming Answer option 1"
    },
    {
      "id": 2,
      "question": "Sample question 2 about Python Asynchronous Programming?",
      "options": [
        "Python Asynchronous Programming Answer option 1",
        "Python Asynchronous Programming Answer option 2",
        "Python Asynchronous Programming Answer option 3",
        "Python Asynchronous Programming Answer option 4"
      ],
      "answer": "Python Asynchronous Programming Answer option 1"
    }
  ]
}
```
- **Result**: PASS

---

### Test 4: POST /quiz (Invalid Request - Number of Questions Exceeds Limit)
- **Tool**: Swagger UI (`/docs`)
- **Request URL**: `http://127.0.0.1:8000/quiz`
- **Request Body**:
```json
{
  "topic": "Data Science",
  "num_questions": 50
}
```
- **Expected Status Code**: `422 Unprocessable Entity`
- **Actual Response Body**:
```json
{
  "detail": [
    {
      "type": "less_than_equal",
      "loc": [
        "body",
        "num_questions"
      ],
      "msg": "Input should be less than or equal to 20",
      "input": 50,
      "ctx": {
        "le": 20
      }
    }
  ]
}
```
- **Result**: PASS

---

### Test 5: POST /summarise (Valid Request)
- **Tool**: Swagger UI (`/docs`)
- **Request URL**: `http://127.0.0.1:8000/summarise`
- **Request Body**:
```json
{
  "text": "FastAPI is designed for building modern APIs. It supports high concurrency with asyncio. Automatic OpenAPI documentation is included by default.",
  "max_bullets": 3
}
```
- **Expected Status Code**: `200 OK`
- **Actual Response Body**:
```json
{
  "summary": "Summary: FastAPI is designed for building modern APIs",
  "bullets": [
    "Key point: FastAPI is designed for building modern APIs",
    "Key point: It supports high concurrency with asyncio",
    "Key point: Automatic OpenAPI documentation is included by default"
  ],
  "bullet_count": 3,
  "original_length": 145
}
```
- **Result**: PASS

---

### Test 6: POST /summarise (Invalid Request - Text Too Short)
- **Tool**: Swagger UI (`/docs`)
- **Request URL**: `http://127.0.0.1:8000/summarise`
- **Request Body**:
```json
{
  "text": "Hi",
  "max_bullets": 2
}
```
- **Expected Status Code**: `422 Unprocessable Entity`
- **Actual Response Body**:
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "text"
      ],
      "msg": "String should have at least 5 characters",
      "input": "Hi",
      "ctx": {
        "min_length": 5
      }
    }
  ]
}
```
- **Result**: PASS

---

## 4. Automated Test Suite Results

The automated test suite is located in `tests/test_api.py` and executed using `pytest` and `httpx` (`fastapi.testclient.TestClient`).

### Test Execution Command
```bash
python -m pytest -v
```

### Execution Summary
| Test Function | Target Endpoint | Scenario | Status |
| :--- | :--- | :--- | :--- |
| `test_health_endpoint` | `GET /health` | Valid query, validates schema fields | PASSED |
| `test_chat_endpoint_valid` | `POST /chat` | Valid text payload | PASSED |
| `test_chat_endpoint_invalid` | `POST /chat` | Empty string payload (`min_length` check) | PASSED |
| `test_quiz_endpoint_valid` | `POST /quiz` | Valid topic & question count | PASSED |
| `test_quiz_endpoint_invalid` | `POST /quiz` | Out-of-bounds `num_questions` (`le=20` check) | PASSED |
| `test_summarise_endpoint_valid` | `POST /summarise` | Valid text and max_bullets | PASSED |
| `test_summarise_endpoint_invalid` | `POST /summarise` | Text length < 5 characters | PASSED |

**Total Result**: 7 passed in 1.60s.

