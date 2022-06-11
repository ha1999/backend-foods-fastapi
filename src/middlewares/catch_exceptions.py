from starlette.requests import Request
from fastapi.responses import JSONResponse


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as _:
        content = {
            "message": "Internal Server Error",
            "status_code": 500,
            "reason": str(_)
        }
        return JSONResponse(status_code=500, content=content)
