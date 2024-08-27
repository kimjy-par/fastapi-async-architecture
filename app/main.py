import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.container import Container
from app.routers.routers import router

app = FastAPI(
    title="mnc_onboarding"
)

if "config.app.cors.allow_origin":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]        
    )

contianer = Container()
app.include_router(router)


@app.get("/")
async def check_server_health():
    return {"health": True}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)