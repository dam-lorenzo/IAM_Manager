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

class UserResponse(UserBase):
    id: int
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# # --- Models for Role ---        
# class RoleBase(BaseModel):
#     name: str = Field(min_length=3)
#     description: Optional[str] = None

# class RoleCreate(RoleBase):
#     service_id: int

# class RoleResponse(RoleBase):
#     id: int
#     service_id: int

#     class Config:
#         from_attributes = True 

# # --- Models for Service ---
# class ServiceBase(BaseModel):
#     name: str = Field(min_length=3)
#     description: Optional[str] = None

# class ServiceCreate(ServiceBase):
#     pass

# class ServiceResponse(ServiceBase):
#     id: int
#     roles: List[RoleResponse] = [] # Anidamos la respuesta de los roles

#     class Config:
#         from_attributes = True


# # --- Modelos para Access ---
# class AccessCreate(BaseModel):
#     user_id: int
#     service_id: int
#     role_id: int

# class AccessResponse(BaseModel):
#     id: int
#     created_at: datetime
#     user: UserResponse
#     service: ServiceResponse
#     role: RoleResponse

#     class Config:
#         from_attributes = True