from fastapi import FastAPI, HTTPException
from app.calculator import Calculator

app = FastAPI(title="Calculator API", version="1.0")

calc = Calculator()


@app.get("/")
def home():
    return {"message": "Calculator API Running"}


@app.get("/add")
def add(a: float, b: float):
    return {"result": calc.add(a, b)}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": calc.subtract(a, b)}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": calc.multiply(a, b)}


@app.get("/divide")
def divide(a: float, b: float):
    try:
        return {"result": calc.divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/power")
def power(a: float, b: float):
    return {"result": calc.power(a, b)}


@app.get("/sqrt")
def sqrt(a: float):
    try:
        return {"result": calc.sqrt(a)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/quadratic")
def quadratic(a: float, b: float, c: float):
    try:
        roots = calc.quadratic(a, b, c)
        return {"roots": roots}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
@app.get("/factorial")
def factorial(n: int):
    try:
        return {"result": calc.factorial(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

