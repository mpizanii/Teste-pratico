# Projeto de Avaliação e Comparação das IAs do ChatGPT e do Gemini
Este projeto é uma aplicação Python que se conecta simultaneamente a duas APIs de modelos de linguagem (LLMs), ChatGPT e Gemini, para enviar perguntas e comparar as respostas fornecidas por ambos os modelos. A aplicação utiliza vários padrões de projeto, incluindo Factory, Command, Strategy, e Observer, para garantir uma estrutura flexível e extensível.
## Funcionalidades
- Conexão com APIs: Conecta-se simultaneamente às APIs do ChatGPT e do Gemini utilizando o padrão [Factory](https://refactoring.guru/pt-br/design-patterns/factory-method).
- Interface de Linha de Comando (CLI): Permite ao usuário enviar perguntas para ambos os modelos através de uma interface de linha de comando, utilizando o padrão [Command](https://refactoring.guru/pt-br/design-patterns/command) para encapsular a solicitação como um objeto, permitindo
parametrizar clientes com diferentes solicitações.
- Processamento de Respostas: Compara as respostas dos modelos usando critérios de avaliação, como clareza e tamanho da resposta, implementados com o padrão [Strategy](https://refactoring.guru/pt-br/design-patterns/strategy).
- Notificações: Utiliza o padrão [Observer](https://refactoring.guru/pt-br/design-patterns/observer) para notificar o usuário sobre o resultado da avaliação das respostas.
- Segurança: As chaves de API são armazenadas de forma segura em um arquivo .env.
## Instalação
### Pré-Requisitos
- Python 3.9 ou superior
- Bibliotecas listadas no arquivo [requeriments.txt](./requeriments.txt)
### Passos de Instalação
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/mpizanii/teste-pratico.git
   cd teste-pratico
   ```
2. **Crie um ambiente virtual**
   ```bash
   python -m venv env
   source env/bin/activate  # Para macOS/Linux
   env\Scripts\activate  # Para Windows
   ```
3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure suas chaves API**
- Crie um arquivo `.env` na raiz do projeto
- Adicione as chaves de API no arquivo `.env` (veja em [.env.example](./.env.example))
- **Nota**: Substitua `your-gpt-api-key` e `your-gemini-api-key` pelas suas chaves reais. Consulte as chaves em [Chave GPT](https://platform.openai.com/settings/profile?tab=api-keys) e [Chave Gemini](https://aistudio.google.com/app/apikey)
## Uso
1. **Execute o script principal**
   ```bash
   python main.py
   ```
2. **Siga as instruções na interface de linha de comando**
- Digite sua pergunta para enviar aos modelos
- Escolha o critério de avaliação (Clareza ou Tamanho)
- O resultado será mostrado com base na avaliação escolhida
## Estrutura do projeto
- [`factory.py`](./factory.py): Contém a implementação da fábrica de conexões para as APIs do ChatGPT e Gemini.
-  [`command.py`](./command.py): Implementa o padrão Command para encapsular a solicitação do usuário.
-  [`strategy.py`](./strategy.py): Contém as estratégias de avaliação das respostas (clareza e tamanho).
-  [`observer.py`](./observer.py): Implementa os padrões Observer e Subject para notificação de resultados.
-  [`main.py`](./main.py): Script principal que integra todas as funcionalidades.
-  `.env`: Armazena as chaves de API de forma segura (não incluído no repositório).
## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
## Apresentação

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
## Contato
Para dúvidas ou sugestões, entre em contato pelo email: mpizani28@gmail.com
  
