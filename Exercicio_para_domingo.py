"""Fazer um exercício que leia o dicionário e efetue as seguintes alteracoes:
1 - Troque o nome completo do Estado pela sua respectiva sigla
2 - Sempre que houver um dado desconhecido trocar pela variável nula
3 - o email: acaso esteja como desconhecido trocar pelo modelo "nome.sobrenome@gmail.com", garantir que TODOS
OS EMAIL estejam em letra minúscula (low case)
4 - Trocar o nome do curso "A melhor linguagem do mundo" para "Python"
5 - Transformar o valor de cursos para o seguinte dicionário:
'cursos': {'Quantidade de cursos':
'Aluno Aplicado': True or False
'Aluno da melhor professora': True or False
'cursos do aluno': [lista dos cursos do aluno]}
O Aluno será aplicado se fizer mais de 2 cursos
O Aluno será aluno da melhor professora de estiver no curso de Python
*********************************************
Um exemplo de resolução:
{'usuarios': [{'nome completo': 'Matheus Esteque',
'Estado': 'Roraima',
'email': 'Matheus.Esteque@gmail.com',
'cursos': ['Pascal', 'JavaScript', 'C', 'Assembly', 'C++', 'Rusty'],
'phone': 981972367,
'endereço': 'Estrada Girassol',
'CEP': 1549431}, ]}

resposta esperada:
[{'nome completo': 'Matheus Esteque',
'Estado': 'RR',
'email': 'matheus.esteque@gmail.com',
'cursos': {'Quantidade de cursos': 6
'Aluno Aplicado': True
'Aluno da melhor professora': False
'cursos do aluno': ['Pascal', 'JavaScript', 'C', 'Assembly', 'C++', 'Rusty']},
'phone': 981972367,
'endereço': 'Estrada Girassol',
'CEP': 1549431}]

# dica mentora: fazer uma classe, e na hora de instanciar fazer uma lista da classe
# se não, fazer um for/in para fazer as variações
"""

from predef_dict import dict_users
from utils import print_arrumado
from estados import dict_estados


lista_usuarios = dict_users["usuarios"]

contador = 0
for usuario in lista_usuarios:
    # 1 - Troque o nome completo do Estado pela sua respectiva sigla
    estado_user = usuario["Estado"]
    uf = dict_estados[estado_user]
    usuario["Estado"] = uf

    # 2 - Sempre que houver um dado desconhecido, trocar pela variável nula

    if usuario["nome completo"] == "desconhecido":
        usuario["nome completo"] = None

    if usuario["Estado"] == "desconhecido":
        usuario["Estado"] = None

    # 3 - Caso o e-mail esteja como desconhecido, trocar pelo modelo "nome.sobrenome@gmail.com", garantir que TODOS OS
    # E-MAILS estejam em letra minúscula (lower case)

    usuario["email"] = usuario["email"].lower()

    if usuario["email"] == "desconhecido":
        nom_sobren = usuario["nome completo"].split()
        primeiro_nome = nom_sobren[0]
        sobrenome1 = nom_sobren[-1]
        sobrenome2 = nom_sobren[-2]

        if sobrenome2 is None:
            pass
        else:
            continue
        # prof não consegui fazer com que ele adc o '.' depois do 1º sobrenome pra quem tinha 2 ):
        email_arrumado = primeiro_nome + "." + sobrenome1 + "." + sobrenome2 + "@gmail.com"
        usuario["email"] = email_arrumado.lower()

    if usuario["phone"] == "desconhecido":
        usuario["phone"] = None

    if usuario["endereço"] == "desconhecido":
        usuario["endereço"] = None

    if usuario["CEP"] == "desconhecido":
        usuario["CEP"] = None

    cursos_users = usuario["cursos"]

    # 4 - Trocar o nome do curso "A melhor linguagem do mundo" para "Python"

    if "A melhor linguagem do mundo" in usuario["cursos"]:
        indice_python = usuario["cursos"].index("A melhor linguagem do mundo")
        usuario["cursos"][indice_python] = "Python"

    # 5 - Transformar o valor de cursos para o dicionário (comentário do início)

    usuario["cursos"] = {
        "Quantidade de cursos": len(cursos_users),
        "Aluno Aplicado": len(cursos_users) > 2,
        "Aluno da melhor professora": "Python" in usuario["cursos"],
        "cursos do aluno": cursos_users
    }

    print_arrumado(usuario)
    contador += 1
