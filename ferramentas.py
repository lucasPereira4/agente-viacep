import requests


def consultar_cep(cep):
    """FERRAMENTA EXTERNA: consulta a API ViaCEP e devolve os dados do CEP."""
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code != 200:
            return {"erro": "formato"}
        dados = resposta.json()
    except (requests.exceptions.RequestException, ValueError):
        return {"erro": "conexao"}

    return dados
