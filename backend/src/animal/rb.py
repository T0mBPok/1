class RBAnimal:
    def __init__(self, id: int | None = None,
                kind: str | None = None,
                name: str | None = None,
                age: int | None = None):
        self.id = id
        self.kind = kind
        self.name = name
        self.age = age
        
    def to_dict(self) -> dict:
        data = {"id": self.id, "kind": self.kind, "name": self.name, "age": self.age}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data