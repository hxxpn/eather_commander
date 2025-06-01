from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def read_root():
    print("Health check started.")
    return {"message": "Hello, World!"}