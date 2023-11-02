import requests
from pydantic import BaseModel

url: str = "https://pokeapi.co/api/v2/pokemon/pikachu"

response: requests.Response = requests.get(url)
response_as_dict: dict = response.json()

# fields: list[str] = ["id", "name", "weight"]

# result = {}

# for key, value in response_as_dict.items(): #     if key in fields:
#         result[key] = value


class Pokemon(BaseModel):
    id: int
    name: str
    weight: int

    @property
    def new_pokemon(self) -> bool:
        if self.id > 20:
            return True
        return False


pokemon = Pokemon(
    id=response_as_dict["id"],
    name=response_as_dict["name"],
    weight=response_as_dict["weight"],
)

print(pokemon)
