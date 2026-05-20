"""
recieve prompt and question from users,rerturn the answer to users

"""

from fastapi import APIRouter

chat_router = APIRouter()


@chat_router.get("/stream")
async def test():
    return {"msg": "I am chat api"}
