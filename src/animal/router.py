from fastapi import APIRouter, Depends, Path
from src.animal.schemas import GetAnimal, AddAnimal, DeleteAnimal, UpdateAnimal
from src.animal.rb import RBAnimal
from src.animal.logic import AnimalLogic

router = APIRouter(prefix='/animal', tags = ["Работа с животными"])

@router.get('/', summary='Получить данные о животных', response_model=list[GetAnimal])
async def get_animal(request_body: RBAnimal = Depends()):
    return await AnimalLogic.get(**request_body.to_dict())

@router.post('/', summary='Добавить животное', response_model = AddAnimal)
async def add_animal(form_data: AddAnimal = Depends(AddAnimal.as_form)):
    return await AnimalLogic.add(**form_data.to_dict())

@router.delete('/{id}', summary='Удалить животное', response_model = DeleteAnimal)
async def delete_animal(id: int = Path(..., gt=0)):
    return await AnimalLogic.delete(id=id)

@router.put('/', summary = 'Обновить данные о животном', response_model = UpdateAnimal)
async def update_animal(animal: UpdateAnimal):
    new_info = animal.to_dict()
    animal_id = new_info.pop('id')
    return await AnimalLogic.update_animal(animal_id, **new_info)