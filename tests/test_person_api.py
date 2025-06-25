import pytest
import random
from pages.import_api import PersonAPI
from utils.db_utils import get_person_from_db

# NOTA: Este test asume que la API y la base de datos están disponibles.
# Si no lo están, el test puede fallar o ser saltado por error de conexión.
@pytest.fixture
def person_api():
    return PersonAPI()

# Happy Path
def test_post_person_happy_path(person_api):
    person_id = random.randint(100, 999)
    response = person_api.post_person(person_id)
    print(f"\n[INFO] Probando con person_id: {person_id}")
    print(f"[INFO] Status code: {getattr(response, 'status_code', 'N/A')}")
    print(f"[INFO] Respuesta: {getattr(response, 'json', lambda: {})()}")

    # Si es un error de conexión, se salta
    if isinstance(response, dict) and "error" in response:
        pytest.skip(f"Error de conexión: {response['error']}")

    assert response.status_code in (200, 201), "El código de estado debe ser 200 o 201"
    json_resp = response.json()
    assert "success" in json_resp or "message" in json_resp
    print(f"[INFO] Mensaje de respuesta: {json_resp.get('message', json_resp.get('success', 'Sin mensaje'))}")

    db_row = get_person_from_db(person_id)
    if db_row is not None:
        print(f"[INFO] personId {person_id} encontrado en la base de datos: {db_row}")
    else:
        print(f"[ERROR] personId {person_id} NO encontrado en la base de datos")
    assert db_row is not None, f"personId {person_id} no encontrado en la base de datos"


# Sad Path
@pytest.mark.parametrize("invalid_id", [None, "", "abc", -1, 999999])
def test_post_person_sad_path(person_api, invalid_id):
    response = person_api.post_person(invalid_id)

    if isinstance(response, dict) and "error" in response:
        pytest.skip(f"Error de conexión: {response['error']}")

    assert response.status_code in (400, 404, 422), f"Se esperaba un error (4xx), recibido: {response.status_code}"
    assert "error" in response.json() or "message" in response.json()