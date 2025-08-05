from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# -------- INPUT SCHEMAS --------

class PolicyholderCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class PolicyCreate(BaseModel):
    policyholder_id: int
    policy_type: str
    amount: float
    status: str

class ClaimCreate(BaseModel):
    policy_id: int
    claim_amount: float
    status: str
    description: Optional[str] = None

# -------- OUTPUT SCHEMAS --------

class Policyholder(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True

class Policy(BaseModel):
    id: int
    policyholder_id: int
    policy_type: str
    amount: float
    status: str

    class Config:
        orm_mode = True

class Claim(BaseModel):
    id: int
    policy_id: int
    claim_amount: float
    status: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
