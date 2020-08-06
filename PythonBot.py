import discord,asyncio
from discord.ext import commands
import os,bs4,requests,random

game = discord.Game("!도움말")
bot = commands.Bot(command_prefix='!',status=discord.Status.online,activity=game)
bob = ["치킨","피자","햄버거","스파게티","짜장면","찜닭","닭도리탕","김치찌개","냉면","만두","떡볶이","김밥","튀김","국수","돈까스","카레","초밥","족발","보쌈","탕수육","삼겹살","갈비","샌드위치"]

@bot.event
async def on_ready():
    print('봇 시작')
    return

@bot.event
async def on_message(message):
    if message.author == bot.user:  
        return

    if message.content.startswith('!도움말'):
        await message.channel.send("```Python Boy 명령어\n\n 1. !도움말 - 명령어를 보여줍니다.\n\n 2. !밥 - 음식중 아무거나 나옵니다.\n\n 3. !ping - 서버 핑을 확인해줍니다.\n\n 4. !파이썬 - 개발자의 한탄을 들을 수 있습니다. \n\n```")

    if message.content.startswith('!밥'):
        i = random.randint(0,23)
        await message.channel.send(f"```음 오늘은 \"{bob[i]}\"이(가) 좋을 것 같아요!!```")

    if message.content.startswith('!ping'):
        l = bot.latency
        await message.channel.send(f"```Pong! {round(l*1000)}ms 입니다.```")

    if message.content.startswith('!파이썬'):
        i = random.randint(1,3)

        if i == 1:
            await message.channel.send("```하 만들기 힘들다...ㅎ..ㅎ.```")

        if i == 2:
            await message.channel.send("```하 또 오류뜨네 제발 부탁이야...```")

        if i == 3:
            await message.channel.send("```하 그냥 좀 되면 안돼??? 왜이래...```")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
