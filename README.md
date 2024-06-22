Este repositório contém um exemplo de requisição para a API do **Groq** (não confundir com o Grok do Elon Musk).  

Este serviço Groq é um serviço que possui um hardware de inferência de LLM (large language model) que é promissor, por ser rápido e de alta eficiencia energética quando comparado às GPU convencionais que os modelos usam hoje (pelo menos até Junho/2024).  


A **chave API KEY** do Groq você gera em: https://console.groq.com/keys  
Crie um arquivo **.env** na raiz do projeto,  
e adicione o seguinte conteúdo:  
```
GROQ_API_KEY=[SUA CHAVE API AQUI]
```

Recomendo a criação de um environment (com o venv abaixo) para não gerar conflito com bibliotecas que possua localemente.  
**Requisitos: Python 3.3+**  
Rodar os comandos na raiz do projeto:
``` 
python -m venv env1
env1\Scripts\activate
pip install -r requirements.txt
python teste.py
```
Expected output:  
The result of the question "What is 2+2?" = 4
