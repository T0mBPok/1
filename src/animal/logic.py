from sqlalchemy import exists, select
from src.animal.dao import AnimalDAO
from src.database import with_session
from fastapi import HTTPException, status

class AnimalLogic(AnimalDAO):
    @classmethod
    @with_session
    async def update_animal(cls, session, id:int, **values):
        temp = select(exists().where(cls.model.id == id))
        animal_exists = await session.scalar(temp)
        if not animal_exists:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = 'Такого животного не существует')
        if not values:
            raise ValueError('Нет полей для обновления')
        
        return cls.update(id, **values)
            