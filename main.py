from typing import Annotated, Optional
from fastapi import FastAPI, Header, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from crud import get_items, post_items, put_item, delete_item, update_item

import starlette.status as status
import uvicorn


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=["*"]
)

class Item(BaseModel):
    data: dict

@app.get('/')
def base():
    return HTMLResponse(status_code=status.HTTP_200_OK, content = 'Initial page!')

@app.get('/get')
def get(response: Response):
    content = get_items()
    if content == None:
        response = HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content = 'Can\'t get items!')
    response = JSONResponse(status_code=status.HTTP_200_OK, content = content)
    return response

@app.post('/post')
def post(item: Item):
    post_items(item.data)
    return JSONResponse(status_code=status.HTTP_200_OK, content = get_items())

@app.put('/put/{item_id}{item_value}')
def put(item_id: str, item_value: str):
    put_item(item_id, int(item_value))
    return Response(status_code=status.HTTP_200_OK, content='Item successfuly added!')

@app.patch('/put/{item_id}{item_value}')
def patch(item_id: str, item_value: str):
    update_item(item_id, int(item_value))
    return Response(status_code=status.HTTP_200_OK, content='Item successfuly updated!')

@app.delete('/delete/{item_id}')
def delete(item_id:str):
    try:
        delete_item(item_id)
        return Response(status_code=status.HTTP_200_OK, content='Item successfuly deleted!')
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content='No such item found!')

@app.get('/headers')
def get_headers(request: Request):
    content = {}

    for header in request.headers.raw:
        content[header[0].decode()] = header[1].decode()

    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

@app.get('/origin')
def get_headers(host: Annotated[str | None, Header()] = None):
    content = { "Host" : host }
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

@app.get('/agent')
def get_user_agent( user_agent: Annotated[str | None, Header()] = None):
    content = {"User-Agent": user_agent}
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)










if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)