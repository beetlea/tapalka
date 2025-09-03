// Глобальный трекер для Telegram Web App
(function() {
    if (window.Telegram && window.Telegram.WebApp) {
        const user = window.Telegram.WebApp.initDataUnsafe.user;
        
        if (user) {
            function sendAction(action) {
                navigator.sendBeacon('/user_action', JSON.stringify({
                    action: action,
                    user_id: user.id,
                    username: user.username || 'Неизвестен'
                }));
            }
            
            // События видимости страницы
            document.addEventListener('visibilitychange', () => {
                if (document.hidden) {
                    sendAction('свернул приложение');
                } else {
                    sendAction('развернул приложение');
                }
            });
            
            // Событие закрытия приложения
            window.addEventListener('beforeunload', () => {
                sendAction('закрыл приложение');
            });
            
            // Событие паузы приложения (специфично для Telegram)
            window.addEventListener('pagehide', () => {
                sendAction('закрыл приложение');
            });
        }
    }
})();