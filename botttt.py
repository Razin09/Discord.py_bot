
''' basic discord bot using discord.py'''

import discord
from discord.ext import commands
import random
import imdb
import time
import json
from PyDictionary import PyDictionary


moviesDB = imdb.IMDb()   # imdb api, using to get movie data stright from imdb
client = commands.Bot(command_prefix = ".")   # command prefix to call commands
dictionary1 = PyDictionary()

dares = [
    "Do freestyle rap for 1 minute about the other participants.",
    "Kiss the person to your left.",
    "Call your crush",
    "Dance with no music for 1 minute.",
    "Let the person on your right draw on your face.",
    "Drink lemon juice.",
    "Call a friend, pretend it’s their birthday, and sing “Happy Birthday” to them.",
    "Pour ice down your pants.",
    "Spin around 12 times and try to walk straight.",
    "Talk without closing your mouth.",
    "You have 5 minutes to write a country song and perform it.",
    "Do 5 minutes of stand-up comedy.",
    "Quack like a duck until your next turn.",
    "Sing the national anthem in a British accent.",
    "say 'ara ara sayonara'",
    "Eat a spoonful of sugar.",
    "Do a silly dance.",
    "Lick your elbow.",
    "Go outside and yell “Merry Christmas!”",
    "Talk and act like a cowboy.",
    "Draw something blindfolded.",
    "jump 10 times"

]
truths = [
    "What’s the last lie you told?",
    "What was the most embarrassing thing you’ve ever done on a date?",
    "Have you ever accidentally hit something (or someone!) with your car?",
    "Name someone you’ve pretended to like but actually couldn’t stand.",
    "What’s your most bizarre nickname?",
    "What’s been your most physically painful experience?",
    "What’s the craziest thing you’ve done on public transportation?",
    "If you met a genie, what would your three wishes be?",
    "Who was your worst kiss ever?",
    "What’s the craziest thing you’ve done in front of a mirror?",
    "What’s the meanest thing you’ve ever said about someone else?",
    "Who are you most jealous of?",
    "Who’s the oldest person you’ve dated?",
    "How many selfies do you take a day?",
    "How many times a week do you wear the same pants?",
    "Would you date your high school crush today?",
    "What’s one movie you’re embarrassed to admit you enjoy?",
    "When’s the last time you apologized? What for?",
    "What app do you waste the most time on?",
    "What is the youngest age partner you’d date?",
    "Have you ever lied about your age?",
    "What’s your most embarrassing late night purchase?",
    "Have you ever used a fake ID?",
    "Which of your family members annoys you the most and why?",
    "What celebrity do you think is overrated?",
    "Have you ever lied to your boss?",
    "What’s the longest you’ve gone without brushing your teeth?"
    "Have you ever ghosted a friend?",
    "What’s one thing in your life you wish you could change?",
]



@client.event
async def on_ready():
    ''' to print a message on the console when the bot is ready '''
    print("The bot is online")

@client.command()
async def ping(ctx):
    ''' this command will sent the authors internet ping latency on ms'''
    await ctx.channel.send(f"your ping is {round(client.latency * 1000)} ms")

@client.command()
async def math(ctx, x:int, op, y:int):
    ''' this command will do some basics math operations by passing the values and operation'''

    if op == "+":
        answer = x + y
        await ctx.channel.send(f'Answer = {x} + {y} = {answer}')
    elif op == "-":
        answer = x - y
        await ctx.channel.send(f'Answer = {x} - {y} = {answer}')
    elif op == "*":
        answer = x * y
        await ctx.channel.send(f'Answer = {x} * {y} = {answer}')
    elif op == "/":
        answer = x * y
        await ctx.channel.send(f'Answer = {x} / {y} = {answer}')
    else:
        await ctx.channel.send(f"'{op}' is an invalid command, use only '+,-,*,/'")

@client.command()
async def clear(ctx, amount=5):
    '''
    this command will clear upto 5 messages from the server chat, you can change the value.
    first you have to give Administrator permission or manage channel / message permisson from the discord dev portal.
    put the clear limit using elif. this command can clear all the messages from the server. so be carefull with the amounts
    '''
    if amount <= 5:
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f"{amount} messages has been deleted from the server")
    else:
        await ctx.channel.send("You can only delete 5 messages at a time, try again")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    '''
    this command will kick someone from the server.
    you have to give Administrator permission or kick member permission to the bot fom discord dev portal
    with 'member : discord.member' you can tag the person
    you can add the reason of kicking, diffult reasone is None
    '''
    await member.kick(reason=reason)
    await ctx.channel.send(f"{member} has been kicked out from the server,\nReason = {reason}")

@client.command(aliases = ["qq","QQ","Qq"])
async def _8ball(ctx, *, question):
    '''
    a basic 8ball game. you can ask the bot any yes or no questions.
    there is 20 responses. with posstive and negative answers to the question.
    using aliases, its easy to call the command
    '''
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send(f"Question : {question}\nAnswer    : {random.choice(responses)}")

@client.command()
async def tod(ctx, td):
    '''
    basic truth or dare game.
    it'll ask a truth or dare from the truths,dares list.
    you just need to pass t or d after the command.
    '''
    if td == "t":
        await ctx.channel.send(random.choice(truths))
    elif td == "d":
        await ctx.channel.send(random.choice(dares))
    else:
        await ctx.channel.send("sorry, ivalid command. use 't' or 'd'")

@client.command()
async def movie(ctx, movie = None):
    '''
    getting movie info from imdb using offical imdb api
    pass the movie name after the command.
    it'll show the movie title, year, imdb rating, directors and the casting
    '''
    movies = moviesDB.search_movie(movie)
    id = movies[0].getID()
    movie = moviesDB.get_movie(id)

    title = movie['title']
    year = movie['year']
    rating = movie['rating']
    directors = movie['directors']
    casting = movie['cast']
    await ctx.channel.send(f'About the movie {movie}\n\n\n')
    await ctx.channel.send(f'\nmovie name - {title}')
    await ctx.channel.send(f'released on - {year}')
    await ctx.channel.send(f'imdb rating is - {rating}')

    direcStr = ''.join(map(str,directors))
    await ctx.channel.send(f'directed by - {direcStr}')

    actorStr = ', '.join(map(str,casting[0:5]))
    await ctx.channel.send(f'main actors - {actorStr}')

@client.command()
async def word(ctx, word = None):
    '''
    this command is and dictionary command
    just pass the word you want to serch and the bot will pass the noun, verb, synonym and antonym of the word
    used PyDictionary
    '''
    try:

        noun = (dictionary1.meaning(word)['Noun'])
        verb = (dictionary1.meaning(word)['Verb'])
        synonym = (dictionary1.synonym(word))
        antonym = (dictionary1.antonym(word))

        await ctx.channel.send(f"""
The word = {word}

Noun of {word} -  {noun[0]}
Verb of {word} -  {verb[0]}
Synonyms of {word} - {synonym[0]}, {synonym[1]}, {synonym[2]}
Antonyms of {word} - {antonym[0]}, {antonym[1]}, {antonym[2]}
        """)
    except:
        await ctx.channel.send("Sorry, The word you typed is invalid. Try again")

@client.command()
async def evil(ctx):
    ''' To rickroll someone from the server, using imgur.com 's embed video file'''
    await ctx.channel.send("https://i.imgur.com/MxAE8Wp.mp4")

@client.command()
async def helpx(ctx):
    ''' bot help menu'''

    await ctx.channel.send("""

Hello there, How you doin!
iam sus bot pro, the latest version of sus bot with more intresting features

-------  Menu   -------

-{'always use a dot "." before your commands'}-

.qq {question}  =-= to ask any yes or no questions to the bot

.movie {movie name} =-= to get a movie details

.word {word} =-= to get a word's details from dictionary

.tod {'t' ot 'd'}  =-= Truth or dare game

.math x ? y  =-= to do basics math operations, (eg - .math 2 + 2)

.clear =-= to clear 5 messages from the chat, you can change the value from 0-5

.kick  =-= to kick someone from the server. 

.ping =-= to check your internet ping in ms

.evil  =-= find out whats that is

.helpx  =-= for help
    """)



client.run("Your Bot's Token from discrod Dev Portal") # bot token. to run the bot
