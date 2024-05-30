from fastapi import APIRouter, HTTPException
from app.db_management import expenditure_CRUD
from app.models.expenditure import Expenditure

expenditure_router = APIRouter()


@expenditure_router.get('/all')
async def get_all_expenses():
    return await expenditure_CRUD.get_all_expenses()


@expenditure_router.get('/get_expenditure', )
async def sign_in(name: str):
    try:
        return await expenditure_CRUD.get_expenditure(name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@expenditure_router.post('/add_expenditure')
async def sign_up(expenditure: Expenditure):
    try:
        return await expenditure_CRUD.add_expenditure(expenditure)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@expenditure_router.put('/update_expenditure')
async def update_expenditure(name: str, updated_expenditure: Expenditure):
    try:
        await expenditure_CRUD.update_expenditure(name, updated_expenditure)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@expenditure_router.delete('/delete_expenditure')
async def delete(name: str):
    try:
        return await expenditure_CRUD.delete_expenditure(name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
