from fastapi import FastAPI
from src.auth.router_auth import router_auth
from src.postgresql.init_db import database, create_all_table


app = FastAPI()


@app.on_event("startup")
async def startup():
    try:
        print("Connecting to DB...!")
        await database.connect()
        print("Connected to DB!")
        create_all_table()
    except Exception as ex:
        print(f"Error cannot connect to DB: {str(ex)}")


@app.on_event("shutdown")
async def shutdown():
    try:
        print("Disconnecting to DB...!")
        await database.disconnect()
        print("Disconnected to DB!")
    except Exception as ex:
        print(f"Error cannot disconnect to DB: {str(ex)}")


@app.get("/")
async def root():
    return {
        "message": "Hi, This is my API if you want to use it please contact me at leha220699@gmail.com!",
        "version": "1.0.0",
        "created_at": "05-29-2022",
        "created_by": "haln-uet",
        "language_used": "python_fastapi"
    }


app.include_router(router_auth)
