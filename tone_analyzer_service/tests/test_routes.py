import pytest
import requests_mock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
INFERENCE_SERVICE_URL = "http://model_inference_service:8001/api/inference"

def test_analyze_route_valid_text():
    # Mockear una respuesta válida del servicio de inferencia
    with requests_mock.Mocker() as mock:
        mock.post(INFERENCE_SERVICE_URL, json={
            "emotions": [
                {"emotion": "joy", "percentage": 80.0},
                {"emotion": "neutral", "percentage": 20.0}
            ],
            "predominant_emotion": "joy",
            "confidence": 80.0
        }, status_code=200)

        response = client.post("/api/analyze", json={"text": "I am happy today!"})
        assert response.status_code == 200
        result = response.json()
        assert result["predominant_emotion"] == "joy"
        assert result["confidence"] == 80.0

def test_analyze_route_empty_text():
    """
    Test the /api/analyze route with empty text, expecting a 400 response due to validation failure.
    """
    response = client.post("/api/analyze", json={"text": ""})
    assert response.status_code == 422  # Debería devolver 400 debido a la validación personalizada

def test_analyze_route_too_long_text():
    """
    Test the /api/analyze route with text exceeding the maximum allowed length, expecting a 400 response.
    """
    long_text = "a" * 501  # 501 characters, exceeds limit of 500
    response = client.post("/api/analyze", json={"text": long_text})
    assert response.status_code == 400  # Debería devolver 400 debido a la validación de longitud
