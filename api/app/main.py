from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World reload 2"}


@app.get("/test")
def read_test():
    return {"test": "Ceci est un test"}