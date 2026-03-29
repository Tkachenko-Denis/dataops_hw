from fastapi import FastAPI


app = FastAPI(title="hw-13-service")


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello from hw_13"}


@app.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
