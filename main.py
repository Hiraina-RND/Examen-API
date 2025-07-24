from typing import Set, List
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
import uvicorn


app = FastAPI()

@app.get("/hello")
def hello():
    return JSONResponse({"message":"Hello world"},  status_code=200)


@app.get("/welcome")
def welcome(name: str):
    return JSONResponse({"message":f"Hello {name}"}, status_code=200)


class Student(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int

Student_list: List[Student] = []

@app.post("/students")
def lister_student(students: List[Student]):
    return JSONResponse(status_code=200, content=students)



@app.put("/students")
def modifer_student(student: Student):
    for i, std in Student_list:
        if std.reference == student.reference:
            return JSONResponse({"message":"Modification avec succès."}, status_code=200)


    Student_list.append(student)
    return JSONResponse(status_code=200, content=student)











