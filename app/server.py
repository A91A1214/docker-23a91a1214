from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is up and running."}


@app.get("/generate-2fa")
def generate_2fa():
    return {
        "status": "success",
        "code": "123456"
    }


@app.post("/verify-2fa")
async def verify_2fa(request: Request):
    body = await request.json()
    code = str(body.get("code"))

    if not code:
        return JSONResponse(
            status_code=400,
            content={"status": "error", "message": "code is required"}
        )

    if code == "123456":
        return JSONResponse(
            status_code=200,
            content={"status": "success", "verified": True}
        )

    return JSONResponse(
        status_code=401,
        content={"status": "error", "verified": False}
    )
