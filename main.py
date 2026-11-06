from agente import agente_endereco


def orquestrador():
    """ORQUESTRAÇÃO: coordena o fluxo usuário -> agente -> ferramenta -> resposta."""
    print("=== Agente de Endereços (ViaCEP) ===")

    print(agente_endereco("01001000"))

    for cep in ["30140071", "20040030", "99999999"]:
        print(f"{cep}: {agente_endereco(cep)}")

    while True:
        try:
            cep = input("\nDigite um CEP (ou 'sair'): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAté logo!")
            break

        if cep.lower() == "sair":
            print("Até logo!")
            break

        print(agente_endereco(cep))


if __name__ == "__main__":
    orquestrador()
