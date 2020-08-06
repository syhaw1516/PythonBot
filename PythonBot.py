import discord,asyncio
from discord.ext import commands
import os,bs4,requests,random

bob = ["치킨","피자","햄버거","스파게티","짜장면","찜닭","닭도리탕","김치찌개","냉면","만두","떡볶이","김밥","튀김","국수","돈까스","카레","초밥","족발","보쌈","탕수육","삼겹살","갈비","샌드위치","부대찌개"]
game = discord.Game("!도움말")
bot = commands.Bot(command_prefix='!',status=discord.Status.online,activity=game)

token_path = os.path.dirname(os.path.abspath(__file__) )+"/token.txt"
t = open(token_path,"r",encoding="utf-8")
token = t.read().split()[0]
print("Token_key :",token)

@bot.event
async def on_ready():
    print('봇 시작')
    return

@bot.event
async def on_message(message):
    if message.author == bot.user:  
        return

    if message.content.startswith('!도움말'):
        await message.channel.send("```Python Boy 명령어\n 1. !도움말 - 명령어를 보여줍니다.\n 2. 추가 예정 ``` \n")

    if message.content.startswith('!밥'):
        i =  random.randint(0,22)
        await message.channel.send(f"```\n 오늘은 {bob[i]}어떠신가요?\n```")

    if message.content.startswith('!ping'):
        latancy = bot.latency
        await message.channel.send(f'```Pong! {round(latancy*1000)}ms 입니다.```')
bot.run(token)