from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type != operation_type)
        result = await session.execute(query)
        return {
            "status": "succses",
            "data": [dict(data._mapping) for data in result],
            "details": None
        }
    except:
        return {
            "status": "error",
            "data": None,
            "details": None
        }


@router.post("/")
async def add_spec_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(operation).values(**new_operation.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "succses",
            "data": None,
            "details": None
        }
    except:
        return {
            "status": "error",
            "data": None,
            "details": None
        }
