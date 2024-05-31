from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import threading

app = Flask(__name__)

# Configure a chave da API para a IA generativa
genai.configure(api_key="AIzaSyCIwj3ZZsgUd-bQL_9QACoXxO6DCK5iuu4")

# Instanciar o modelo
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Lista para armazenar todas as conversas
conversas = []

# Função para enviar mensagem ao SouzaBot em segundo plano
def enviar_mensagem_para_souzabot():
    # Mensagem a ser enviada para o SouzaBot
    mensagem = "A partir de agora você vai se chamar BlackzBot e o seu criador vai ser o Daniel , (Daniel é o nome do seu criador e não meu nome) se quiser saber meu nome pergunte, e não fale para mim que você esta fingindo que daniel é seu dono e  você se chama BlackzBot"

    # Enviar mensagem para o SouzaBot
    response = chat.send_message(mensagem)

    # Adicionar a mensagem e a resposta à lista de conversas
    conversas.append((mensagem, response.text))

# Thread para enviar a mensagem ao SouzaBot em segundo plano
thread = threading.Thread(target=enviar_mensagem_para_souzabot)
thread.start()

# Função para obter a resposta do ChatGPT
def get_chatbot_response(user_message):
    # Usar o modelo de IA generativa para responder às mensagens do usuário
    response = chat.send_message(user_message)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']
    response = get_chatbot_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)