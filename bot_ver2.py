import discord
import key
from neuralintents import GenericAssistant
import nltk
from discord.utils import find


client = discord.Client()
embed = discord.Embed()
@client.event
async def on_ready():
    print("connected")




@client.event
async def on_guild_join(guild):
    embed.description = " @everyone \n Hello hoomans❤️ \n I am FFCS-BOT to help you with your FFCS doubts. \n Shoot your questions using the command -!vinny"

    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(embed=embed)
@client.event
async def on_message(message):
    if message.author == client.user:
        print(message.content)
        return
    if message.content.startswith("!vinny"):
        responce = chatbot.request(message.content[9:])
        print(message.content)
        await message.channel.send(responce)
    if message.content.startswith("!vinny ffcs"):
        await message.channel.send("1) FFCS (Fully Flexible Credit System) is a system which VIT follows to let its students choose the subjects they want to study and the teachers they want to study the subjects from. \n 2) You'll receive a mail regarding the alloted time slot. Try to login 2-3 seconds after the given time to prevent server crash.\n 3) To get same faculty , Sit together and keep your all the teachers together and next day while registering try your best to register the same. Try to select teachers that the crowd will not prefer but will be good enough. Its all about luck here.")
    if message.content.startswith("!vinny thanks" or "!vinny thank you"):
        await message.channel.send("happy to serve you😊😊")





if __name__=="__main__":
    nltk.download("omw-1.4")
    chatbot = GenericAssistant("intents.json")
    chatbot.train_model()
    chatbot.save_model()
    print("model done training and saving")




    client.run(key.TOKEN)