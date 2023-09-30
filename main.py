from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from apiTools import *

app = FastAPI()
templates = Jinja2Templates(directory='templates')

dados_cep = {}

@app.get('/cep')
async def get_address(request: Request):

    return templates.TemplateResponse(
        'base.html',
        {'request': request, 'dados_cep': dados_cep}
    )

@app.post('/post-cep')
async def post_cep(request: Request, cep: str = Form(...)):    
    url = f'https://viacep.com.br/ws/{cep}/json/'
    dados_cep = get_data_url(url)

    return templates.TemplateResponse(
        'base.html',
        {'request': request, 'dados_cep': dados_cep}
    )