import requests

AUTH_SERVICE_URL = "http://localhost:8000"
CHAT_SERVICE_URL = "http://localhost:8001"
PTP_SERVICE_URL = "http://localhost:8002"

def test_auth_service():
    # Создание нового пользователя
    new_user = {
        "user_id": 1,
        "login": "wkfbwek",
        "password": "password3",
        "first_name": "Test3",
        "last_name": "User3",
        "email": "wjbfkwb@example.com"
    }
    response = requests.post(f"{AUTH_SERVICE_URL}/create_user/", json=new_user)
    assert response.status_code == 200

    # Поиск пользователя по логину
    response = requests.get(f"{AUTH_SERVICE_URL}/get_user_by_login/", params={"login": new_user["login"]})
    assert response.status_code == 200
    assert response.json()["login"] == new_user["login"]

    # Поиск пользователя по маске имени и фамилии
    response = requests.get(f"{AUTH_SERVICE_URL}/search_users/", params={"first_name_mask": "Te", "last_name_mask": "Us"})
    assert response.status_code == 200
    assert any(user["login"] == new_user["login"] for user in response.json())

def test_chat_service():
    # Создание первого пользователя
    user1_response = requests.post(f"{AUTH_SERVICE_URL}/create_user/", json={
        "user_id": 2,
        "login": "wefkjwebf",
        "password": "password",
        "first_name": "User",
        "last_name": "One",
        "email": "wjfwsdw@example.com"
    })
    assert user1_response.status_code == 200
    user1_id = user1_response.json()["user_id"]

    # Создание второго пользователя
    user2_response = requests.post(f"{AUTH_SERVICE_URL}/create_user/", json={
        "user_id": 3,
        "login": "jwefkw",
        "password": "password",
        "first_name": "User",
        "last_name": "Two",
        "email": "wejfwen@example.com"
    })
    assert user2_response.status_code == 200
    user2_id = user2_response.json()["user_id"]

    # Создание нового группового чата пользователем 1
    new_chat_response = requests.post(f"{CHAT_SERVICE_URL}/create_group_chat/", json={
        "chat_name": "New Test Chat",
        "creator_user_id": user1_id,
        "member_user_ids": [user1_id]
    })
    assert new_chat_response.status_code == 200
    new_chat_id = new_chat_response.json()["chat_id"]

    # Добавление пользователя 2 в новый чат
    add_user_response = requests.post(f"{CHAT_SERVICE_URL}/add_user_to_chat/", json={
        "chat_id": new_chat_id,
        "user_id": user2_id
    })
    assert add_user_response.status_code == 200

    # Добавление сообщения в новый групповой чат пользователем 1
    new_message = {
        "chat_id": new_chat_id,
        "sender_user_id": user1_id,
        "message_content": "Welcome to the new chat!"
    }
    response = requests.post(f"{CHAT_SERVICE_URL}/add_message_to_chat/", json=new_message)
    assert response.status_code == 200

    # Загрузка сообщений нового группового чата
    response = requests.get(f"{CHAT_SERVICE_URL}/get_chat_messages/", params={"chat_id": new_chat_id})
    assert response.status_code == 200
    assert any(message["message_content"] == new_message["message_content"] for message in response.json())

def test_ptp_service():
    # Отправка PtP сообщения пользователю
    new_ptp_message = {
        "sender_user_id": 1,
        "recipient_user_id": 1,
        "message_content": "Hello, User!"
    }
    response = requests.post(f"{PTP_SERVICE_URL}/send_ptp_message/", json=new_ptp_message)
    assert response.status_code == 200

    # Получение PtP списка сообщений для пользователя
    response = requests.get(f"{PTP_SERVICE_URL}/get_ptp_messages/", params={"user_id": 1})
    assert response.status_code == 200
    assert any(message["message_content"] == new_ptp_message["message_content"] for message in response.json())

if __name__ == "__main__":
    # test_auth_service()
    # test_chat_service()
    # test_ptp_service()
    print("All tests passed!")
