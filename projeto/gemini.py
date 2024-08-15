import google.generativeai as genai
import PIL.Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def gemini():
    API_KEY = 'AIzaSyDkG7n0T6oal2EKmIM3h_LkKQbklpbYyBs'
    genai.configure(api_key=API_KEY)
    while True:
        escolha = input('Digite "img" para carregar uma imagem ou "msg" para questionar algo ao Gemini (Digite "fim" para sair):')
        if escolha == "fim":
            print("Encerrando...")
            break
        try:
            if escolha == "img":
                Tk().withdraw()
                caminho_imagem = askopenfilename(title="Selecione uma imagem", 
                                                filetypes=[("Imagens", "*.jpg*.jpeg *.png *.bmp *.gif")])
                if caminho_imagem:
                    img = PIL.Image.open(caminho_imagem)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = input(
                        "Explique para o Gemini o que gostaria que ele fizesse com a imagem:")
                    response = model.generate_content([prompt, img])
                    print(response.text)
                else:
                    print("Nenhuma imagem selecionada.")
            elif escolha == "msg":
                model = genai.GenerativeModel("gemini-pro")
                mensagem = input("Digite a mensagem:")
                response = model.generate_content(mensagem)
                print(response.text)
            else:
                print("Opção inválida, tente novamente.")
        except Exception as e:
            print(f"[ERRO]: Ocorreu um erro inesperado: {e}")
