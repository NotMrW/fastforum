from pydantic import BaseModel # type: ignore

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    auth_level: str
    hashpass: str

    class Config:
        from_attributes: True

class UserLogin(BaseModel):
    email: str
    plainpass: str

class UserOut(UserBase):
    pass