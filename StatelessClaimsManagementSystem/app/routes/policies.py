from fastapi import APIRouter
from app import crud
from app.schemas import PolicyCreate, Policy

router = APIRouter(prefix="/policies", tags=["Policies"])

@router.post("/", response_model=Policy)
def create_policy(policy: PolicyCreate):
    return crud.create_policy(policy)

@router.get("/{policy_id}", response_model=Policy)
def get_policy(policy_id: int):
    return crud.get_policy(policy_id)

@router.get("/", response_model=list[Policy])
def get_all_policies():
    return crud.get_all_policies()

@router.put("/{policy_id}", response_model=Policy)
def update_policy(policy_id: int, policy: PolicyCreate):
    return crud.update_policy(policy_id, policy)

@router.delete("/{policy_id}")
def delete_policy(policy_id: int):
    return crud.delete_policy(policy_id)
