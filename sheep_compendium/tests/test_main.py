from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep")

    assert response.status_code == 200

    assert response.json() == {
        # Expected JSON structure

        "id" : 1,
        "name" : "Spice",
        "breed" : "Gotland",
        "sex" : "ewe"
    }

def test_add_sheep():
    # Prepare the new sheep data
    new_sheep = {
        "id": 7,
        "name": "Luna",
        "breed": "Merino",
        "sex": "ewe"
    }

    # Send a POST request to add the new sheep
    response = client.post("/sheep", json=new_sheep)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep

    # Verify the sheep was actually added by retrieving it by ID
    get_response = client.get(f"/sheep/{new_sheep['id']}")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep