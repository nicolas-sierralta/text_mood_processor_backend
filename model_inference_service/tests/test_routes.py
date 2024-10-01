from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_inference_route_valid():
    """
    Test the inference route with valid data.
    """
    response = client.post("/api/inference", json={"text": "I am very happy today!"})
    assert response.status_code == 200
    json_data = response.json()
    assert "emotions" in json_data
    assert "predominant_emotion" in json_data
    assert "confidence" in json_data

def test_inference_route_empty_text():
    """
    Test the inference route with empty text (should return 422 for validation error).
    """
    response = client.post("/api/inference", json={"text": ""})
    assert response.status_code == 422  # Pydantic returns 422 for invalid inputs
    json_data = response.json()
    assert "detail" in json_data

def test_inference_route_missing_text():
    """
    Test the inference route with missing text field (should return 422 for validation error).
    """
    response = client.post("/api/inference", json={})
    assert response.status_code == 422
    json_data = response.json()
    assert "detail" in json_data

def test_inference_route_text_too_long():
    """
    Test the inference route with text that exceeds the maximum allowed length (should return 422).
    """
    long_text = "a" * 501  # 501 characters, which exceeds the limit of 500
    response = client.post("/api/inference", json={"text": long_text})
    assert response.status_code == 422
    json_data = response.json()
    assert "detail" in json_data
    # Check for specific error message related to length
    assert "The string length should not exceed 500 characters" in str(json_data["detail"])
