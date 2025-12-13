from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is up and running."}

@app.get("/generate-2fa")
def generate_2fa():
    return {"2fa_code": "123456"}  # placeholder
