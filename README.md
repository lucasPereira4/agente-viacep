# Agente ViaCEP

Projeto de exemplo que usa uma ferramenta externa para consultar endereço por CEP com a API do ViaCEP.

## Respostas da atividade

1. Como as ferramentas externas ajudam os agentes a executarem ações reais em um sistema?
R: As ferramentas externas permitem que o agente acesse dados e serviços fora do próprio código, como consultar a API do ViaCEP para obter informações reais de endereço. Isso amplia a capacidade do agente para executar ações que dependem de sistemas externos, como internet, banco de dados ou APIs.

2. Qual arquivo é a ferramenta? Qual é o agente? Qual é a orquestração?
R: A ferramenta é o arquivo `ferramentas.py`, que faz a consulta na API ViaCEP. O agente é o arquivo `agente.py`, que valida o CEP, chama a ferramenta e organiza a resposta em linguagem humana. A orquestração é o arquivo `main.py`, que coordena a interação entre o usuário e o agente.

3. O que aconteceria se o agente respondesse sem chamar a ferramenta?
R: Ele não teria acesso aos dados reais do endereço, então responderia sem confirmação, com informação incompleta ou errada. A ferramenta é o que traz os dados corretos da API.

4. Qual é o fluxo percorrido quando você digita um CEP?
R: O usuário digita um CEP no programa. O arquivo `main.py` chama o agente. O agente valida o CEP e, em seguida, chama a função em `ferramentas.py`, que consulta a API do ViaCEP. A API retorna um JSON com os dados do endereço e o agente transforma esse resultado em uma resposta legível para o usuário.

## Como executar

1. Ative o ambiente virtual:
   ```bash
   .venv\Scripts\activate
   ```
2. Instale as dependências:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Execute o projeto:
   ```bash
   python main.py
   ```
