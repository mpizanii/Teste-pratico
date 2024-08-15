from abc import ABC,abstractmethod
import google.generativeai as genai
import PIL.Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import openai
import openai.error

class ConexaoLLM(ABC):
    @abstractmethod
    def conexao(self) -> str:
        pass

class ConexaoGPT(ConexaoLLM):
    def conexao(self) -> str:
        chave = input("Cole aqui a sua chave de acesso da api do ChatGPT:") 
        openai.api_key = chave 
        prompt = input('Digite a mensagem:')
        messages = [ #criando uma memória das ultimas mensagens
                    {"role": "system", "content": "Você é um ótimo assistente."}, # define o comportamento do modelo, no caso, educado
                    ]
        messages.append({"role": "user", "content": prompt}) #adiciona a mensagem solicitada pelo usuario na memoria da IA
        while prompt.lower() != "fim":
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
                prompt = input('Digite a mensagem (Digite "fim" para sair):')
                if prompt.lower() == 'fim': #verifica se a mensagem é "fim", caso verdadeiro, quebra o ciclo
                    print("Encerrando conexão com o ChatGPT...")
                    break
                messages.append({"role": "user", "content": prompt})
            except openai.error.AuthenticationError:
                print("[ERRO]: Verifique sua chave de API e tente novamente.   ")
                break
            except openai.error.RateLimitError:
                print("[ERRO]: Você excedeu sua cota máxima de uso. Verifique sua cota em https://platform.openai.com/account/usage.")
                break
            except Exception as e:
                print(f"[ERRO]: Ocorreu um erro inesperado: {e}")
                break

class ConexaoGemini(ConexaoLLM):
    def conexao(self) -> str:
        API_KEY = 'chave' #tirei a chave por uma questão de segurança
        genai.configure(api_key=API_KEY)
        while True:
            escolha = input('Digite "img" para carregar uma imagem ou "msg" para questionar algo ao Gemini (Digite "fim" para sair):') #input do usuario
            if escolha == "fim":
                print("Encerrando conexão com Gemini...")
                break
            try:
                if escolha == "img":
                    Tk().withdraw()
                    caminho_imagem = askopenfilename(title="Selecione uma imagem", 
                                                    filetypes=[("Imagens", "*.jpg*.jpeg *.png *.bmp *.gif")])
                    if caminho_imagem:
                        img = PIL.Image.open(caminho_imagem) #abre o explorador de arquivo para o usuario selecionar a imagem
                        model = genai.GenerativeModel('gemini-1.5-flash')
                        prompt_imagem = input(
                            "Explique para o Gemini o que gostaria que ele fizesse com a imagem:")
                        response = model.generate_content([prompt_imagem, img]) 
                        print(response.text)
                    else:
                        print("Nenhuma imagem selecionada.") #caso o usuario cancele a operação
                elif escolha == "msg":
                    model = genai.GenerativeModel("gemini-pro")
                    prompt = input("Digite a mensagem:") #pergunta do usuario
                    response = model.generate_content(prompt)
                    print(response.text)
                else:
                    print("Opção inválida, tente novamente.") #caso o usuario tente escolher algo que nao seja img ou msg
            except Exception as e:
                print(f"[ERRO]: Ocorreu um erro inesperado: {e}")

class FactoryConexao: #abre a classe factory
    @staticmethod
    def criar_conexao(model_name: str) -> ConexaoLLM:
        if model_name == "gpt-3.5-turbo":
            return ConexaoGPT() #chama o método gpt
        elif model_name == "gemini-1.5-flash":
            return ConexaoGemini() #chama o método gemini
        else:
            raise ValueError("Modelo não suportado!") #caso o usuario tente escolher outra IA, que não esteja presente


        
        

    