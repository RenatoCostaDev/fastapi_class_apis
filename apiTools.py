# get todos clientes sem as avaliações (HOF)
map_client = lambda client: {
        'id': client['id'],
        'nome': client['nome'],
    }

def get_formatted_data_basic(lista_clientes: list) -> list:
    '''
        Recebe: lista de dict de clients
        Retorna: lista de dict de clients sem  os dados/keys: peso, altura e as avaliações
    '''
    data_basic = list(map(map_client, lista_clientes))
    return data_basic

# get cliente todas avaliações
def get_formatted_data(lista_clientes: list, id:int):
    data_basic = []
    for client in lista_clientes:
        if client['id'] == id:
            data_basic.append({
                'id': client['id'],
                'nome': client['nome'],
                'altura': client['altura'],
                'peso': client['peso'],
                'avaliações': client['avaliações']
            })
    return data_basic

# get cliente com última avaliação
def get_client_last_measure(lista_clientes: list, id: int):
    data_basic = []
    for client in lista_clientes:
        if client['id'] == id:
            avaliacoes = client['avaliações']
            if avaliacoes:  # Verifica se a lista de avaliações não está vazia
                data_basic.append({
                    'nome': client['nome'],
                    'altura': client['altura'],
                    'peso': client['peso'],
                    'avaliações': avaliacoes[-1]
                })
    return data_basic

# post: com primeira avaliação 
def criar_dict_avaliacao(nome, peso, altura, data):
    # Cálculo
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    imc = peso / (altura ** 2)
    # Condicionais classificação
    classificacao = ''
    if imc < 18.5:
        classificacao = "MAGREZA"
    elif imc < 25.0:
        classificacao = "NORMAL"
    elif imc < 30.0:
        classificacao = "SOBREPESO I"
    elif imc < 40.0:
        classificacao = "OBESIDADE II"
    else:
        classificacao = "OBESIDADE GRAVE III"

    # Retorno do dict criado
    return {
        'nome': nome,
        'altura': altura,
        'peso': peso,
        'avaliações': [
          {
            "data": data,
            "imc": round(imc, 2),
            "classificação": classificacao
          }
        ]
    }

def create_new_client(nome, peso, altura, data, lista_clientes):
    new_client = criar_dict_avaliacao(nome, peso, altura, data)
    
    # 1st Ache o maior número id
    max_id = max(client['id'] for client in lista_clientes) if lista_clientes else 0
    
    # Incrementa ele
    new_id = max_id + 1
    
    # Confere se existe algum igual
    while any(client['id'] == new_id for client in lista_clientes):
        new_id += 1

    lista_clientes.append({
        'id': new_id,
        'nome': nome,
        'altura': altura,
        'peso': peso,
        'avaliações': new_client['avaliações']
    })
    
# update: mudando peso, coloca nova avaliação no []
def update_dict_avaliacao(id, peso, data, lista_clientes):

    for client in lista_clientes:
        if client['id'] == id:
            # Cálculo
            if client['altura'] <= 0:
                raise ValueError("A altura deve ser maior que zero.")
            imc = peso / (client['altura'] ** 2)
            # Condicionais classificação
            classificacao = ''
            if imc < 18.5:
                classificacao = "MAGREZA"
            elif imc < 25.0:
                classificacao = "NORMAL"
            elif imc < 30.0:
                classificacao = "SOBREPESO I"
            elif imc < 40.0:
                classificacao = "OBESIDADE II"
            else:
                classificacao = "OBESIDADE GRAVE III"
            
            client['peso'] = peso
            
            client['avaliações'].append({
                "data": data,
                "imc": round(imc, 2),
                "classificação": classificacao
            })

    return lista_clientes

# Delete client
def delete_client_by_id(id, lista_clientes):
    id_delete = None

    for index, client in enumerate(lista_clientes):
        if client['id'] == id:
            id_delete = index

    if id_delete is not None:
        del lista_clientes[id_delete]

    return lista_clientes