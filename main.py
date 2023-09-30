from fastapi import FastAPI, Depends, HTTPException, status
from typing import Any

from apiTools import fake_db # simular chamada demorada ao db,Ex: uso do async
from data import cursos

app = FastAPI()

@app.get('/cursos', status_code=status.HTTP_200_OK)
async def get(db: Any = Depends(fake_db)):
    try:
        return cursos
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Cursos não encontrados'
    )

@app.get('/cursos/{id}', status_code=status.HTTP_200_OK)
async def get_curso_by_id(id: int):
    # return cursos[id]
    try:
        return cursos[id]
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Curso não encontrado'
    )

@app.post('/curso-post', status_code=status.HTTP_201_CREATED)
async def post_curso(titulo: str, aulas: int, horas: int):
      try:
        next_id: int = len(cursos) + 1
        cursos[next_id] = {
            'titulo': titulo,
            'aulas': aulas,
            'horas': horas,
            }
        return cursos
      except:
          raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail='Curso não encontrado'
    )          

@app.put('/curso-update/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_curso(titulo: str, aulas: str, horas: str, id: int):
    try:
        if id in cursos:
            cursos[id] = {
                'titulo': titulo,
                'aulas': aulas,
                'horas': horas,
                }
            return cursos
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Curso não encontrado com o id:{id}'
    )
    
@app.delete('/curso-delete/{id}', status_code=status.HTTP_200_OK)
async def delete_curso(id: int):
    try:
        del cursos[id]

        # Desafio!!
        # atualizar indices/keys do objeto/dict cursos
        
        return cursos
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Curso não encontrado com o id:{id}'
    )
    