prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nType 'quit' to exit. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)