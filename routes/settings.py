from fastapi import APIRouter
from fastapi import Body
import httpx

router = APIRouter(
    prefix="/settings"
)

SPRING_URL = "https://backend-project-o0lt.onrender.com"

@router.get("")
async def get_settings():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{SPRING_URL}/settings"
        )

        return response.json()

@router.post("")
async def create_setting(
    data: dict = Body(...)
):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{SPRING_URL}/settings",
            json=data
        )

        return response.json()

@router.put("/{id}")
async def update_setting(
    id: int,
    data: dict = Body(...)
):

    async with httpx.AsyncClient() as client:

        response = await client.put(
            f"{SPRING_URL}/settings/{id}",
            json=data
        )

        return response.json()

@router.delete("/{id}")
async def delete_setting(
    id: int
):

    async with httpx.AsyncClient() as client:

        response = await client.delete(
            f"{SPRING_URL}/settings/{id}"
        )

        return {
            "message": "Deleted"
        }