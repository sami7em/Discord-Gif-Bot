import discord
import praw
import random

client = discord.Client()
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent='sami7em')

prefix = ",,"
    
def gif(sreddit, source):
    urls = []
    for submission in reddit.subreddit(sreddit).hot(limit=100):
        if source in submission.url:
            urls.append(submission.url)
    gif = urls[random.randint(0, len(urls))]
    return gif
    
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(f'{prefix}help'):  
        msg = 'Commands: help, catgif, coolgif, satisfyinggif'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(f'{prefix}catgif'):
        msg = f'{gif("startledcats", "i.imgur")}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(f'{prefix}coolgif'):
        msg = f'{gif("mesmerizinggifs", "i.imgur")}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(f'{prefix}satisfyinggif'):
        msg = f'{gif("oddlysatisfying", "i.imgur")}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name=f'{prefix}help'))

client.run('token')
