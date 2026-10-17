from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

try:
    User(name="Venkatesh", age="abc")
except ValidationError as e:
    print(e)