from abc import ABC, abstractmethod
from strategy import Avaliador
from observer import Observer, Subject

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Prompt_Modelos(Command):
    def __init__(self, prompt: str, conexoes: dict, avaliador: Avaliador, subject: Subject):
        self.prompt = prompt
        self.conexoes = conexoes
        self.avaliador = avaliador
        self.subject = subject
        
    def execute(self):
        resposta_gpt = self.conexoes["gpt"].conexao(self.prompt)
        resposta_gemini = self.conexoes["gemini"].conexao(self.prompt)

        resultado = self.avaliador.avaliar(resposta_gpt, resposta_gemini)
        self.subject.notify_observers(resultado)

        print(f"Resposta do GPT: {resposta_gpt}")
        print(f"Resposta do Gemini: {resposta_gemini}")
        print(f"Avaliação: {resultado}")

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

class ResultadoObserver(Observer):
    def update(self, mensagem: str):
        print(mensagem)