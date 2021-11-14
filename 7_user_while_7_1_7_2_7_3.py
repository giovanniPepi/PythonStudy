# input ()

# '+=' takes the string that was assigned to prompt and adds the new string onto the end

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
