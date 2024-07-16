from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    Message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(BaseModel):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
