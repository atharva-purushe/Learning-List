from passlib.context import CryptContext    
passwrd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return passwrd_context.hash(password)
def verify_password(plain_password, hashed_password): 
    return passwrd_context.verify(plain_password, hashed_password)

users = {
    "atharva":{
        "username": "atharva",
        "full_name": "Atharva Purushe",
        "hashed_password": hash_password("atharva123"),
    }
}
def get_user(username: str):
    return users.get(username)