from starlette.requests import Request
from fastapi.responses import JSONResponse
from src.config.settings import settings


async def catch_header_middleware(request: Request, call_next):
    error_header = False
    req_header = request.headers
    user_agent = req_header.get("user-agent", "")
    if "Mozilla" not in user_agent:
        error_header = True
        # content = {
        #     "message": "Permission denied",
        #     "status_code": 401
        # }
        # return JSONResponse(status_code=401, content=content)

    referer = req_header.get("referer", "none")
    if referer not in settings.BACKEND_CORS_ORIGINS:
        error_header = True
    time_request = req_header.get("trq")
    text_origin = req_header.get("to")
    text_decode = req_header.get("tdc")
    secret_key = req_header.get("sck")
    print(user_agent, "================================")
    return await call_next(request)
