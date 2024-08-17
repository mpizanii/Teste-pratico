import os
from dotenv import load_dotenv
from abc import ABC,abstractmethod
import google.generativeai as genai
import openai
import openai.error

load_dotenv()

class ConexaoLLM(ABC):
    @abstractmethod
    def conexao(self, prompt: str) -> str:
        pass

class ConexaoGPT(ConexaoLLM):
    def conexao(self, prompt: str) -> str:
        chave = os.getenv("gpt_key")
        openai.api_key = chave 
        messages = [  
            {"role": "system", "content": "Você é um ótimo assistente."},  
            {"role": "user", "content": prompt}  
        ]
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=2048,
                n=1,
            )
            resposta = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": resposta}) 
            return resposta
        except openai.error.AuthenticationError:
            return "[ERRO]: Verifique sua chave de API e tente novamente."
        except openai.error.RateLimitError:
            return "[ERRO]: Você excedeu sua cota máxima de uso. Verifique sua cota em https://platform.openai.com/account/usage."
        except Exception as e:
            return f"[ERRO]: Ocorreu um erro inesperado: {e}"


class ConexaoGemini(ConexaoLLM):
    def conexao(self, prompt: str) -> str:
        chave = os.getenv("gemini_key")
        genai.configure(api_key=chave)
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt) 
            return response.text 
        except Exception as e:
            print(f"[ERRO]: Ocorreu um erro inesperado: {e}")

class FactoryConexao: 
    @staticmethod
    def criar_conexoes() -> dict:
        conexoes = {
            "gpt": ConexaoGPT(),  
            "gemini": ConexaoGemini() 
        }
        return conexoes

        

        
        

    