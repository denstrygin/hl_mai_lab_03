CREATE USER IF NOT EXISTS 'monitor'@'%' IDENTIFIED BY 'admin123';
GRANT REPLICATION CLIENT ON *.* TO 'monitor'@'%';
FLUSH PRIVILEGES;

DROP DATABASE IF EXISTS messenger;
CREATE DATABASE messenger;

USE messenger;

CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    login VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS group_chats (
    chat_id INT AUTO_INCREMENT PRIMARY KEY,
    chat_name VARCHAR(255) NOT NULL,
    creator_user_id INT,
    FOREIGN KEY (creator_user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS group_chat_members (
    chat_id INT,
    user_id INT,
    FOREIGN KEY (chat_id) REFERENCES group_chats(chat_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    PRIMARY KEY (chat_id, user_id)
);

CREATE TABLE IF NOT EXISTS group_chat_messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    chat_id INT,
    sender_user_id INT,
    message_content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chat_id) REFERENCES group_chats(chat_id),
    FOREIGN KEY (sender_user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS ptp_messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    sender_user_id INT,
    recipient_user_id INT,
    message_content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_user_id) REFERENCES users(user_id),
    FOREIGN KEY (recipient_user_id) REFERENCES users(user_id)
);