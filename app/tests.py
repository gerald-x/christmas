import random

task = []

with open('messages.txt', 'r', encoding='utf-8') as file:
    for line in file:
        task.append(line.rstrip('\n'))

message = random.choice(task)
print(message)