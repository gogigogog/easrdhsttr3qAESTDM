document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('message-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') sendMessage();
});

let userId = localStorage.getItem('userId');
if (!userId) {
    userId = 'user-' + Math.random().toString(36).substr(2, 9);
    localStorage.setItem('userId', userId);
}

// Получаем количество оставшихся сообщений
fetch(`/get_balance?userId=${userId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('message-limit').textContent = `Осталось сообщений: ${data.messages_left}`;
    });

function sendMessage() {
    const inputField = document.getElementById('message-input');
    const messageText = inputField.value.trim();

    if (messageText === '') return;

    fetch('/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: messageText, userId: userId })
    }).then(response => response.json()).then(data => {
        if (data.status === 'No messages left') {
            alert('У вас не осталось сообщений!');
        } else {
            fetchMessages();
        }
    });

    inputField.value = '';
}

// Логика получения и отображения сообщений...
