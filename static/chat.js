async function sendMessage() {
  const userInput = document.getElementById('user-input');
  const message = userInput.value.trim();

  if (message === '') return;

  // Append user message to chat box
  appendMessage('user', message);
  userInput.value = '';

  // Send message to server
  const response = await fetch('/send_message', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message: message })
  });

  const data = await response.json();
  appendMessage('bot', data.response);
}

function appendMessage(sender, text) {
  const chatBox = document.getElementById('chat-box');
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', sender);
  messageElement.innerHTML = `<div class="message-content"><p>${text}</p></div>`;
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}