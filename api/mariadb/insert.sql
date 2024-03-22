USE messenger;

INSERT INTO users (login, password, first_name, last_name, email)
VALUES
    ('user1', 'password1', 'John', 'Doe', 'john.doe@example.com'),
    ('user2', 'password2', 'Jane', 'Doe', 'jane.doe@example.com'),
    ('user3', 'password3', 'Mike', 'Smith', 'mike.smith@example.com'),
    ('user4', 'password4', 'Alice', 'Johnson', 'alice.johnson@example.com'),
    ('user5', 'password5', 'Bob', 'Brown', 'bob.brown@example.com'),
    ('user6', 'password6', 'Emma', 'Wilson', 'emma.wilson@example.com'),
    ('user7', 'password7', 'James', 'Taylor', 'james.taylor@example.com'),
    ('user8', 'password8', 'Olivia', 'Martinez', 'olivia.martinez@example.com'),
    ('user9', 'password9', 'William', 'Anderson', 'william.anderson@example.com'),
    ('user10', 'password10', 'Sophia', 'Thomas', 'sophia.thomas@example.com');

INSERT INTO group_chats (chat_name, creator_user_id)
VALUES
    ('Chat 1', 1),
    ('Chat 2', 2),
    ('Chat 3', 3),
    ('Chat 4', 4),
    ('Chat 5', 5),
    ('Chat 6', 6),
    ('Chat 7', 7),
    ('Chat 8', 8),
    ('Chat 9', 9),
    ('Chat 10', 10);

INSERT INTO group_chat_members (chat_id, user_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (1, 10);

INSERT INTO group_chat_messages (chat_id, sender_user_id, message_content)
VALUES
    (1, 1, 'Hello, everyone!'),
    (1, 2, 'Hi, John!'),
    (1, 3, 'How are you all?'),
    (1, 4, 'Doing great, thanks!'),
    (1, 5, 'Good to hear!'),
    (1, 6, 'What\'s new?'),
    (1, 7, 'Just working on a project.'),
    (1, 8, 'Sounds interesting!'),
    (1, 9, 'Yeah, it\'s going well.'),
    (1, 10, 'Great to hear!');

INSERT INTO ptp_messages (sender_user_id, recipient_user_id, message_content)
VALUES
    (1, 2, 'Hey, how are you?'),
    (2, 1, 'I\'m good, thanks! You?'),
    (3, 4, 'Did you finish the report?'),
    (4, 3, 'Yes, I\'ll send it over.'),
    (5, 6, 'Want to grab lunch?'),
    (6, 5, 'Sure, sounds good!'),
    (7, 8, 'Can you help me with this problem?'),
    (8, 7, 'Of course, what do you need?'),
    (9, 10, 'Happy birthday!'),
    (10, 9, 'Thank you so much!');