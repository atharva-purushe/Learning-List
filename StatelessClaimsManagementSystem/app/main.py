from fastapi import FastAPI
from app import models, crud
from app.models import Policyholder, Policy, Claim

app = FastAPI()

# -------- POLICYHOLDER ROUTES --------

@app.post("/policyholders/")
def create_policyholder(policyholder: Policyholder):
    return crud.create_policyholder(policyholder)

@app.get("/policyholders/{policyholder_id}")
def get_policyholder(policyholder_id: int):
    return crud.get_policyholder(policyholder_id)

@app.get("/policyholders/")
def get_all_policyholders():
    return crud.get_all_policyholders()

# -------- POLICY ROUTES --------

@app.post("/policies/")
def create_policy(policy: Policy):
    return crud.create_policy(policy)

@app.get("/policies/{policy_id}")
def get_policy(policy_id: int):
    return crud.get_policy(policy_id)

@app.get("/policies/")
def get_all_policies():
    return crud.get_all_policies()

# -------- CLAIM ROUTES --------

@app.post("/claims/")
def create_claim(claim: Claim):
    return crud.create_claim(claim)

@app.get("/claims/{claim_id}")
def get_claim(claim_id: int):
    return crud.get_claim(claim_id)

@app.get("/claims/")
def get_all_claims():
    return crud.get_all_claims()
