import asyncio
from InquirerPy import prompt
import asyncclick as click
from src.animal.logic import AnimalLogic


@click.group()
async def cli():
    pass

async def select_animal():
    animals = await AnimalLogic.get()
    choices = [f"{a.id}: {a.kind} {a.name} {a.age}" for a in animals]

    loop = asyncio.get_running_loop()
    answers = await loop.run_in_executor(
        None,
        lambda: prompt([
            {
                "type": "list",
                "name": "animal_choice",
                "message": "Выберите животное:",
                "choices": choices,
                "pointer": ">",
                "cycle": True,
            }
        ])
    )
    selected_id = int(answers["animal_choice"].split(":")[0])
    return selected_id

@cli.command()
async def list_animals():
    animals = await AnimalLogic.get()
    for a in animals:
        click.echo(f"{a.id}: {a.kind} - {a.name} - {a.age}")
        
@cli.command()
async def add_animal():
    kind = click.prompt('Kind')
    name = click.prompt('Name')
    age = click.prompt('Age', type=int)
    await AnimalLogic.add(kind=kind, name=name, age=age)
    click.echo("Animal added.")
    
@cli.command()
async def edit_animal():
    animal_id = await select_animal()
    animal_list = await AnimalLogic.get(id=animal_id)
    if not animal_list:
        click.echo("Животное не найдено")
        return
    animal = animal_list[0]
    kind = click.prompt('Kind', default=animal.kind)
    name = click.prompt('Name', default=animal.name)
    age = click.prompt('Age', type=int, default=animal.age)
    await AnimalLogic.update_animal(id=animal_id, kind=kind, name=name, age=age)
    click.echo("Животное обновлено.")
    
@cli.command()
async def delete_animal():
    animal_id = await select_animal()
    await AnimalLogic.delete(id=animal_id)
    click.echo("Животное удалено.")

if __name__ == '__main__':
    cli()