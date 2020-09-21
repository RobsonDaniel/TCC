import json
from datetime import datetime
'''
ssc/201/acesso
ssc/202/acesso
ssc/203/acesso
ssc/222/acesso

ACESSO PERMITIDO - ARMAZENAR
documentoJSON = {
  "permitido": valor_boolean,
  "usuario": {
    "nome": "valor_string",
    "vinculo": valor_boolean,
    "registro": "valor_string",
    "id": valor_inteiro,
    "horario_cadastrado": "valor_data",
    "horario_tag": "valor_data"
  },
  "tag": {
    "id": valor_inteiro,
    "codigo": "valor_string",
    "horario": "valor_data"
  },
  "sala": {
    "numero": valor_inteiro,
    "nome_completo": "valor_string",
    "nome_curto": "valor_string",
    "id": valor_inteiro,
    "horario": "valor_data"
  },
  "horario": "valor_data"
}

ACESSO NEGADO - IGNORAR
documentoJSON = {
  "permitido": valor_boolean,
  "sala": {
    "numero": valor_inteiro,
    "nome_completo": "valor_string",
    "nome_curto": "valor_string",
    "id": valor_inteiro,
    "horario": "valor_data"
  },
  "horario": "valor_data"
}

'''

def ssc_sensor(lista_topico, mensagem):
    id = lista_topico[1]
    sensor = lista_topico[3]
    valor_sensor = json.loads(mensagem.decode('UTF-8'))

    documento = {
        'id': id,
        'nome_sensor': sensor,
        'valor': valor_sensor,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return documento

def ssc_informacao(mensagem):
    return json.loads(mensagem.decode('UTF-8'))

def formatar(index, lista_topico, mensagem):
    if index == "ssc_sensor":
        return ssc_sensor(lista_topico, mensagem)
    elif index == "ssc_informacao":
        return ssc_informacao(mensagem)
    elif index == "ssc_acesso":
        pass
