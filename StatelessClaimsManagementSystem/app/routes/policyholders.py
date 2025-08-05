from app.schemas import PolicyholderCreate, Policyholder
from fastapi import APIRouter
from app import crud

router = APIRouter(prefix="/policyholders", tags=["Policyholders"])

# -------- CREATE --------
@router.post("/", response_model=Policyholder)
def create_policyholder(policyholder: PolicyholderCreate):
    return crud.create_policyholder(policyholder)

# -------- READ ONE --------
@router.get("/{policyholder_id}", response_model=Policyholder)
def get_policyholder(policyholder_id: int):
    return crud.get_policyholder(policyholder_id)

# -------- READ ALL --------
@router.get("/", response_model=list[Policyholder])
def get_all_policyholders():
    return crud.get_all_policyholders()

# -------- UPDATE --------
@router.put("/{policyholder_id}", response_model=Policyholder)
def update_policyholder(policyholder_id: int, updated_data: PolicyholderCreate):
    return crud.update_policyholder(policyholder_id, updated_data)

# -------- DELETE --------
@router.delete("/{policyholder_id}")
def delete_policyholder(policyholder_id: int):
    return crud.delete_policyholder(policyholder_id)

