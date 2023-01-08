from fastapi import FastAPI
from enum import Enum

app = FastAPI()  # create an instance of FastAPI


class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italina = "italian"


food_items = {
    'indian': ['Samosa', 'Dosa'],
    'american': ['Hot Dog', "Burger"],
    "italian": ['Pasta', 'Pizza']
}

valid_cuisines = food_items.keys()


@app.get('/hello/{name}')
async def hello(name):
    return f'hello {name}'


@app.get('/cuisines/{cuisine}')
async def get_cuisines(cuisine: AvailableCuisines):
    return food_items.get(cuisine)
