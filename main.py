from fastapi import FastAPI, HTTPException, status, Path
from apiTools import *
from data import lista_clientes
app = FastAPI(    
   title='Api Restaurante',
   version='0.0.1',
   description="Api com nomes de clientes e seu prato favorito",
)

@app.get('/clientes',
        status_code=status.HTTP_200_OK,
        description='Retorna todos os clientes ou uma lista vazia.',
        summary='Retorna todos os clientes'
        )
async def get_clientes():
    try:
        return lista_clientes
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Clientes não encontrados'
    )

@app.get('/cliente/{id}', status_code=status.HTTP_200_OK)
async def get_cliente_id(id: int = Path(
    title='ID do curso',
    description=f'Deve ser de 1 a {len(lista_clientes)}',
    gt=1,
    lt=len(lista_clientes) + 1)
    ):
    try:
        resposta = get_by_id(id, lista_clientes)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Cliente não encontrado'
    )

@app.post('/cliente-create', status_code=status.HTTP_201_CREATED)
async def create_cliente(nombre: str, plato_favorito: str):
    try:
        resposta = create_cliente_new(nombre, plato_favorito, lista_clientes)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail='Cliente não criado'
    )   

@app.put('/cliente-update/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_cliente(nombre: str, plato_favorito: str, id: int):
    try:
        resposta = update_cliente_by_id(nombre, plato_favorito, lista_clientes, id)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Cliente com o id:{id} não encontrado'
    )

@app.delete('/cliente-delete/{id}', status_code=status.HTTP_200_OK)
async def delete_cliente(id: int):
    try:        
        resposta = delete_cliente_by_id(lista_clientes, id)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Cliente não encontrado com o id:{id}'
    )