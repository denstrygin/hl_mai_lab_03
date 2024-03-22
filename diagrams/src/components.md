# Компонентная архитектура
<!-- Состав и взаимосвязи компонентов системы между собой и внешними системами с указанием протоколов, ключевые технологии, используемые для реализации компонентов.
Диаграмма контейнеров C4 и текстовое описание. 
-->
## Компонентная диаграмма

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="microservice")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

Person(user, "Пользователь")

System_Boundary(chat_app, "Чат-приложение") {
   Container(app, "Клиентское веб-приложение", "HTML, JavaScript, React", "Портал чат-приложения")
   Container(auth_service, "Сервис авторизации", "Python, FastAPI", "Сервис управления пользователями", $tags = "microService")
   Container(chat_service, "Сервис чатов", "Python, FastAPI", "Сервис управления чатами и сообщениями", $tags = "microService")
   Container(messaging_service, "Сервис обмена сообщениями", "Python, FastAPI", "Сервис доставки сообщений", $tags = "microService")
   ContainerDb(db, "База данных", "MariaDB", "Хранение данных пользователей, чатов и сообщений", $tags = "storage")
}

Rel(user, app, "Взаимодействует с")

Rel(app, auth_service, "Авторизация, создание и поиск пользователей", "HTTP")
Rel(app, chat_service, "Управление чатами и сообщениями", "HTTP")
Rel(app, messaging_service, "Отправка и получение сообщений", "WebSocket")

Rel(auth_service, db, "Запросы к БД", "SQL")
Rel(chat_service, db, "Запросы к БД", "SQL")
Rel(messaging_service, db, "Запросы к БД", "SQL")

@enduml
```
## Список компонентов

### Сервис авторизации
**API**:
-	Создание нового пользователя
      - входыне параметры: login, password, first_name, last_name, email
      - выходные параметры, отсутствуют
-	Поиск пользователя по логину
     - входные параметры:  login
     - выходные параметры: user_id, first_name, last_name, email
-	Поиск пользователя по маске имя и фамилии
     - входные параметры: first_name_mask, last_name_mask
     - выходные параметры: user_id, login, first_name, last_name, email
### Сервис чатов
**API**:
- Создание группового чата
  - Входные параметры: chat_name, creator_user_id,  [member_user_ids]
  - Выходыне параметры: chat_id
- Добавление пользователя в чат
  - Входные параметры: chat_id, user_id
  - Выходные параметры: отсутствуют
- Добавление сообщения в групповой чат
  - Входные параметры: chat_id, sender_user_id, message_content
  - Выходные параметры: отсутствуют
- Загрузка сообщений группового чата
  - Входные параметры: chat_id
  - Выходные параметры: message_id, sender_user_id, message_content, timestamp


### Сервис обмена сообщениями
**API**:
- Отправка PtP сообщения пользователю
  - Входные параметры:  sender_user_id, recipient_user_id, message_content
  - Выходные параметры: отсутствуют
- Получение PtP списка сообщений для пользователя
  - Входные параметры: user_id, [optional_filters]
  - Выходные параметры: message_id, sender_user_id, recipient_user_id, message_content, timestamp
