def show_messages(messages):
    """Print the messages received. """
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message) 

messages = ['hi', 'hello', 'teste', 'auehuaeh brbr']
sent_messages =[]

show_messages(messages[:])

print(messages)
print(sent_messages)
