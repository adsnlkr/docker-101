from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="My FastAPI App",
    description="A simple FastAPI app with health check and Swagger UI",
    version="1.0.0"
)

@app.get("/health", tags=["Health"])
async def health_check():
    return JSONResponse(content={"status": "ok"})