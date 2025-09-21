from src.database import with_session
from sqlalchemy import exists, select, delete, update
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status


class BaseDAO:
    model = None

    @classmethod
    @with_session
    async def get(cls, session, **filter_by):
        data = await session.execute(select(cls.model).filter_by(**filter_by))
        return data.scalars().all()
            
    @classmethod
    @with_session
    async def add(cls, session, **values):
        new_obj = cls.model(**values)
        session.add(new_obj)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
        return new_obj
            
    @classmethod
    @with_session
    async def delete(cls, session, id: int):
        check = await session.execute(delete(cls.model).where(cls.model.id == id))
        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return check.rowcount
    
    @classmethod
    @with_session
    async def update(cls, session, id:int, **values):
        result = await session.execute(update(cls.model).where(cls.model.id == id).values(**values))
        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return result.rowcount