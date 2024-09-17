document.getElementById('check-balance-button').addEventListener('click', function () {
    let userId = localStorage.getItem('userId');
    if (!userId) {
        userId = 'user-' + Math.random().toString(36).substr(2, 9);
        localStorage.setItem('userId', userId);
    }

    fetch('/update_balance', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ userId: userId, stars: 250 }) // 250 звезд, например
    }).then(response => response.json()).then(data => {
        alert(`Баланс сообщений пополнен. У вас теперь ${data.messages_left} сообщений.`);
        window.location.href = '/chat';
    });
});
