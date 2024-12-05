from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    print(request.json())
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)