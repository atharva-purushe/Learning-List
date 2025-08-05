from fastapi import APIRouter
from app import crud
from app.schemas import ClaimCreate, Claim

router = APIRouter(prefix="/claims", tags=["Claims"])

@router.post("/", response_model=Claim)
def create_claim(claim: ClaimCreate):
    return crud.create_claim(claim)

@router.get("/{claim_id}", response_model=Claim)
def get_claim(claim_id: int):
    return crud.get_claim(claim_id)

@router.get("/", response_model=list[Claim])
def get_all_claims():
    return crud.get_all_claims()

@router.put("/{claim_id}", response_model=Claim)
def update_claim(claim_id: int, claim: ClaimCreate):
    return crud.update_claim(claim_id, claim)

@router.delete("/{claim_id}")
def delete_claim(claim_id: int):
    return crud.delete_claim(claim_id)