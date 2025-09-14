from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
from typing import List, Optional


# --- Models for User ---
class UserBase(BaseModel):
    full_name: str = Field(min_length=3)
    email: EmailStr

    @field_validator('full_name')
    @classmethod
    def name_must_contain_space(cls,v:str)-> str:
        if ' ' not in v:
            raise ValueError("User name must contain a space")
        return v.title()
    
class UserCreate(UserBase):
    pass
class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(default=None, min_length=3)
    email: Optional[EmailStr] = None
    active: Optional[bool] = None

    @field_validator('full_name')
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if v and ' ' not in v:
            raise ValueError("User name must contain a space")
        return v.title() if v else v
class UserResponse(UserBase):
    id: int
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# --- Models for Role ---        
class RoleBase(BaseModel):
    name: str = Field(min_length=3)
    description: Optional[str] = None

class RoleCreate(RoleBase):
    service_id: int
class RoleUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3)
    description: Optional[str] = None
    service_id: Optional[int] = None
class RoleResponse(RoleBase):
    id: int
    service_id: int

    class Config:
        from_attributes = True 

# --- Models for Service ---
class ServiceBase(BaseModel):
    name: str = Field(min_length=3)
    description: Optional[str] = None

class ServiceCreate(ServiceBase):
    pass
class ServiceUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3)
    description: Optional[str] = None
class ServiceResponse(ServiceBase):
    id: int
    roles: List[RoleResponse] = []

    class Config:
        from_attributes = True

# --- Models Access ---
class AccessCreate(BaseModel):
    user_id: int
    service_id: int
    role_id: int
    active: bool
class AccessUpdate(BaseModel):
    user_id: Optional[int] = None
    service_id: Optional[int] = None
    role_id: Optional[int] = None
    active : Optional[bool] = None
class AccessResponse(BaseModel):
    id: int
    created_at: datetime
    user: UserResponse
    service: ServiceResponse
    role: RoleResponse

    class Config:
        from_attributes = True