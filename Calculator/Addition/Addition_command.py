from pydantic import BaseModel 
class Addition_command(BaseModel):
    numer1: int
    numer2: int
