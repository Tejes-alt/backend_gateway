from fastapi import APIRouter
import httpx

router = APIRouter(
    prefix="/analytics"
)

SPRING_URL = "https://backend-project-o0lt.onrender.com"

@router.get("")
async def get_analytics():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{SPRING_URL}/analytics"
        )

        return response.json()