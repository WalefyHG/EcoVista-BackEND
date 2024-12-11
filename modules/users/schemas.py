from enum import Enum
from typing import Optional
from ninja import Schema, UploadedFile
from datetime import datetime


class RoleFilterEnum(str, Enum):
    admin = "admin"
    user = "user"

class UserPostSchema(Schema):
    username: str
    email: str
    password: str
    role: RoleFilterEnum
    
class UserPutSchema(Schema):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[RoleFilterEnum] = None
    profile_picture: Optional[UploadedFile] = None
    
class UserListSchema(Schema):
    id: int
    username: str
    email: str
    role: str
    profile_picture: Optional[str] = None
    date_joined: datetime
    last_login: datetime
    is_active: bool
    
    
class ErrorResponse(Schema):
    message: str