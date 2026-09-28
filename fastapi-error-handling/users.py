from fastapi import APIRouter

from app.schemas.user import UserResponse
from app.services.user_service import get_user_by_id

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return get_user_by_id(user_id)
