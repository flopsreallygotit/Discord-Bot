import discord
import  time_command #My module
import wikipedia
import bad_words #My module
import random
import random_number #My module
wikipedia.set_lang('Choose your language')

time_now = str(time_command.time_now())

greetings = ['привет', 'hello', 'здорово', 'hi']

token = '' #Enter your token
client = discord.Client()

@client.event
async def on_ready():
    print('Bot is running!')
    
@client.event
async def on_message(message):

    author = str(message.author)
    name, tag = author.split('#')
    print(time_now, '['+name+']: ' + message.content)

    if name != 'Name of your BOT':

        for i in greetings:
            if i in message.content.lower():
                print(time_now + ' [Command]: hello ')
                await message.channel.send('Hello, ' + name + '!')
        if message.content.lower() == 'hi' or message.content.lower() == 'hi!': #I put the word separately for greater accuracy
            print(time_now + ' [Command]: hello ')
            await message.channel.send('Hi, ' + name + '!')
        
        if message.content.lower() == 'time' or message.content.lower() == '!time':
            print(time_now + ' [Command]: time')
            await message.channel.send(time_command.now())

        if 'timer' in message.content.lower():
            print(time_now + ' [Command]: timer')
            command, timer_time = map(str, message.content.lower().split())
            time_command.timer(timer_time)
            await message.channel.send('Time!') #Help me with timer please. When time ends, bot restarts

        if 'wiki' in message.content.lower():
            print(time_now + ' [Command]: wiki')
            search = message.content.lower().replace('wiki ','')
            page = wikipedia.page(search)
            await message.channel.send(page.content[0:1500] + '. Read it on: ' + page.url)

        if '!ran' in message.content.lower():
            print(time_now + ' [Command]: random')
            command, num1, num2 = map(str, message.content.lower().split())
            await message.channel.send(random_number.n(int(num1), int(num2)))

        for i in bad_words.words():
            if i in message.content.lower():
                print(time_now + ' [Bad Words]: 1') #Bot detected bad word, you must enter them yourself in bad_words.py
                answers = []
                answer = random.choice(answers)
                await message.channel.send(answer)
                break

client.run(token) #email me if u have any questions or for collab 


