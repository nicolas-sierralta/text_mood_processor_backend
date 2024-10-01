import pytest
from fastapi.testclient import TestClient
from app.main import app 
from unittest.mock import patch

# Definir el cliente de pruebas
client = TestClient(app)

def test_change_tone_empty_text_error():
    response = client.post("/api/change-tone", json={
        "text": "",
        "target_tone": "friendly"
    })

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "text"],
                "msg": "String should have at least 1 character",
                "type": "value_error.string.min_length",
                "ctx": {"min_length": 1},
                "input": ""  # Este campo debe coincidir con la entrada vacía
            }
        ]
    }

def test_change_tone_text_too_long_error():
    long_text = "x" * 501  # Texto de 501 caracteres, excediendo el límite de 500

    response = client.post("/api/change-tone", json={
        "text": long_text,
        "target_tone": "friendly"
    })

    assert response.status_code == 422
    assert response.json() == {
        "detail": "The string length should not exceed 500 characters. Given length: 501"
    }


def test_change_tone_empty_text_error():
    response = client.post("/api/change-tone", json={
        "text": "",
        "target_tone": "friendly"
    })

    assert response.status_code == 422

    # Actualización para reflejar el mensaje real devuelto por FastAPI
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "text"],
                "msg": "String should have at least 1 character",
                "type": "string_too_short",  # Cambiado para reflejar lo que FastAPI realmente devuelve
                "ctx": {"min_length": 1},
                "input": ""  # Este campo coincide con la entrada vacía
            }
        ]
    }
