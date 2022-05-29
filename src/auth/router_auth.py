from fastapi import APIRouter

router_auth = APIRouter()


@router_auth.post("/login-local")
def loginLocal():
    pass


@router_auth.post("/login-google")
def loginGoogle():
    pass


@router_auth.post("/login-facebook")
def loginFaceBook():
    pass


@router_auth.post("/login-zalo")
def loginZalo():
    pass


@router_auth.post("/login-twitter")
def loginTwitter():
    pass


@router_auth.post("/login-github")
def loginGithub():
    pass


@router_auth.post("/logout")
def logout():
    pass
