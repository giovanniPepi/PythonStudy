import praw

reddit = praw.reddit (
    client_id = 'roggisreal',
    client_secret = 'abc_123@AB',
    user_agent ='roggisreal',
    password='abc_123@AB',
)

print(reddit.read_only)