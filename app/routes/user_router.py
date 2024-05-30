from fastapi import APIRouter, HTTPException
from app.db_management import user_CRUD
from app.models.user import User

user_router = APIRouter()


@user_router.get('/all')
async def get_all_users():
    return await user_CRUD.get_all_users()


@user_router.get('/sign_in', )
async def sign_in(name: str, password: str):
    try:
        return await user_CRUD.get_user(name, password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.post('/sign_up')
async def sign_up(user: User):
    try:
        return await user_CRUD.add_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.put('/update_user')
async def update_user(name: str, password: str, updated_user: User):
    try:
        await user_CRUD.update_user(name, password, updated_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
