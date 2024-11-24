from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


#####################################################################
def add(a, b):
    """
    Suma dos números y devuelve el resultado.
    """
    return a + b


def divide(a, b):
    """
    Divide el número `a` por `b` y devuelve el resultado.
    Lanza una excepción si `b` es 0.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
