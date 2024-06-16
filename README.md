A chave API KEY do Groq você encontra em: https://console.groq.com/keys  
Crie um arquivo **.env** na raiz do projeto,  
e adicione o seguinte conteúdo:  
```
OPENAI_API_KEY=[SUA CHAVE API AQUI]  
GROQ_API_KEY=[SUA CHAVE API AQUI]
```

Comandos rodar para executar abaixo.  
Recomendo a criação de um environment (como abaixo) para não gerar conflito com bibliotecas que possua localemente.  
**Requisitos: Python 3.3+**  
Rodar os comandos abaixo na raiz do projeto:
``` 
python -m venv env1
env1\Scripts\activate
pip install -r requirements.txt
python teste.py
```
Expected output:
The result of the question "What is 2+2?" = 4
