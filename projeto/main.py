from factory import *
from command import *
from strategy import *
from observer import *

def extrair_palavras_chave(prompt: str) -> set:
    return set(prompt.lower().split())

def main():
    invoker = Invoker() 
    conexoes = FactoryConexao.criar_conexoes()  

    # Cria o Subject e o Observer
    avaliacao_subject = Subject()
    resultado_observer = ResultadoObserver()
    avaliacao_subject.add_observer(resultado_observer)
    
    while True:
        print('Digite "fim" para sair')
        prompt = input('Digite a mensagem que deseja enviar para os modelos: ')
        if prompt.lower() == "fim":
            print("Encerrando conexão...")
            break

        
        resposta_gpt = conexoes["gpt"].conexao(prompt)
        resposta_gemini = conexoes["gemini"].conexao(prompt)

        
        print("\nResposta do GPT:")
        print(resposta_gpt)
        print("\nResposta do Gemini:")
        print(resposta_gemini)

        
        escolha_avalicao = input('Digite "clareza" para avaliar clareza ou "tamanho" para avaliar tamanho: ')
        
        if escolha_avalicao.lower() == "clareza":
            palavras_chave = extrair_palavras_chave(prompt)
            avaliacao = Avaliador(AvaliacaoClareza(palavras_chave))
            criterio = "clareza"
        elif escolha_avalicao.lower() == "tamanho":
            avaliacao = Avaliador(AvaliacaoTamanho())
            criterio = "tamanho"
        else:
            print("Opção de avaliação inválida!")
            continue

        resultado_avaliacao = avaliacao.avaliar(resposta_gpt, resposta_gemini)

        
        avaliacao_subject.notify_observers(resultado_avaliacao)

        print(f"\nAvaliação ({criterio}): {resultado_avaliacao}")

if __name__ == '__main__':
    main()



