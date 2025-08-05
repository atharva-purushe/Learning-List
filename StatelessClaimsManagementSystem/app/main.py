from fastapi import FastAPI
from app.routes import policyholders, policies, claims

app = FastAPI()

app.include_router(policyholders.router)
app.include_router(policies.router)
app.include_router(claims.router)
