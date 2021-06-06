#connect
token = ""
mess = [ "hi", "Привет", "ky", "ку", "здарова"]
otvet = ["Узнать информацию о сервере", "Команды", 'Админ панель']
yt = ['yt']
client = commands.Bot(command_prefix='$')
# $help

@client.event

async def on_ready():
    print('Ok')
    print("Please install Discord.py")
#commands
@client.command( pass_context = True)
async def hello(ctx):
    await ctx.send(f"Hello I bot GeffMine My created -> Games Dark")
@client.event
async def on_message(message):
    msg = message.content.lower()
    if msg in mess:
        await message.channel.send("Привет @everyone я бот GeffMine что хотел?")
async def on_message(message):
    await message in yt
    await message.channel.send('Ты не ютубер вероятность 50%')
client.run(token)