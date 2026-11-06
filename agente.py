from ferramentas import consultar_cep


def agente_endereco(cep):
    """AGENTE: valida o pedido, usa a ferramenta e organiza a resposta."""
    cep = str(cep).replace("-", "").replace(".", "").strip()

    if len(cep) != 8 or not cep.isdigit():
        return "CEP inválido. Digite 8 números (ex.: 01001000)."

    dados = consultar_cep(cep)

    if "erro" in dados:
        if dados["erro"] == "conexao":
            return "Não consegui acessar a API. Verifique sua internet."
        return "CEP não encontrado."

    rua = dados.get("logradouro") or "(logradouro não informado)"
    cidade = dados.get("localidade", "")
    estado = dados.get("uf", "")

    resposta = f"O CEP informado pertence a {rua}, {cidade} - {estado}."
    return resposta
