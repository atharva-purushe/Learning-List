from fastapi import HTTPException
from app.models import Policyholder, Policy, Claim
from app.schemas import PolicyholderCreate, PolicyCreate, ClaimCreate
from app.database import (
    policyholders,
    policies,
    claims,
    policyholder_id_counter,
    policy_id_counter,
    claim_id_counter,
)

# ----------------- CREATE FUNCTIONS -----------------

def create_policyholder(policyholder_data: PolicyholderCreate) -> Policyholder:
    global policyholder_id_counter
    new_id = policyholder_id_counter
    policyholder_id_counter += 1

    full_policyholder = Policyholder(id=new_id, **policyholder_data.dict())
    policyholders[new_id] = full_policyholder
    return full_policyholder


def create_policy(policy_data: PolicyCreate) -> Policy:
    global policy_id_counter

    if policy_data.policyholder_id not in policyholders:
        raise HTTPException(status_code=400, detail="Invalid policyholder ID.")

    new_id = policy_id_counter
    policy_id_counter += 1

    full_policy = Policy(id=new_id, **policy_data.dict())
    policies[new_id] = full_policy
    return full_policy


def create_claim(claim_data: ClaimCreate) -> Claim:
    global claim_id_counter

    if claim_data.policy_id not in policies:
        raise HTTPException(status_code=400, detail="Invalid policy ID.")

    if claim_data.claim_amount > policies[claim_data.policy_id].amount:
        raise HTTPException(status_code=400, detail="Claim amount exceeds policy sum assured.")

    new_id = claim_id_counter
    claim_id_counter += 1

    full_claim = Claim(id=new_id, **claim_data.dict())
    claims[new_id] = full_claim
    return full_claim

# ----------------- READ FUNCTIONS -----------------

def get_policyholder(policyholder_id: int) -> Policyholder:
    if policyholder_id not in policyholders:
        raise HTTPException(status_code=404, detail="Policyholder not found.")
    return policyholders[policyholder_id]

def get_all_policyholders() -> list[Policyholder]:
    return list(policyholders.values())

def get_policy(policy_id: int) -> Policy:
    if policy_id not in policies:
        raise HTTPException(status_code=404, detail="Policy not found.")
    return policies[policy_id]

def get_all_policies() -> list[Policy]:
    return list(policies.values())

def get_claim(claim_id: int) -> Claim:
    if claim_id not in claims:
        raise HTTPException(status_code=404, detail="Claim not found.")
    return claims[claim_id]

def get_all_claims() -> list[Claim]:
    return list(claims.values())

# ----------------- UPDATE FUNCTIONS -----------------

def update_policyholder(policyholder_id: int, updated_data: PolicyholderCreate) -> Policyholder:
    if policyholder_id not in policyholders:
        raise HTTPException(status_code=404, detail="Policyholder not found.")

    updated = Policyholder(id=policyholder_id, **updated_data.dict())
    policyholders[policyholder_id] = updated
    return updated

def update_policy(policy_id: int, updated_data: PolicyCreate) -> Policy:
    if policy_id not in policies:
        raise HTTPException(status_code=404, detail="Policy not found.")

    if updated_data.policyholder_id != policies[policy_id].policyholder_id:
        raise HTTPException(status_code=400, detail="Policyholder ID cannot be changed.")

    updated = Policy(id=policy_id, **updated_data.dict())
    policies[policy_id] = updated
    return updated

def update_claim(claim_id: int, updated_data: ClaimCreate) -> Claim:
    if claim_id not in claims:
        raise HTTPException(status_code=404, detail="Claim not found.")

    if updated_data.policy_id not in policies:
        raise HTTPException(status_code=400, detail="Invalid policy ID.")

    if updated_data.claim_amount > policies[updated_data.policy_id].amount:
        raise HTTPException(status_code=400, detail="Claim amount exceeds policy sum assured.")

    updated = Claim(id=claim_id, **updated_data.dict())
    claims[claim_id] = updated
    return updated

# ----------------- DELETE FUNCTIONS -----------------

def delete_policyholder(policyholder_id: int):
    if policyholder_id not in policyholders:
        raise HTTPException(status_code=404, detail="Policyholder not found.")

    # Check if policyholder has any policies
    for policy in policies.values():
        if policy.policyholder_id == policyholder_id:
            raise HTTPException(status_code=400, detail="Cannot delete policyholder with active policies.")

    del policyholders[policyholder_id]
    return {"detail": "Policyholder deleted successfully."}

def delete_policy(policy_id: int):
    if policy_id not in policies:
        raise HTTPException(status_code=404, detail="Policy not found.")

    # Check if policy has any claims
    for claim in claims.values():
        if claim.policy_id == policy_id:
            raise HTTPException(status_code=400, detail="Cannot delete policy with associated claims.")

    del policies[policy_id]
    return {"detail": "Policy deleted successfully."}

def delete_claim(claim_id: int):
    if claim_id not in claims:
        raise HTTPException(status_code=404, detail="Claim not found.")

    del claims[claim_id]
    return {"detail": "Claim deleted successfully."}
