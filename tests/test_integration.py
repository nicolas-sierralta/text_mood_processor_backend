import requests

API_GATEWAY_URL = "http://127.0.0.1:8000"  # Adjust the URL as needed

def test_integration_tone_analysis_success():
    """
    Integration test for a successful tone analysis through the API Gateway.
    """
    response = requests.post(f"{API_GATEWAY_URL}/api/analyze-tone", json={"text": "I am very happy today!"})

    assert response.status_code == 200  # Verify that the response is successful
    result = response.json()

    assert result["predominant_emotion"] == "joy"  # Verify the 'predominant_emotion' field and its value
    assert result["confidence"] == 99.9  # Verify the confidence level of the prediction

def test_integration_tone_analysis_empty_text():
    """
    Integration test to analyze an empty text. The API Gateway should return a validation error.
    """
    response = requests.post(f"{API_GATEWAY_URL}/api/analyze-tone", json={"text": ""})

    assert response.status_code == 422  # Verify that the status code is 422 (Unprocessable Entity)
    result = response.json()

    # Verify that the error message is as expected for Pydantic validation
    assert result["detail"][0]["msg"] == "String should have at least 1 character"

def test_integration_tone_analysis_text_too_long():
    """
    Test to analyze a text that exceeds the maximum allowed length (2000 characters).
    """
    long_text = "a" * 2001  # Texto que excede el límite de 2000 caracteres
    response = requests.post(f"{API_GATEWAY_URL}/api/analyze-tone", json={"text": long_text})

    assert response.status_code == 422  # Pydantic validation should return 422
    result = response.json()

    # Verifica que el error esté relacionado con la longitud
    assert "String should have at most 2000 characters" in result["detail"][0]["msg"]

def test_integration_tone_analysis_non_text_input():
    """
    Test to analyze a text that contains only numbers or symbols.
    """
    response = requests.post(f"{API_GATEWAY_URL}/api/analyze-tone", json={"text": "1234567890!"})

    assert response.status_code == 200  # The analysis should still be successful
    result = response.json()

    assert "predominant_emotion" in result  # Verify that there is a predicted emotion

def test_integration_tone_analysis_invalid_json():
    """
    Test to analyze a request with a malformed field.
    """
    response = requests.post(f"{API_GATEWAY_URL}/api/analyze-tone", json={"texto": "I am happy!"})  # Incorrect key

    assert response.status_code == 422  # Verify that a validation error is returned
    result = response.json()

    # Verify the error message (adjusted to match the real message)
    assert result["detail"][0]["msg"] == "Field required"  # With 'F' capitalized

def test_integration_change_tone_success():
    """
    Integration test for a successful tone change through the API Gateway.
    """
    response = requests.post(f"{API_GATEWAY_URL}/api/change-tone", json={"text": "I am feeling great today!", "target_tone": "serious"})

    assert response.status_code == 200  

def test_integration_change_tone_empty_text():
    """
    Integration test to analyze an empty text. The API Gateway should return a validation error.
    """
    response = requests.post(f"{API_GATEWAY_URL}/api/change-tone", json={"text": "", "target_tone": "friendly"})

    assert response.status_code == 422  # Verificar que el código de estado sea 422
    result = response.json()

    assert result["detail"][0]["msg"] == "String should have at least 1 character"

def test_integration_change_tone_empty_tone():
    """
    Integration test to analyze an empty target tone. The API Gateway should return a validation error.
    """
    response = requests.post(f"{API_GATEWAY_URL}/api/change-tone", json={"text": "This is a valid text", "target_tone": ""})

    assert response.status_code == 422  # Verificar que el código de estado sea 422
    result = response.json()

    assert result["detail"][0]["msg"] == "String should have at least 1 character"

def test_integration_change_tone_text_too_long():
    """
    Test to analyze a text that exceeds the maximum allowed length (2000 characters).
    """
    long_text = "x" * 2001  # Texto que excede el límite de 2000 caracteres
    response = requests.post(f"{API_GATEWAY_URL}/api/change-tone", json={"text": long_text, "target_tone": "friendly"})

    assert response.status_code == 422  # La validación de Pydantic debería devolver 422
    result = response.json()

    assert "String should have at most 2000 characters" in result["detail"][0]["msg"]

def test_integration_change_tone_invalid_json():
    """
    Test to analyze a request with a malformed field.
    """
    response = requests.post(f"{API_GATEWAY_URL}/api/change-tone", json={"texto": "I am happy!"})  # Clave incorrecta

    assert response.status_code == 422  # Verificar que se devuelva un error de validación
    result = response.json()

    assert result["detail"][0]["msg"] == "Field required"  # Con 'F' en mayúscula