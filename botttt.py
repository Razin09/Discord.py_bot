
''' basic discord bot using discord.py'''

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import random
import imdb
import time
import json
from PyDictionary import PyDictionary
from dadjokes import Dadjoke
import googletrans
from googletrans import Translator
import requests
from datetime import datetime
import pytz
import asyncio
import wikipedia



client = commands.Bot(command_prefix = ".")   # command prefix to call commands
slash = SlashCommand(client, sync_commands=True)  # using for Slash commands


@client.event
async def on_ready():
    ''' to print a message on the console when the bot is ready '''
    print("The bot is online")

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

@client.command(aliases = ["qq"])
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
async def dadjoke(ctx):
    # a dad joke command. using a Dadjoke API

    url = "https://dad-jokes.p.rapidapi.com/random/joke/png"
    headers = {
        'x-rapidapi-key': "e7875e7294mshd3acf8547625a85p117ba0jsn09f03bb4ce3c",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    joke_body = (response.json()['body'])     # body
    joke_setup = (joke_body['setup'])              # setup
    joke_punchline = joke_body['punchline']        # punchline

    await ctx.channel.send('here is an dad joke for ya... ***evil laugh***')
    await asyncio.sleep(2)
    await ctx.channel.send(joke_setup)                         # pass joke setup
    await asyncio.sleep(6)
    await ctx.channel.send(joke_punchline)                     # pass joke punchline

@client.command()
async def love(ctx, fname, sname,):
    '''
    a love percentage calculator
    using an API from rapid api
    '''
    url = "https://love-calculator.p.rapidapi.com/getPercentage"
    querystring = {"fname": fname, "sname": sname}

    headers = {
        'x-rapidapi-key': "e7875e7294mshd3acf8547625a85p117ba0jsn09f03bb4ce3c",
        'x-rapidapi-host': "love-calculator.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json = (response.json())
    fname = json['fname']
    sname = json['sname']
    perc = json['percentage']
    result = json['result']
    await asyncio.sleep(1)
    await ctx.channel.send(f'first name = {fname}')        # fname
    await asyncio.sleep(1)
    await ctx.channel.send(f'second name = {sname}')       # sname
    await asyncio.sleep(2)
    await ctx.channel.send(f'love percentage = {perc}')    # percentage
    await asyncio.sleep(1)
    await ctx.channel.send(f'and ill say that = {result}') # result based on the result

@client.command()
async def tod(ctx, td):
    '''
    basic truth or dare game.
    it'll ask a truth or dare from the truths,dares list.
    you just need to pass t or d after the command.
    '''

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
    moviesDB = imdb.IMDb()  # imdb api, using to get movie data stright from imdb

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
    dictionary1 = PyDictionary()
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

@client.command(aliases=['tr'])
async def translate(ctx, lang_to, *args):
    lang_to = lang_to.lower()

    if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
        await ctx.channel.send("Inavlid language to translate")
    text = ' '.join(args)
    trans = googletrans.Translator()
    text_trans = trans.translate(text, dest=lang_to).text
    await ctx.channel.send(f'''
Text = {text}

translate to '{lang_to}' =  {text_trans}
''')

@client.command()
async def mp3(ctx,url):
    '''
    this command will convert a youtube video to an mp3 audio
    itll give us the audio download link and we can directly download it from there
    used an mp3 converter API from rapidapi
    '''

    url_for_id = "https://youtube-mp36.p.rapidapi.com/dl"

    content_id = url[32:]   # we only needed the watch id from the youtube link. so we just needed this

    querystring = {"id": content_id}

    headers = {
        'x-rapidapi-key': "e7875e7294mshd3acf8547625a85p117ba0jsn09f03bb4ce3c",
        'x-rapidapi-host': "youtube-mp36.p.rapidapi.com"
    }

    response = requests.request("GET", url_for_id, headers=headers, params=querystring)

    mp3_link = (response.json()['link'])         # to get the mp3 download link
    mp3_title = (response.json()['title'])       # to get the title

    await ctx.channel.send(f'''
title of the video = {mp3_title}

mp3 download link  = {mp3_link}

''')

@client.command()
async def image(ctx, content, *args):
    '''
    image searcher.
    this command will give us the image of the content passed
    eg - .image car = this will sent us 2 car images from online
    used bing image api
    '''

    content_arg = ' '.join(args)
    url = "https://bing-image-search1.p.rapidapi.com/images/search"
    querystring = {"q": content_arg}   # content search

    headers = {
        'x-rapidapi-key': "e7875e7294mshd3acf8547625a85p117ba0jsn09f03bb4ce3c",
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    '''
    some images are not passable.
    so it'll show us and index erorr.   
    '''
    try:
        result = (response.json())
        value = (result['value'])
        img_one = (value[0]['thumbnailUrl'])
        img_two = (value[1]['thumbnailUrl'])
        await ctx.channel.send(img_one)            # image one
        await ctx.channel.send(img_two)            # image two
    except IndexError:
        await ctx.channel.send("Sorry, invalid image to search. Try again with another content")

@client.command()
async def time(ctx):
    # IST
    tz_IN = pytz.timezone('Asia/Kolkata')
    datetime_IN = datetime.now(tz_IN)
    # HST
    tz_US_hw = pytz.timezone('US/Hawaii')
    datetime_US_hw = datetime.now(tz_US_hw)
    # AKDT
    tz_US_al = pytz.timezone('US/Alaska')
    datetime_US_al = datetime.now(tz_US_al)
    # PDT
    tz_US_pa = pytz.timezone('US/Pacific')
    datetime_US_pa = datetime.now(tz_US_pa)
    # MDT
    tz_US_mt = pytz.timezone('US/Mountain')
    datetime_US_mt = datetime.now(tz_US_mt)
    # CDT
    tz_US_ct = pytz.timezone('US/Central')
    datetime_US_ct = datetime.now(tz_US_ct)
    # EDT
    tz_US_et = pytz.timezone('US/Eastern')
    datetime_US_et = datetime.now(tz_US_et)
    # TRT
    tz_EU_tur = pytz.timezone('Europe/Istanbul')
    datetime_EU_tur = datetime.now(tz_EU_tur)

    await ctx.channel.send(datetime_IN.strftime("Indian Standard Time     - %Y-%m-%d %I:%M:%p %Z"))
    await ctx.channel.send(datetime_US_hw.strftime("Hawaii Standard Time     - %Y-%m-%d %I:%M:%p %Z"))
    await ctx.channel.send(datetime_US_al.strftime("Alaska Daylight Time     - %Y-%m-%d %I:%M:%p %Z"))
    await ctx.channel.send(datetime_US_pa.strftime("Pacific Time             - %Y-%m-%d %I:%M:%p %Z"))
    await ctx.channel.send(datetime_US_mt.strftime("Mountain Time            - %Y-%m-%d %I:%M:%p %Z"))
    await ctx.channel.send(datetime_US_ct.strftime("Central Time             - %Y-%m-%d %I:%M:%p %Z"))
    await ctx.channel.send(datetime_US_et.strftime("Eastern Time             - %Y-%m-%d %I:%M:%p %Z"))
    await ctx.channel.send(datetime_EU_tur.strftime("Turkey Time              - %Y-%m-%d %I:%M:%p TRT"))

@client.command()
async def covid(ctx, enter_country):
    '''
    this command will show us the covid cases on individual country's
    pass the country name on enter_country
    ussed covid-19 offical API
    '''

    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"name": enter_country}

    headers = {
        'x-rapidapi-key': "e7875e7294mshd3acf8547625a85p117ba0jsn09f03bb4ce3c",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    country = response.json()[0]['country']
    code = response.json()[0]['code']
    confirmed = response.json()[0]['confirmed']
    recovered = response.json()[0]['recovered']
    critical = response.json()[0]['critical']
    deaths = response.json()[0]['deaths']
    last_update = response.json()[0]['lastUpdate']

    await ctx.channel.send(f"""
country = {country}.{code}
    
confirmed cases = {confirmed}
critical cases  = {critical}
recovered cases = {recovered}
deaths          = {deaths}

last update = {last_update}
    """)

# @client.command()
# async def gold(message, ara = None):
#     ara = message.author
#     print(ara)
#     await ara.send('https://en.wikipedia.org/wiki/Gold')

@client.command()
async def rate(ctx, amount, amount_from, ara, amount_to,):
    '''
    Currency exchanger command.
    the command capable of delivering real-time exchange rate data for 170 world currencies.
    eg  - .rate 12 USD to INR
    '''

    try:
        url = "https://fixer-fixer-currency-v1.p.rapidapi.com/convert"
        querystring = {"amount": amount, "to": amount_to, "from": amount_from}
        headers = {
            'x-rapidapi-key': "e7875e7294mshd3acf8547625a85p117ba0jsn09f03bb4ce3c",
            'x-rapidapi-host': "fixer-fixer-currency-v1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)

        result = response.json()['result']
        await ctx.channel.send(f"""
Currency exchange Amount = {amount}
from = {amount_from}
to = {amount_to}
    
result = {result}
        """)
    except:
        await ctx.channel.send("Invalid currency or command")

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

.tr {language} {text} =-= Translator, pass language and text to translate.
.covid {country}  =-=  covid case data's from individual country's
.qq {question}  =-= to ask any yes or no questions to the bot
.rate {X to Y} =-= delivering real-time exchange rate for 170 world currencies.
.movie {movie name} =-= to get a movie details
.mp3 {youtube video link} =-= Convert and download any YouTube video into 
.image {content}   =-= Image Searcher from bing
.word {word} =-= to get a word's details from dictionary
.time =-= to print different time zone's time
.tod {'t' ot 'd'}  =-= Truth or dare game
.love {fname} {sname} =-= a love percentage calculator
.dadjoke =-= bot will pass some dad jokes
.math x ? y  =-= to do basics math operations, (eg - .math 2 + 2)
.clear =-= to clear 5 messages from the chat, you can change the value from 0-5
.kick  =-= to kick someone from the server. 
.ping =-= to check your internet ping in ms
.evil  =-= find out whats that is
.helpx  =-= for help
    """)

@slash.slash(
    # add a name to the slash, this name will display when you type /
    name="wiki",
    # add the description to it
    description="Search anything on wikipedia",
    # you have to pass the guild ids
    guild_ids=[868506526002851861],
)
async def wiki_searcher(ctx: SlashContext, content):
    '''
    wikipedia searcher.
    it'll pass the page title, summary, readmore url etc
    function name isn't matters for this.
    '''
    await ctx.send(f'Searching for {content} ...')
    try:
        page = wikipedia.page(content)
        sum = page.summary
        title = page.title
        url = page.url
        image = page.images[0]
        await ctx.channel.send(f"""
- {title} -

{sum[0:400]}....click here to read more {url}
""")
    except:
        await asyncio.sleep(1)
        await ctx.channel.send('Searching failed. try again with another content')

@slash.slash(
    name="covid",
    description="get covid stats for a country",
    guild_ids=[868506526002851861],
)

async def covid_searcher(ctx:SlashContext, country):
    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"name": country}

    headers = {
        'x-rapidapi-key': "e7875e7294mshd3acf8547625a85p117ba0jsn09f03bb4ce3c",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    country = response.json()[0]['country']
    code = response.json()[0]['code']
    confirmed = response.json()[0]['confirmed']
    recovered = response.json()[0]['recovered']
    critical = response.json()[0]['critical']
    deaths = response.json()[0]['deaths']
    last_update = response.json()[0]['lastUpdate']

    embed = discord.Embed(title=f'COVID-19 Statistics for {country}', description=f'{code}',color=0x50f2a9)
    embed.set_author(name='sus')
    embed.set_thumbnail(url='https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png')
    embed.set_footer(text='stay home, stay safe')

    embed.add_field(name='Cases',value=confirmed,inline=True)
    embed.add_field(name='Deaths',value=deaths,inline=True)
    embed.add_field(name='Recovered',value=recovered,inline=True)
    embed.add_field(name='Critical cases ',value=critical,inline=True)
    embed.add_field(name='Code',value=code,inline=True)
    embed.add_field(name='Last update',value=last_update,inline=False)

    await ctx.send(embed=embed)


#     await ctx.send(f"""
#     country = {country}.{code}
#
# confirmed cases = {confirmed}
# critical cases  = {critical}
# recovered cases = {recovered}
# deaths          = {deaths}
#
# last update     = {last_update}
#         """)

@slash.slash(
    name="ping",
    description="Get your internet ping in ms",
    guild_ids=[868506526002851861],
)

async def xping(ctx):
    _ping = (f"your ping is {round(client.latency * 1000)} ms")

    myEmbed = discord.Embed(title="Ping in ms", description='to check your internet ping', color=0xe68f39)
    myEmbed.add_field(name='Ping:', value=_ping, inline= True)
    myEmbed.set_footer(text='by sus bot pro')
    await ctx.send(embed=myEmbed)


client.run('bot token') # bot token. to run the bot
