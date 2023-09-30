def get_by_id(id, lista_clientes):
    for cliente in lista_clientes:
        if cliente['id'] == id:
            return cliente
        
def create_cliente_new(nombre, plato_favorito, lista_clientes: list):
    new_cliente = {
        'id': len(lista_clientes) + 1,
        'nombre': nombre,
        'plato_favorito': plato_favorito
    }
    lista_clientes.append(new_cliente)
    return lista_clientes

def update_cliente_by_id(nombre, plato_favorito, lista_clientes, id):
    for cliente in lista_clientes:
        if cliente['id'] == id:
            cliente['nombre']=  nombre
            cliente['plato_favorito']=  plato_favorito
    
    return lista_clientes

def delete_cliente_by_id(lista_clientes, id):
    lista_clientes.pop(id - 1)
    new_id = 0
    for cliente in lista_clientes:
        new_id +=1
        cliente['id'] = new_id
    
    return lista_clientes