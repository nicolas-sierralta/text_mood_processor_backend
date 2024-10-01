import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.business_logic.change_tone import client

client_test = TestClient(app)


def test_change_tone_empty_text():
    response = client_test.post("/api/change-tone", json={
        "text": "",
        "target_tone": "friendly"
    })

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "text"],
                "msg": "String should have at least 1 character",
                "type": "string_too_short",
                "ctx": {"min_length": 1},
                "input": ""
            }
        ]
    }

def test_change_tone_openai_error():
    with patch.object(client.chat.completions, 'create', side_effect=Exception("OpenAI API error")):
        response = client_test.post("/api/change-tone", json={
            "text": "I am feeling great today!",
            "target_tone": "serious"
        })

        assert response.status_code == 500
        assert response.json() == {"detail": "An error occurred during tone change."}

def test_change_tone_text_too_long():
    long_text = "x" * 501  # Asumiendo que el límite sea 500 caracteres

    response = client_test.post("/api/change-tone", json={
        "text": long_text,
        "target_tone": "friendly"
    })

    assert response.status_code == 422
    assert response.json() == {
        "detail": f"The string length should not exceed 500 characters. Given length: 501"
    }

def test_change_tone_empty_tone():
    response = client_test.post("/api/change-tone", json={
        "text": "This is a valid text",
        "target_tone": ""
    })

    assert response.status_code == 422
    assert response.json() == {
        "detail": "The value must be a non-empty string."
    }
