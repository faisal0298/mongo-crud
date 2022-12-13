from pydantic import BaseModel


class createuser(BaseModel):
    fullname : str
    age : int
    phone : int
    address : str
    email :str
    rolename :str


class updateuser(BaseModel):
    name:str
    age : int
    email : str


class createproject(BaseModel):
    email : str
    name : str
    Annotationcount : int