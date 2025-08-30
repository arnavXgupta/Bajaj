from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app instance from your main.py file

# Create a client to interact with the app
client = TestClient(app)

def test_health_check():
    """
    Tests the /health endpoint to ensure the API is running and healthy.
    """
    # Make a GET request to the /health endpoint
    response = client.get("/health")
    
    # Assert that the HTTP status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert that the response body is the expected JSON
    assert response.json() == {"status": "healthy"}

def test_read_root():
    """
    Tests the root / endpoint.
    """
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"status": "API is running. Use /docs for documentation."}