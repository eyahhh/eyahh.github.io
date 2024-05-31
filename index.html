<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="apple-mobile-web-app-capable" content="yes"> <!-- Tela cheia no iOS -->
    <meta name="mobile-web-app-capable" content="yes"> <!-- Tela cheia no Android -->
    <title>Blackz Bot</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }
        #header {
            display: flex;
            align-items: center;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
        }
        #header img {
            max-width: 60px; /* Defina o tamanho máximo da largura da imagem aqui */
            height: auto; /* Isso permite que a altura seja ajustada automaticamente */
            margin-right: 10px;
        }
        .code-block {
            background-color: #000;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
            cursor: pointer;
        }
        #chat-container {
            width: 100%;
            height: calc(100vh - 50px);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            padding: 20px;
            box-sizing: border-box;
            overflow-y: auto;
        }
        #chat-messages {
            width: 100%;
            max-width: 600px;
            margin-bottom: 20px;
        }
        .message {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 10px;
            background-color: #007bff;
            color: #fff;
            max-width: 80%;
            word-wrap: break-word;
        }
        .message.sent {
            align-self: flex-end;
            background-color: #28a745;
        }
        #user-input {
            width: 100%;
            max-width: 600px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
            outline: none;
            margin-right: 10px;
        }
        #send-button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            outline: none;
            transition: background-color 0.3s ease;
        }
        #send-button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div id="header">
        <img src="https://th.bing.com/th/id/OIG3.c5eCgXkVIGk5_5ZpI3py?pid=ImgGn" alt="Logo Souza">
        <h1>Blackz Bot</h1>
    </div>
    <div id="chat-container">
        <div id="chat-messages"></div>
        <input type="text" id="user-input" placeholder="Digite sua mensagem...">
        <button id="send-button">&#10148;</button>
    </div>

    <script>
        const chatMessages = document.getElementById('chat-messages');
        const userInput = document.getElementById('user-input');
        const sendButton = document.getElementById('send-button');

        sendButton.addEventListener('click', () => {
            sendMessage(userInput.value);
            userInput.value = '';
        });

        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage(userInput.value);
                userInput.value = '';
            }
        });

        function sendMessage(message) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message', 'sent');
            messageElement.textContent = message;
            chatMessages.appendChild(messageElement);

            const scrollHeight = chatMessages.scrollHeight;
            chatMessages.scrollTo(0, scrollHeight);

            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message
                })
            })
            .then(response => response.json())
            .then(data => {
                const responseElement = document.createElement('div');
                responseElement.classList.add('message');
                // Se a mensagem da IA estiver entre aspas triplas, exibiremos como um bloco de código
                if (message.startsWith("'''") && message.endsWith("'''")) {
                    const codeBlock = document.createElement('pre');
                    codeBlock.classList.add('code-block');
                    codeBlock.textContent = data.response;
                    codeBlock.addEventListener('click', () => {
                        copyToClipboard(data.response);
                    });
                    responseElement.appendChild(codeBlock);
                } else {
                    responseElement.textContent = data.response;
                }
                chatMessages.appendChild(responseElement);

                const scrollHeight = chatMessages.scrollHeight;
                chatMessages.scrollTo(0, scrollHeight);
            });
        }

        function copyToClipboard(text) {
            navigator.clipboard.writeText(text)
                .then(() => alert('Conteúdo copiado para a área de transferência: ' + text))
                .catch((error) => console.error('Erro ao copiar conteúdo: ', error));
        }
    </script>
</body>
</html>
