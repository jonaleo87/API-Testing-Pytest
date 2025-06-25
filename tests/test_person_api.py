import pytest
from pages.import_api import PersonAPI

@pytest.fixture
def person_api():
    return PersonAPI()

# Happy Path
def test_post_person_happy_path(person_api):
    person_id = 123
    response = person_api.post_person(person_id)

    # Si es un error de conexión, se salta
    if isinstance(response, dict) and "error" in response:
        pytest.skip(f"Error de conexión: {response['error']}")

    assert response.status_code in (200, 201), "El código de estado debe ser 200 o 201"
    assert "success" in response.json() or "message" in response.json()

# Sad Path
@pytest.mark.parametrize("invalid_id", [None, "", "abc", -1, 999999])
def test_post_person_sad_path(person_api, invalid_id):
    response = person_api.post_person(invalid_id)

    if isinstance(response, dict) and "error" in response:
        pytest.skip(f"Error de conexión: {response['error']}")

    assert response.status_code in (400, 404, 422), f"Se esperaba un error (4xx), recibido: {response.status_code}"
    assert "error" in response.json() or "message" in response.json()