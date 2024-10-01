from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name" : "john",
        "age" : 17,
        "class" : 10
    },
    2: {
        "name" : "Ashru",
        "age" : 22,
        "class" : 10  
    },
    3: {
        "name" : "john",
        "age": 23,
        "class": 7
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    year: Optional[str]=None
    

@app.get("/")
def index():
    return{"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0, lt=4)):
     return students[student_id]

@app.get("/get-by-name-age/{id}")
def get_student(
    id : int, 
    name: Optional[str]= None,  
    class_id : Optional[int]= None
    ):

    if name is None and class_id is None:
        return students[id]
    

    if name is None:
        result = []
        for student_id in students:
            details = students[student_id]
            if details['class'] == class_id:
                result.append(details)

        return result if result else 'Data Not Found'
    
    if class_id is None:
        result = []
        for student in students:
            details=students[student]
            print(student , '-->', details)
        return None
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"error" : "student exist"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id : int, student : UpdateStudent):
    if student_id not in students:
        return {"student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

@app.delete("/delete-student/{student_id}")
def update_student(student_id : int):
    if student_id not in students:
        return {"Error" : "student does not exist"}
    del students[student_id]
    return {"message": "student successfully deleted"}
    
    
    
    
    return students[student_id]




    # for student_id in students:
    #     # print(student)
    #     details= students[student_id]
    #     if details["age"] == class_id and details["name"] == name and student_id==id:
    #         return students[student_id]
    # return{"Data": "Not found"}
    