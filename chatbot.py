import openai 

chave_api = "sk-proj-jwn2ZpkRcRqP2esE461LT3BlbkFJmG0ynDHp8ESoEuDWp76i"

openai.api_key = chave_api

def enviar_mensagem(mensagem):
    resposta = openai.Chatcompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": mensagem}
        ],

    )

    return resposta["choices"] [0] ["message"]


while True:
    texto = input("Escreva aqui sua mensagem:")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto)
        print("Chatbot:", resposta ["content"])

print(enviar_mensagem("Em que poderia te ajudar?"))
