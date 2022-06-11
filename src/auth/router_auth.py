from fastapi import APIRouter, HTTPException
from src.auth.response_model import Token
from src.auth.model_auth import DataAuthLocal

router_auth = APIRouter()


@router_auth.post("/login-local", response_model=Token)
def loginLocal(auth_data: DataAuthLocal):
    try:
        return {
            # "access_token": "11111111.22222222222.33333333",
            "refresh_token": "44444444.55555555555555.66666666666",
            "info": {
                "email": "leha220699@gmail.com",
                "username": auth_data.username,
                "role": "admin"
            }
        }
    except Exception as _:
        raise HTTPException(status_code=500, detail="Server internal error!")


@router_auth.post("/login-google", response_model=Token)
def loginGoogle():
    pass


@router_auth.post("/login-facebook", response_model=Token)
def loginFaceBook():
    pass


@router_auth.post("/login-zalo", response_model=Token)
def loginZalo():
    pass


@router_auth.post("/login-twitter", response_model=Token)
def loginTwitter():
    pass


@router_auth.post("/login-github", response_model=Token)
def loginGithub():
    pass


@router_auth.post("/logout")
def logout():
    return {
        "logout": "ok"
    }
