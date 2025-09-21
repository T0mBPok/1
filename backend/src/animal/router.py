from fastapi import APIRouter, Depends, Path
from src.animal.schemas import GetAnimal, AddAnimal, UpdateAnimal
from src.animal.rb import RBAnimal
from src.animal.logic import AnimalLogic

router = APIRouter(prefix='/animal', tags = ["Работа с животными"])

@router.get('/', summary='Получить данные о животных', response_model=list[GetAnimal])
async def get_animal(request_body: RBAnimal = Depends()):
    return await AnimalLogic.get(**request_body.to_dict())

@router.post('/', summary='Добавить животное', response_model = AddAnimal)
async def add_animal(form_data: AddAnimal = Depends(AddAnimal.as_form)):
    return await AnimalLogic.add(**form_data.model_dump())

@router.delete('/{id}', summary='Удалить животное')
async def delete_animal(id: int = Path(..., gt=0)):
    await AnimalLogic.delete(id=id)
    return {'message': f'Данные о животном с id={id} успешно удалены!'}

@router.put('/{id}', summary = 'Обновить данные о животном', response_model = UpdateAnimal)
async def update_animal(animal: UpdateAnimal, id: int = Path(..., gt=0)):
    new_info = animal.model_dump(exclude_unset=True)
    await AnimalLogic.update_animal(id=id, **new_info)
    return new_info