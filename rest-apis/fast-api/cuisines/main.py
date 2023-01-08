from fastapi import FastAPI

app = FastAPI()  # create an instance of FastAPI


@app.get('/hello/{name}')
async def hello(name):
    return f'hello {name}'
