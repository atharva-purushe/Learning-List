from fastapi import HTTPException
from app.models import Policyholder, Policy, Claim
from app.database import (
    policyholders,
    policies,
    claims,
    policyholder_id_counter,
    policy_id_counter,
    claim_id_counter,
)

# ----------------- CREATE FUNCTIONS -----------------

def create_policyholder(policyholder_data: Policyholder):
    global policyholder_id_counter
    new_id = policyholder_id_counter
    policyholders[new_id] = policyholder_data
    policyholder_id_counter += 1
    return {"id": new_id, "data": policyholder_data}


def create_policy(policy_data: Policy):
    global policy_id_counter

    if policy_data.policyholder_id not in policyholders:
        raise HTTPException(status_code=400, detail="Invalid policyholder ID.")

    new_id = policy_id_counter
    policies[new_id] = policy_data
    policy_id_counter += 1
    return {"id": new_id, "data": policy_data}


def create_claim(claim_data: Claim):
    global claim_id_counter

    if claim_data.policy_id not in policies:
        raise HTTPException(status_code=400, detail="Invalid policy ID.")

    if claim_data.claimed_amount > policies[claim_data.policy_id].sum_assured:
        raise HTTPException(status_code=400, detail="Claim amount exceeds policy sum assured.")

    new_id = claim_id_counter
    claims[new_id] = claim_data
    claim_id_counter += 1
    return {"id": new_id, "data": claim_data}

# ----------------- READ FUNCTIONS -----------------

def get_policyholder(policyholder_id: int):
    if policyholder_id not in policyholders:
        raise HTTPException(status_code=404, detail="Policyholder not found.")
    return {"id": policyholder_id, "data": policyholders[policyholder_id]}

def get_all_policyholders():
    return [{"id": pid, "data": data} for pid, data in policyholders.items()]


def get_policy(policy_id: int):
    if policy_id not in policies:
        raise HTTPException(status_code=404, detail="Policy not found.")
    return {"id": policy_id, "data": policies[policy_id]}

def get_all_policies():
    return [{"id": pid, "data": data} for pid, data in policies.items()]


def get_claim(claim_id: int):
    if claim_id not in claims:
        raise HTTPException(status_code=404, detail="Claim not found.")
    return {"id": claim_id, "data": claims[claim_id]}

def get_all_claims():
    return [{"id": cid, "data": data} for cid, data in claims.items()]
