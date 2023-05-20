from typing import List

from fastapi import APIRouter, Depends


router = APIRouter()


@router.get("/example")
async def example():
    return {"data": "example"}
