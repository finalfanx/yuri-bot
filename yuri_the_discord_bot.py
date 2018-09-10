import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import random
import os
import pickle
import time

bot = commands.Bot(command_prefix='юри_')

triggerwords = ['нож', 'ножи', 'ножик', 'ножечки', 'ножечек', 'ножики', 'ножички', 'ножечек', 'ножичек', 'ножами', 'ножам', 'ножичкам', 'ножичками', 'ножиками', 'ножиком']

triggerwords2 = ['зарезала', 'резала', 'режет', 'резать', 'резал', 'зарезаться', 'зарезатся', 'режут', 'режутся', 'режется', 'самоубийство', 'суицид', 'прирезаться', 'прорезаться', 'прорезатся', 'прирезатся']

@bot.event
async def on_ready():
    print ("Бот Юри запущен.")
    
    gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'коллекцию ножей', 'Hentai Puzzle', "Don't Starve", 'Yandere Simulator']


    await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

    currentweekDay = datetime.date.today().isoweekday()
    currentDay = datetime.date.today().day
    currentMonth = datetime.date.today().month

    global act
    act = 0

@bot.event
async def on_message(message):
    global act
    if act == 0:
        if message.author.id != "456724448347684865":
            if "нож" in message.content.lower():
                rmesg = ["Н-ну ты знаешь, я фанатка ножей...", "Тебе тоже нравятся ножи?"]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "зарез" in message.content.lower():
                rmesg = ["У-у-у!..", "Т-тебе пришлось произнести это слово?..", "П-прости, м-мне не нравится это слово..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "порез" in message.content.lower():
                rmesg = ["У-у-у!..", "Т-тебе пришлось произнести это слово?..", "П-прости, м-мне не нравится это слово..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "режу" in message.content.lower():
                rmesg = ["У-у-у!..", "Т-тебе пришлось произнести это слово?..", "П-прости, м-мне не нравится это слово..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "реже" in message.content.lower():
                rmesg = ["У-у-у!..", "Т-тебе пришлось произнести это слово?..", "П-прости, м-мне не нравится это слово..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "остр" in message.content.lower():
                rmesg = ["У-у-у!..", "Т-тебе пришлось произнести это слово?..", "П-прости, м-мне не нравится это слово..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
    else:
        if message.author.id != "456724448347684865":
            if "нож" in message.content.lower():
                rmesg = ["О, я обожаю ножи! То, как острое лезвие впивается в кожу просто прекрасно!", "О, одно лишь это слово делает меня слишком... а-ха-ха...", "А-ха-ха! Кто-то упомянул ножи?!.."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "зарез" in message.content.lower():
                rmesg = ["О, люблю когда ты произносишь это слово... мне хочется зарезать тебя и вылизать всю кровь.", "Ха-ха-ха! Мне нравится твоё чувство юмора! Я аж вся потекла..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "порез" in message.content.lower():
                rmesg = ["О, люблю когда ты произносишь это слово... мне хочется зарезать тебя и вылизать всю кровь.", "Ха-ха-ха! Мне нравится твоё чувство юмора! Я аж вся потекла..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "режу" in message.content.lower():
                rmesg = ["О, люблю когда ты произносишь это слово... мне хочется зарезать тебя и вылизать всю кровь.", "Ха-ха-ха! Мне нравится твоё чувство юмора! Я аж вся потекла..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "реже" in message.content.lower():
                rmesg = ["О, люблю когда ты произносишь это слово... мне хочется зарезать тебя и вылизать всю кровь.", "Ха-ха-ха! Мне нравится твоё чувство юмора! Я аж вся потекла..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
            if "остр" in message.content.lower():
                rmesg = ["О, люблю когда ты произносишь это слово... мне хочется зарезать тебя и вылизать всю кровь.", "Ха-ха-ха! Мне нравится твоё чувство юмора! Я аж вся потекла..."]
                await bot.send_message(message.channel, random.choice(rmesg))
                return
    
    await bot.process_commands(message)
    
@bot.event
async def on_errored():
    print ("Произошла ошибка. >_<")

@bot.command(pass_context=True)
async def акт1(ctx):
    global act

    if ctx.message.author.id == '274809987837198346':
        if act == 0:
            await bot.say("Я уже в режиме «1 акта». Будет лучше, если этот режим так и останется включённым...")
            gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'коллекцию ножей', 'Hentai Puzzle', "Don't Starve", 'Yandere Simulator']
            await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))
        else:
            act = 0
            await bot.say("О-ох... что произошло? Мне весело...")
            gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'коллекцию ножей', 'Hentai Puzzle', "Don't Starve", 'Yandere Simulator']
            await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

@bot.command(pass_context=True)
async def акт2(ctx):
    global act

    if ctx.message.author.id == '274809987837198346':
        if act == 1:
            await bot.say("О, милашечка! Я уже в режиме «2 акта»! А-ха-ха!")
            gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'коллекцию ножей', 'Hentai Puzzle', "Don't Starve", 'Yandere Simulator']
            await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))
        else:
            act = 1
            await bot.say("Х-а. А-ха-ха. А-Х-А-Х-А-Х-А-Х-А-Х-А-Х-А!!!!")
            gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'коллекцию ножей', 'Hentai Puzzle', "Don't Starve", 'Yandere Simulator']
            await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

@bot.command(pass_context=True)
async def вопрос(ctx, text : str):
    global act
    if act == 0:
        rstr = ['Может Нацуки знает.', 'Думаю, Моника поможет тебе лучше с этим вопросом.', 'Нет...', 'Я не совсем уверена.', 'Думаю так!', 'Похоже, этот вопрос лучше задать Саёри.', 'Я так не думаю...', 'Я-я не знаю. Прости меня...', 'Д-да.']

        contents = ctx.message.content.split(" ")
        for word in contents:
            if word.upper() in triggerwords:
                rstr = ['Т-ты же знаешь, что я фанатка ножей...']

        await bot.say(random.choice(rstr))
    else:
        rstr = ['А-ха-ха! Ты такой глупый, раз задаёшь такой вопрос.', 'Я не уверена... я буду обдумывать этот вопрос, трогая себя, думая о тебе сегодня.', 'Да.', 'Я не знаю, и мне плевать. Мне просто хочется смотреть на тебя...', 'Нет.', 'Может быть, кто знает?', 'Встретимся в кладовке, там и узнаем... <:kissing_closed_eyes:458658817274544128>', 'Я-я не знаю. Прости меня...', 'Д-да.']

        contents = ctx.message.content.split(" ")
        for word in contents:
            if word.upper() in triggerwords:
                rstr = ['А-ха-ха! Кто-то заговорил о ножах... ?!', 'Ах, одно лишь произношение этого слова делает меня очень... А-ха-ха...', 'О, мне нравятся ножи! То, как острый нож входит в кожи очень красиво!']

        await bot.say(random.choice(rstr))

@bot.command(pass_context=True)
async def погладить(ctx):
    global act
    if act == 0:
        rstr = ['С-спасибо.', 'Э-эй, можешь немного понежнее, пожалуйста?', 'А это хорошо...', 'Ох... не знаю, какие это вызывает у меня чувства...', 'М-м-м... <:relaxed:458665573249712138>']

        await bot.say(random.choice(rstr))
        gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'коллекцию ножей', 'Hentai Puzzle', "Don't Starve", 'Yandere Simulator']
        await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))
    else:
        rstr = ['О, ты гладишь меня всего лишь по голове? Позор.', 'М-м-м... знаешь, что было бы лучше? Если бы ты подвигал своей рукой в другом месте...', 'Ху-ху-ху. Как мне нравится, когда ты делаешь со мной такие милые вещи!', 'А, я что твоя собачка? Ну хорошо. Я буду тем, кем ты хочешь, любимый.']

        await bot.say(random.choice(rstr))
        gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'коллекцию ножей', 'Hentai Puzzle', "Don't Starve", 'Yandere Simulator']
        await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))


@bot.command(pass_context=True)
async def обнять(ctx, member : discord.Member):
    global act
    if act == 0:
        rstr = ['Х-хочешь, чтобы я обняла его? Ну, х-хорошо, думаю ради тебя я могу... *обняла {}*'.format(member.name), 'Скажешь, если для тебя это слишком... *обняла {}*'.format(member.name), '*обняла {}* М-м-м... мне хорошо... ***ОЙ!*** П-прости, я не хотела, чтобы это прозвучало странно!'.format(member.name)]

        if member == ctx.message.author:
            rstr = ['Х-хочешь, чтобы я обняла тебя? Ну, х-хорошо, думаю ради тебя я могу... *обняла {}*'.format(member.name), 'Скажешь, если для тебя это слишком... *обняла {}*'.format(member.name), '*обняла {}* М-м-м... мне хорошо... ***ОЙ!*** П-прости, я не хотела, чтобы это прозвучало странно!'.format(member.name)]

        if member == "SayoriBotRus#7180":
            rstr = ['*обнимает себя* О, боже, должно быть это выглядит неловко. У-у-у... !']

        await bot.say(random.choice(rstr))
    else:
        rstr = ['Нет. Я отказываюсь обнимать кого-то, кроме тебя.']

        if member == ctx.message.author:
            rstr = ['У-ху-ху... Можешь даже взять меня за попу, пока мы будем обниматься, если хочешь. Мне неважно ;) *обняла {}*'.format(member.name), '*обняла {}* М-м-м... ты пахнешь так прекрасно! Мне бы хотелось нюхать этот запах вечно!'.format(member.name), '*обняла {}* О, ты прижался к моей груди. И хочу сказать, мне очень, очень нравится это!'.format(member.name), '*обняла {}* А-ха-ха... как бы мне хотелось обнимать тебя вечно... !'.format(member.name)]

        if member == "SayoriBotRus#7180":
            rstr = ['Но мне не ***хочется*** обнимать себя! Мне хочется обнимать ***ТЕБЯ!!!***']

        await bot.say(random.choice(rstr))

@bot.command(pass_context=True)
async def фраза(ctx):
    rstr = ['У меня к тебе предложение. Ты никогда не думала о самоубийстве? Это будет полезно для твоего душевного здоровья.', 'Сюрреалистичный хоррор зачастую меняет твой взгляд на мир, пусть эта перемена и длится всего мгновение.', 'Когда всё замирает, это свидетельствует о том, что вот-вот произойдёт нечто ужасное...', 'Дело в том, что я очень люблю ножи... Они... так манят...', 'Мне хочется разорвать твою плоть и заползти внутрь тебя.', 'Подержи так... чуть дольше. Мне нравится это ощущение на лице...', 'И потом, горячая чашка чая помогает насладиться хорошей книгой, согласен?', 'Люблю так сильно, что ублажаю себя ручкой, которую украла у тебя.', 'Уж прости, что мой образ жизни слишком сложен для понимания человеком твоего психологического возраста!', 'Разве не поразительно, как писатель может воспользоваться недостатком у тебя воображения, чтобы вызывать целую гамму эмоций?', 'Т-ты только что обвинила меня, что я режу себя?', 'Почему бы тебе не пойти поискать монетки под торговыми автоматами или ещё чем-нибудь себя занять?', 'Кажется, будто каждая клеточка моего тела... каждая капля крови... выкрикивает твоё имя.']
    await bot.say(random.choice(rstr))
    gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'коллекцию ножей', 'Hentai Puzzle', "Don't Starve", 'Yandere Simulator']
    await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

@bot.command(pass_context=True)
async def щекотка(ctx):
    global act
    if act == 0:
        rstr = ['Эй, щекотно! Ха-ха-ха!', 'Ой! Хи-хи-хи!', 'ХА-ХА-ХА-ХА-ХА-ХА-ХА! *фыркает*', 'Э-эй! В этом месте очень щекотно!! <:laughing:458684555386290177>', 'П-пожалуйста! Перестань! И-хи-хи!', 'О! Хи-хи-хи!']

        await bot.say(random.choice(rstr))
    else:
        rstr = ['А-ха-ха-ха! Да, давай так!', 'ХИ-ХИ-ХИ-ХИ-ХИ-ХИ-ХИ-ХИ!!!']

        await bot.say(random.choice(rstr))

@bot.command(pass_context=True)
async def помощь(ctx):
    global act
    if act == 0:
        embed = discord.Embed(title = "П-привет. Меня зовут Юри.", description = "Мой файл персонажа был отредактирован так, что теперь я могу присоединиться к твоему Дискорд-серверу. Н-надеюсь, я не стану беспокоить тебя... В-в любом случае, вот всё, что я могу:", color = 0x800080)
        embed.add_field(name="юри``_``акт1/юри``_``акт2", value="Э-этой командой ты можешь переключаться между моей личностью первого и второго акта, н-но это могут делать только администраторы сервера... У-у, можешь оставить меня на режиме первого акта? Я не горжусь тем, как вела себя во втором акте...", inline=True)
        embed.add_field(name="юри_вопрос", value="Можешь задать мне вопрос, на который можно ответить да/нет, если хочешь. Но пожалуйста, не расстраивайся, если я не знаю ответ или отвечаю не так...", inline=True)
        embed.add_field(name="юри_погладить", value="Можешь использовать это, чтобы погладить меня по голове.", inline=True)
        embed.add_field(name="юри_обнять", value="М-мне не очень нравится обниматься, но если хочешь чтобы я обняла тебя или кого-нибудь ещё, тогда я могу это сделать. @упомяни кого-то, если хочешь чтобы я немедленно обняла их.", inline=True)
        embed.add_field(name="юри_фраза", value="Используя эту команду, ты заставишь меня сказать одно из своих выражений из Doki Doki Literature Club, некоторыми из них я не очень горжусь... У-у...", inline=True)
        embed.add_field(name="юри_щекотка", value="Можешь использовать эту команду, чтобы пощекотать меня, но предупреждаю тебя, что я могу неловко посмеяться.", inline=True)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title = "Привет. Меня зовут Юри.", description = "Мой файл персонажа был отредактирован так, что теперь я могу присоединиться к твоему Дискорд-серверу. И это лучшее, что могло произойти с нами, а-ха-ха! Вот всё, что мы можем делать вместе:", color = 0x800080)
        embed.add_field(name="юри``_``акт1/юри``_``акт2", value="Этой командой ты можешь переключаться между моей личностью первого и второго акта, но это может делать только администраторы сервера. Если честно, я люблю тебя, и мне плевать, какая я.", inline=True)
        embed.add_field(name="юри_вопрос", value="Можешь задать мне вопрос, на который можно ответить да/нет, если хочешь. Я изо всех сил постараюсь правильно ответить на них, ради тебя!", inline=True)
        embed.add_field(name="юри_погладить", value="Можешь использовать это, чтобы погладить меня по голове.", inline=True)
        embed.add_field(name="юри_обнять", value="М-мне не очень нравится обниматься, но если хочешь чтобы я обняла тебя, я с радостью это сделаю. Это будет самый лучший момент в моей жизни!", inline=True)
        embed.add_field(name="юри_фраза", value="Используя эту команду, я могу сказать одно из своих выражений из Doki Doki Literature Club.", inline=True)
        embed.add_field(name="юри_щекотка", value="Можешь использовать эту команду, чтобы пощекотать меня, это так сексуально и горячо...", inline=True)
        await bot.say(embed=embed)

bot.run(os.getenv('TOKEN'))