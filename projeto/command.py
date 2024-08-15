from abc import ABC, abstractmethod
from factory import FactoryConexao

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class PromptGPT(Command):
    def __init__(self, conexao_gpt):
        self.conexao_gpt = conexao_gpt

    def execute(self):
        self.conexao_gpt.conexao()

class PromptGemini(Command):
    def __init__(self, conexao_gemini):
        self.conexao_gemini = conexao_gemini

    def execute(self):
        self.conexao_gemini.conexao()

class Invoker:
    def __init__(self):
        self.commands = {}
    
    def set_command(self, name: str, command: Command):
        self.commands[name] = command

    def execute_command(self, name: str):
        if name in self.commands:
            self.commands[name].execute()
        else:
            print(f"[ERRO]: Comando {name} não encontrado.")

def main():  
    invoker = Invoker()  # Instancia o Invoker
    while True:
        print('Digite "fim" para sair.')
        escolha1 = input('Digite qual IA deseja usar ("gpt ou gemini"): ')
        try:
            if escolha1.lower() == "gpt":
                conexao = FactoryConexao.criar_conexao("gpt-3.5-turbo")
                comando = PromptGPT(conexao)
                invoker.set_command("gpt", comando)
                invoker.execute_command("gpt")
            elif escolha1.lower() == "gemini":
                conexao = FactoryConexao.criar_conexao("gemini-1.5-flash")
                comando = PromptGemini(conexao)
                invoker.set_command("gemini", comando)
                invoker.execute_command("gemini")
            elif escolha1.lower() == "fim":
                print("Encerrando conexão...")
                break
            else:
                print("Modelo não suportado!")
        except ValueError as e:
            print(f"[ERRO]: {e}")
            break
        
if __name__ == '__main__':
    main()
