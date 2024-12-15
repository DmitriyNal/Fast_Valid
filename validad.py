from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница "}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "ВЫ вошли как администратор"}


@app.get("/user/{user_id}")
async def user(user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100)]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get('/user/{username}/{age}')
async def user_name(username: Annotated[str, Path(min_length=5, max_length=20)],
                    age: Annotated[int, Path(ge=18, le=120)]) -> dict:
    return {"message": f'Имя: {username}, Возраст: {age} '}
