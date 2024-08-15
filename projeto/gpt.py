import openai
import openai.error

def chatgpt():
    chave = input("Cole aqui a sua chave de acesso da api do ChatGPT:") 
    openai.api_key = chave 
    mensagem = input('Digite a mensagem:')
    messages = [ #criando uma memória das ultimas mensagens
        {"role": "system", "content": "Você é um ótimo assistente."}, # define o comportamento do modelo, no caso, educado
                ]
    messages.append({"role": "user", "content": mensagem}) #adiciona a mensagem solicitada pelo usuario na memoria da IA
    while mensagem.lower() != "fim":
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages = messages,
                temperature=0.7,
                max_tokens=2048,
                n=1,
                stop=None
            )
            resposta = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": resposta}) #adiciona a resposta a lista de memórias da IA
            print("Resposta: ", resposta)
            mensagem = input('Digite a mensagem (Digite "fim" para sair):')
            if mensagem.lower() == 'fim': #verifica se a mensagem é "fim", caso verdadeiro, quebra o ciclo
                print("Encerrando o chat...")
                break
            messages.append({"role": "user", "content": mensagem})
        except openai.error.AuthenticationError:
            print("[ERRO]: Verifique sua chave de API e tente novamente.")
            break
        except openai.error.RateLimitError:
            print("[ERRO]: Você excedeu sua cota máxima de uso. Verifique sua cota em https://platform.openai.com/account/usage.")
            break
        except Exception as e:
            print(f"[ERRO]: Ocorreu um erro inesperado: {e}")
            break




