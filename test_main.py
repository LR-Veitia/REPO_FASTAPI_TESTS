import pytest
from fastapi.testclient import TestClient
from main import app
from main import add, divide

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_item():
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}


def test_read_item_without_query():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}


###############################################################################
# Pruebas para la función add
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


@pytest.mark.parametrize(
    "a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (100, 200, 300)]
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


# Pruebas para la función divide
def test_divide():
    assert divide(6, 2) == 3
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError, match="No se puede dividir por cero."):
        divide(10, 0)


def test_divide_invalid_input():
    with pytest.raises(TypeError):
        divide(10, "a")


# Uso de fixtures
@pytest.fixture
def numbers():
    return {"a": 10, "b": 5, "c": 0}


def test_add_with_fixture(numbers):
    assert add(numbers["a"], numbers["b"]) == 15


def test_divide_with_fixture(numbers):
    assert divide(numbers["a"], numbers["b"]) == 2


def test_divide_by_zero_with_fixture(numbers):
    with pytest.raises(ValueError):
        divide(numbers["a"], numbers["c"])


# Fixture con autouse=True
@pytest.fixture(autouse=True)
def setup_teardown():
    print("Ejecutando configuración antes de cada prueba.")
    yield
    print("Ejecutando limpieza después de cada prueba.")


def test_example_1():
    print("Ejecutando prueba 1")


def test_example_2():
    print("Ejecutando prueba 2")


# Fixture con scope
@pytest.fixture(scope="module")
def setup_module():
    print("Configurando módulo de pruebas.")
    return "data"


def test_1(setup_module):
    print(f"Test 1, usando {setup_module}")


def test_2(setup_module):
    print(f"Test 2, usando {setup_module}")


# Pruebas asíncronas
@pytest.mark.asyncio
async def test_async_function():
    import asyncio

    await asyncio.sleep(1)
    assert True


# Saltar una prueba
@pytest.mark.skip(reason="Este test se salta temporalmente.")
def test_skip_example():
    assert 1 == 1


# Prueba esperada a fallar
@pytest.mark.xfail(reason="Este test está fallando a propósito.")
def test_xfail_example():
    assert 1 == 2


# Prueba lenta
@pytest.mark.slow
def test_slow_function():
    import time

    time.sleep(5)
    assert True


# Prueba con marcador personalizado
@pytest.mark.custom_marker
def test_with_custom_marker():
    assert True


# Comparación "avanzada" de diccionarios
def test_compare_dicts():
    expected = {"name": "John", "age": 30}
    actual = {"name": "John", "age": 30}
    assert expected == actual
