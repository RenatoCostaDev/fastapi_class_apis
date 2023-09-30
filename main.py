from fastapi import FastAPI, Depends, HTTPException, status

from apiTools import *
from data import lista_clientes

app = FastAPI()

@app.get('/clientes', status_code=status.HTTP_200_OK)
async def get():
    try:
        return get_formatted_data_basic(lista_clientes)
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Clientes não encontrados'
    )

@app.get('/cliente/{id}', status_code=status.HTTP_200_OK)
async def get_client_by_id(id: int):
    # return cursos[id]
    try:
        return get_formatted_data(lista_clientes, id)
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Cliente não encontrado'
    )

@app.get('/cliente-last-measure/{id}', status_code=status.HTTP_200_OK)
async def get_last_measure(id: int):
    # return cursos[id]
    try:
        return get_client_last_measure(lista_clientes, id)
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Cliente não encontrado'
    )

@app.post('/cliente-post', status_code=status.HTTP_201_CREATED)
async def post_client(nome: str, peso: float, altura: float, data: str):
      try:
        create_new_client(nome, peso, altura, data, lista_clientes)
        return lista_clientes
      except:
          raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail='Cliente não criado'
    )          

@app.put('/cliente-update/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_client(id: int, peso: float, data: str):
    try:
        return update_dict_avaliacao(id, peso, data, lista_clientes)         
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Cliente com o id:{id} não encontrado'
    )
    

@app.delete('/cliente-delete/{id}', status_code=status.HTTP_200_OK)
async def delete_client(id: int):
    try:        
        return delete_client_by_id(id, lista_clientes)
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Curso não encontrado com o id:{id}'
    )
    