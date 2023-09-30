from time import sleep

def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(2)
    except:
        print('Fechando conexão com banco de dados...')
        sleep(2)