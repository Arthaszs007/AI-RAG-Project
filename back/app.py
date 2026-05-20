from fastapi import FastAPI
from api.register import api_v1_router

app = FastAPI(title="AI_RAG_BACKEDN")


# register main api router
app.include_router(api_v1_router, prefix="/api")
