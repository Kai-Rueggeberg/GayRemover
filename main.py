import asyncio
import discord
from discord import Game
import SECRETS
import asyncio
import statics
import time

api = str(os.environ.get('RIOT_KEY'))

client = discord.Client()
global timestart
timestart = time.time()
DelList = []
print(timestart)


@client.event
@asyncio.coroutine
def on_ready():
    print("----------")
    print("GayRemover")
    print("----------")
    for s in client.servers:
        print(" - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name=",während er oboi fagotti zuschaut"))

@client.event
async def on_message(message):
    # if message.content.startswith(statics.PREFIX):
    #print(message.author.id)
    timestart = (time.time() + (statics.SLEEP - statics.COOLDOWN))

    if message.author.id == "270904126974590976":

        DelList.append(message)
        print(DelList)
    if message.content == "%sclean" %(statics.PREFIX):

        DelList.append(message)
        print(DelList)
        if len(DelList) > 2:
            await client.delete_messages(DelList)
            embed = discord.Embed(title="GayRemover regelt die Lage:", description=("%s Nachrichten wurden gelöscht") %(len(DelList)), color=0x00FF0000)
            returnmsg = await client.send_message(message.channel, embed=embed)
            await asyncio.sleep(4)
            await client.delete_message(returnmsg)
            timestart = time.time()
            DelList[:] = []
        else:
            embed = discord.Embed(title="GayRemover konnte die Lage nicht regeln:",
                                  description=("Keine Nachrichten wurden gelöscht"), color=0x00FF0000)
            returnmsg = await client.send_message(message.channel, embed=embed)
            await asyncio.sleep(4)
            await client.delete_message(returnmsg)

    if message.content.startswith("pls"):

        DelList.append(message)
        print(DelList)


async def cooldown():
    await client.wait_until_ready()
    while not client.is_closed:
        await asyncio.sleep(1)
        global timestart
        if time.time() >= timestart + statics.SLEEP:
            if len(DelList) > 2:
                await client.delete_messages(DelList)
                print("deleted")
            print("time over")
            timestart = time.time()


client.loop.create_task(cooldown())
client.run(SECRETS.TOKEN)
