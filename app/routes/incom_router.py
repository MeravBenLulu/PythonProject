from fastapi import APIRouter, HTTPException
from app.db_management import income_CRUD
from app.models.income import Income

income_router = APIRouter()


@income_router.get('/all')
async def get_all_incomes():
    return await income_CRUD.get_all_incomes()


@income_router.get('/get_income', )
async def get_income(name: str):
    try:
        return await income_CRUD.get_income(name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@income_router.post('/add_income')
async def add_income(income: Income):
    try:
        return await income_CRUD.add_income(income)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@income_router.put('/update_income')
async def update_income(name: str, updated_income: Income):
    try:
        await income_CRUD.update_income(name, updated_income)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@income_router.delete('/delete_income', )
async def delete(name: str):
    try:
        return await income_CRUD.delete_income(name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))