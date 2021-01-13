"""
    usage:
    1. pip install -r requirements.txt
    2. python3 -m uvicorn task2_simple_user_app:app --reload     to start server
"""

import uuid
from typing import Optional
import hashlib

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

from task1_gen_username import pseudo_encrypt


"""
    store registered users
    key is {username} gen by pseudo_encrypt
    value is encrypted password
"""
registerd_users = {}
login_users = {} # key is token, value is username


def encrypt_password(password):
    h = hashlib.sha256()
    h.update(bytes(password, encoding='utf-8'))
    return h.hexdigest()


class User(BaseModel):
    username: Optional[str] = None
    password: str

app = FastAPI()

@app.get("/")
def home(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="unauthorized.")
    if len(authorization.split(' ')) != 2:
        raise HTTPException(status_code=401, detail="unauthorized.")
    token = authorization.split(' ')[1]
    username = login_users.get(token)
    if not username:
        raise HTTPException(status_code=401, detail="login first.")

    return {'message': f'welcome home {username}'}


user_count = 0
@app.post("/accounts/register")
def register(user: User):
    global user_count
    if not user.password:
        raise HTTPException(status_code=400, detail="password required.")

    username = pseudo_encrypt(user_count)
    user_count += 1
    registerd_users[username] = encrypt_password(user.password)
    return {'username': username}


@app.post("/accounts/login")
def login(user: User):
    if not user.username:
        raise HTTPException(status_code=400, detail="username required.")
    if not user.password:
        raise HTTPException(status_code=400, detail="password required.")
    
    password_db = registerd_users.get(int(user.username))
    if not password_db:
        raise HTTPException(status_code=404, detail="user not found.")

    if password_db != encrypt_password(user.password):
        raise HTTPException(status_code=400, detail="password invalid.")

    token = uuid.uuid4()
    login_users[token.hex] = user.username
    return {'token': token.hex}

