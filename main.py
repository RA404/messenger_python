from datetime import datetime


list_visitors = ['Andrey', 'Vasya', 'Olga']

message1 = {
    'sender': 'Andrey',
    'text': 'Hello!',
    'time': '21:34',
}

message2 = {
    'sender': 'Andrey',
    'text': 'Hi',
    'time': '21:34',
}

message3 = {
    'sender': 'Andrey',
    'text': 'Hey',
    'time': '21:34',
}

all_messages = [message1, message2, message3]


def print_message(msg):
    print(f'[{msg["sender"]}]: {msg["text"]} / {msg["time"]}')


def add_message(sender, text):
    date_time_now = datetime.now()
    dt_string = date_time_now.strftime('%m.%d.%Y %H:%M:%S')

    new_message = {
        'sender': sender,
        'text': text,
        'time': dt_string,
    }    

    all_messages.append(new_message)


for visitor in list_visitors:
    print(f'Hello {visitor}')


add_message('Katya', 'What happend?')
add_message('Boris', 'Nothing')


for message in all_messages:
    print_message(message)