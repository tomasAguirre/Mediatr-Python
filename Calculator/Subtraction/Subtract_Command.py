from pydantic import BaseModel

class Subtract_Command(BaseModel):
    numer1 : int
    numer2 : int