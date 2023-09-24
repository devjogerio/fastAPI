from fastapi import FastAPI

app = FastAPI()

userName = "Rogério Assunção"


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/users")
async def users_root():
    return {"message": "Hello Users!"}


@app.get("/teste1")
async def test():
    return {"message": f"Hi, {userName}"}
