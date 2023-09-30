import urllib.request, json

def get_data_url(url):
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    json_data = json.loads(dados)

    return json_data