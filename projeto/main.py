from senha import api_key
import requests
import json

headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

conteudo = input('Digite a mensagem:')
body_mensagem = {
    "model": "gpt-3.5-turbo",
    "messages" : [{"role": "user", "content": conteudo}]
}
body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagem)
resposta = requisicao.json()
mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)


