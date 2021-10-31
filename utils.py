import json


def print_arrumado(valor):
    print(json.dumps(valor, indent=4, sort_keys=True))
