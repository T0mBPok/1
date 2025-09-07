from fastapi import Form
from pydantic import BaseModel

class GetAnimal(BaseModel):
    id: int
    kind: str
    name: str
    age: int
    
class AddAnimal(BaseModel):
    kind: str
    name: str
    age: int
    
    @classmethod
    def as_form(
        cls,
        kind: str = Form(...),
        name: str = Form(...),
        age: int = Form(...),
    ):
        return cls(kind=kind, name=name, age=age)
    
class UpdateAnimal(BaseModel):
    kind: str | None = None
    name: str | None = None
    age: int | None = None