from fastapi import FastAPI

app = FastAPI()  # create an instance of FastAPI


@app.get('/hello')
async def hello():
    return 'hello world'
