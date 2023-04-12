import discord
import omegle
import obs
import datetime

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} logged in now!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    # obs.connect_obs()

    or_leader = discord.utils.get(message.guild.roles, id=1038159176754540684)
    vc_helper = discord.utils.get(message.guild.roles, id=984896261121507398)

    # VC Helper or Outreach Leader Commands
    if msg.startswith('!omeglebotjoin'):
        channel = message.author.voice.channel
        await channel.connect()
        print(f"{timestamp} - Bot Joined {message.author.voice.channel} by {message.author}")

    if msg.startswith('!cam'):
        obs.toggle_cam()
        await message.channel.send("Toggled Cam")
        print(f"{timestamp} - Toggled Cam by {message.author}")

    # General User Commands
    if msg.startswith('!help'):
        await message.channel.send("""
Command Help - !help
Toggle Title - !t
Toggled Cruelty - !c
Toggle Vegan Food - !f
Toggle GameChangers - !g
Click Skip - !s""")
        print(f"{timestamp} - Help Requested by {message.author}")

    if msg.startswith('!t'):
        obs.toggle_title()
        await message.channel.send("Title Changed")
        print(f"{timestamp} - Title Changed by {message.author}")

    if msg.startswith('!g'):
        obs.toggle_gamechangers()
        await message.channel.send("Toggled Game Changers")
        print(f"{timestamp} - Toggled Game Changers by {message.author}")

    if msg.startswith('!f'):
        obs.toggle_food()
        await message.channel.send("Toggled Vegan Food")
        print(f"{timestamp} - Toggled Vegan Food by {message.author}")

    if msg.startswith('!c'):
        obs.cruelty()
        await message.channel.send("Toggled Cruelty")
        print(f"{timestamp} - Toggled Cruelty by {message.author}")

    if msg.startswith('!s'):
        omegle.stop()
        await message.channel.send("Clicked Skip")
        print(f"{timestamp} - Clicked Skip by {message.author}")

    ## May be used in future implementation

    # if msg.startswith('?startrec'):
    #     obs.start_recording()
    #     await message.channel.send("Recording Started")
    #     print(f"{timestamp} - Recording Started by {message.author}")
    #
    # if msg.startswith('?stoprec'):
    #     obs.stop_recording()
    #     await message.channel.send("Recording Stopped")
    #     print(f"{timestamp} - Recording Stopped by {message.author}")

client.run('TOKEN')