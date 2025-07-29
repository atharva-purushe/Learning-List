from pydantic import BaseModel, Field
from typing import Optional

class Policyholder(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class Policy(BaseModel):
    id: int
    policyholder_id: int
    policy_type: str
    amount: float
    status: str  # "active" or "inactive"

class Claim(BaseModel):
    id: int
    policy_id: int
    claim_amount: float
    status: str  # "open", "closed", "rejected"
    description: Optional[str] = None
