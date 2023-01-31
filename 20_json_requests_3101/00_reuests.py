import requests as req  # pip install requests (в терминале)


url = "https://google.com/"  # сохраняем URL-адрес, по которому будем подключаться
response = req.get(url)  # отсылаю GET-запрос к адресу URL

"""
GET-запрос - запрос на ПОЛУЧЕНИЕ данных от какого-то ресурса 
POST-запрос - это запрос на ОТПРАВКУ данных какому-то ресурсу 
"""
print(response.status_code)  # пытаюсь узнать статус подключения к ресурсу
"""
1xx - подключение совершено, но ответ еще не получен (сайт думает)
2xx - успешное подключение к ресурсу 
3xx - коды перенаправления (с vkontakte.ru на vk.com) 
Коды ошибок
4xx - 404 - попытка обратиться к странице, которой не существует (коды ошибок пользователя) 
401/403 - доступ запрещен
5xx - 502 - Bad Gateway - сервер/БД не может ответить на запрос (коды ошибки программиста)
"""
