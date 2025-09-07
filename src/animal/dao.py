from src.dao.base import BaseDAO
from src.animal.models import Animal

class AnimalDAO(BaseDAO):
    model = Animal