from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from apiTools import *

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get("/covid", response_class=HTMLResponse)
def read_root(request: Request): 
    url = 'https://covid19-brazil-api.vercel.app/api/report/v1'
    dados_covid = get_data_url(url)

    return templates.TemplateResponse(
        'covid.html',
        {"request": request, 'dados_covid': dados_covid }
    )

@app.get("/covid/desc", response_class=HTMLResponse)
def read_desc(request: Request):
    url = 'https://covid19-brazil-api.vercel.app/api/report/v1'
    dados_covid = get_data_url(url)
    organized_desc = organize_case_list(dados_covid)

    return templates.TemplateResponse(
        'desc.html',
        {"request": request, 'organized_desc': organized_desc }
    )

@app.get("/covid/cresc", response_class=HTMLResponse)
def read_cresc(request: Request):
    url = 'https://covid19-brazil-api.vercel.app/api/report/v1'
    dados_covid = get_data_url(url)
    organized_cresc = organize_case_list_reverse(dados_covid)

    return templates.TemplateResponse(
        'cresc.html',
        {"request": request, 'organized_cresc': organized_cresc }
    )