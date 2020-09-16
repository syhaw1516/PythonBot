import discord,asyncio,datetime
from discord.ext import commands
import os,bs4,requests,random
from urllib.request import urlopen, Request 
import urllib 
from test2 import*
from test3 import*


game = discord.Game("/도움말")
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

    if message.content.startswith('/도움말'):
        await message.channel.send("```Python Boy 명령어\n\n 1. /도움말 - 명령어를 보여줍니다.\n\n 2. /밥 - 음식중 아무거나 나옵니다.\n\n 3. /ping - 서버 핑을 확인해줍니다.\n\n 4. /파이썬 - 개발자의 한탄을 들을 수 있습니다. \n\n 5. /오배 - 오늘의 배그 각을 알려줍니다.(그냥 만듬 심심해서) \n\n 6. /오서 - 오늘의 서든 각을 알려줍니다.(그냥 만듬 심심해서) \n\n 7. /오급 - 오늘의 급식을 알려줍니다. \n\n 8. /내급 - 내일의 급식을 알려줍니다.\
    \n\n 9. /날씨 - 날씨를 알려줍니다. 단,AA시,AA동,AA구 가 하나씩 밖에 입력이 안됩니다. 수정중! \n\n 10. /개발자 - 개발자 연락처를 통해 추가사항을 요청할 수 있습니다.```")

    if message.content.startswith('/밥'):
        i = random.randint(0,23)
        await message.channel.send(f"```음 오늘은 \"{bob[i]}\"이(가) 좋을 것 같아요!!```")

    if message.content.startswith('/ping'):
        l = bot.latency
        await message.channel.send(f"```Pong! {round(l*1000)}ms 입니다.```")

    if message.content.startswith('/파이썬'):
        i = random.randint(1,4)

        if i == 1:
            await message.channel.send("```하 만들기 힘들다...ㅎ..ㅎ.```")

        if i == 2:
            await message.channel.send("```하 또 오류뜨네 제발 부탁이야...```")

        if i == 3:
            await message.channel.send("```하 그냥 좀 되면 안돼??? 왜이래...```")
        
        if i == 4:
            await message.channel.send("```많이 사용해주면... 좀 많이 기쁠지도..(O.O)```")

    if message.content.startswith('/오배'):
        i =  random.randint(1,2)
        if i == 1:
            await message.channel.send(f'```나쁘지않아 각이야 가즈아ㅏㅏㅏㅏㅏㅏㅏㅏ```')

        if i == 2:
            await message.channel.send(f'```음 오늘은 좀 아닌듯 그냥 자자 에휴...```')

    if message.content.startswith('/오서'):
        i =  random.randint(1,2)
        if i == 1:
            await message.channel.send(f'```나쁘지않아 각이야 가즈아ㅏㅏㅏㅏㅏㅏㅏㅏ```')

        if i == 2:
            await message.channel.send(f'```음 오늘은 좀 아닌듯 그냥 자자 에휴...```')
            
    if message.content.startswith("/오급"):
        utcnow= datetime.datetime.utcnow()
        time_gap= datetime.timedelta(hours=9)
        kor_time= utcnow+ time_gap
        date = kor_time
        day = date
        year = day.strftime("%y%y")
        mon = day.strftime("%m")
        da = day.strftime("%d")
        today = f"{year}년 {mon}월 {da}일자 급식"
        meal = get_diet(2, day.strftime("%y%y.%m.%d"), day.weekday())
        embed=discord.Embed(title="세명컴고 오늘의 급식", color=0x00ff56)
        embed.set_author(name=f"{today}")
        embed.add_field(name="중식", value=f"{meal}", inline=True)
        embed.set_footer(text="맛있겠당..")
        await message.channel.send(embed=embed)

    if message.content.startswith("/내급"):
        utcnow= datetime.datetime.utcnow()
        time_gap= datetime.timedelta(hours=9)
        kor_time= utcnow+ time_gap
        date = kor_time
        day = date + datetime.timedelta(days=1)
        year = day.strftime("%y%y")
        mon = day.strftime("%m")
        da = day.strftime("%d")
        today = f"{year}년 {mon}월 {da}일자 급식"
        meal = get_diet(2, day.strftime("%y%y.%m.%d"), day.weekday())
        embed=discord.Embed(title="세명컴고 내일의 급식", color=0x00ff56)
        embed.set_author(name=f"{today}")
        embed.add_field(name="중식", value=f"{meal}", inline=True)
        embed.set_footer(text="맛있겠당..")
        await message.channel.send(embed=embed)

    if message.content.startswith('/개발자'):
        await message.channel.send("```연락처\nDISCORD DM : 소금감자#0332\n 이메일 : syhaw@naver.com\n 뭐넣을지 모르겠다...```")

    if message.content.startswith("/날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.green()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태



        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
