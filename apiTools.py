import urllib.request, json

def get_data_url(url):
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    json_data = json.loads(dados)
    dados_covid = json_data['data']

    return dados_covid

def organize_case_list(case_list):
    sorted_case_list = sorted(case_list, key=lambda x: x['suspects'], reverse=True)
    return sorted_case_list

def organize_case_list_reverse(case_list):
    sorted_case_list = sorted(case_list, key=lambda x: x['suspects'], reverse=False)
    return sorted_case_list