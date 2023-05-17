from typing import List
from fastapi import FastAPI
from models import User, Gender, Role

# Instantiation of FastAPI
app = FastAPI()

# Database => Mock Data
database: List[User] = [
    User(
        first_name= "Emmanuel", 
        last_name="Osinnowo", 
        gender=Gender.male, 
        roles= [
            Role.admin,
            Role.student
        ]
    ),
    User(
        first_name= "Mathew", 
        last_name="Keynes", 
        gender=Gender.female, 
        roles= [
            Role.user,
        ]
    ),
]

@app.get('/')
def root():
    return { 'Hello': 'World'}

@app.get('/api/v1/users')
async def fetchUsers():
    return database