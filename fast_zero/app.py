from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routers import auth, users
from fast_zero.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


"""


@app.get('/users/{id}', response_model=UserList)
def read_user_id(
    user_id: int = Path(
        ..., title='User ID', description='O ID utilizado na busca do user'
    ),
    session: Session = Depends(get_session),
):
    db_user = session.query(User).filter(UserPublic.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


"""
