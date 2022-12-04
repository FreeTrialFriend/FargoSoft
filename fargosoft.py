from secrets import secre
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

#QUOTE LIST
import quotes

#ERRORS FOR FARGOSOFT
from fargoErrors import *

#WIKI
from req import Summarize

#SERVERSTATS
from gpiozero import CPUTemperature
import psutil

#NLTK CORPUS, SNOWBALL STEMMER, AND STOPWORDS
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

#OTHER SHIT
import math
import json
import traceback
import time
import os
import sys
from PIL import ImageOps
import numpy as np
import random
from PIL import Image, ImageDraw
import numpy as np
from io import BytesIO

#DISCORD SHIT
import discord
from discord import *
from discord.ext import *
from discord.utils import *
from discord.ext import commands
import asyncio
from discord import embeds, Embed
from discord import Option



gglKEY  = 'AIzaSyCg1Ukj8QP6BKxPiKxNYqcw4Z2JHiIb5Tc'
gglCX   = 'cx=e58bca19c3ab34051'


def deductCC(amount: int, user):
    username = user
    with open('/home/pi/FargoSoft/json/cringecoin.json','r') as f:
        dic = json.load(f)
        print(dic)
    cc = int( dic[username]["cringecoin"] )
    cc-= amount
    with open('/home/pi/FargoSoft/json/cringecoin.json','w') as f:
        json.dump(dic, f, indent=4)  
    
def checkCC(amount: int, user):
    username = user
    with open('/home/pi/FargoSoft/json/cringecoin.json','r') as f:
        dic = json.load(f)
        
    CC = int(dic[username]["cringecoin"])
    if CC >= amount:
        
        deductCC(amount, user)
    else:
        raise FundsError
    


bwords = [
    ("nigger", 'None'),
    ("niggers", 'None'),
    ("nigga", 'None'),
    ("niggas", 'None'),
    ("chink", 'None'),
    ("chinks", 'None'),
    ("kike", "Banker"),
    ("kikes", "Banker"),
    ("retard", "Genius"),
    ("retards", "Genius"),
    ("retarded", "Genius"),
    ("cunt", 'Irish'),
    ("cunts", 'Irish'),
    ("fag", "Fruity"),
    ("fags", "Fruity")
]

class text_processing:  
    def __init__(self, stemmer):
        self.stemmer = stemmer
    
    stemmer = SnowballStemmer("english")
    def snowball_stemming(text):
        new_text = []
        for word in text.split():
            global stemmer
            new_text.append(stemmer.stem(word))
        return ' '.join(new_text)

    def eliminate_low_feature_words(text):
        text_set = set(text.split()) - (set(stopwords.words('english')) - {'she', 'her', 'herself', 'himself', 'he', 'him'})
        return ' '.join(text_set)

    def remove_punctuation(text):
        for punctuation in ['@',',', '.', '!', ':', ';', '/', '"','`', '(',')','[',']','{','}',",",'%','+','-','_','=','*','&','#','$','^','>','<','?']:
            text = text.replace(punctuation, '')
            return text
            



intents = discord.Intents.all()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='&', intents = intents)


helpcmd = discord.SlashCommandGroup("help")



ccjson = '/home/pi/FargoSoft/json/cringecoin.json'
f = open(ccjson)

#bot.remove_command('help')


#On Ready
@bot.event
async def on_ready():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    await bot.change_presence(activity=discord.Game(name="0r84nM4rk37.onion/gogogo"))


@bot.slash_command(name="nickname")
async def nickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')
@bot.slash_command(guild=796051838632853525, name="serverinfo")
async def serverinfo(ctx):
    
    cputemp = CPUTemperature()

# Getting % usage of virtual_memory ( 3rd field)
    await ctx.respond(f'RAM memory % used: {psutil.virtual_memory()[2]} \nRAM Used (GB): {psutil.virtual_memory()[3]/1000000000} \nCPU Temperature: {cputemp.temperature}')
# Getting usage of virtual_memory in GB ( 4th field)   
#@bot.slash_command(guild=796051838632853525,name="rig")



@bot.slash_command(guild=796051838632853525, name="wiki")
async def wiki(ctx, query):
    
    # getting suggestions
    
    try:
        
        result = Summarize(query)
    # #printing the result
    #print(i)
    except VagueError as e:
        
        await ctx.respond(e.message)
    else:
        
        await ctx.respond(Summarize(query))
        
    
    


@bot.slash_command(guild=796051838632853525, name="boob", description="booby pic")
async def boob(ctx):
     
    boobynumber = random.randint(0,69)
    if boobynumber == 69:
        await ctx.respond(file=discord.File(f"/home/pi/FargoSoft/images/bird.jpg"))
    else:
        await ctx.respond(file=discord.File("/home/pi/FargoSoft/images/booby.jpeg"))
    
@bot. slash_command(guild=796051838632853525, name='reset', description = "Resets the bot's server. (NOTE: /reset can ONLY be used by FargoSoft's creator.)")
async def reset(ctx):
     
    if ctx.author.id == 844314391863230504:
        
        with open('/home/pi/FargoSoft/json/cringecoin.json','r') as f:
            dic = json.load(f)
            

        dic["FargoSoft"]["wasResetLast"] = True
        dic["FargoSoft"]["resetchannelID"] = ctx.channel.id


        with open('/home/pi/FargoSoft/json/cringecoin.json','w') as f:
            json.dump(dic, f, indent=4)
            
        await ctx.delete()
        os.system("clear")
        os.execv(sys.executable, ['python'] + sys.argv)
    else: 
        await ctx.respond("/reset can only be used by FargoSoft's creator!")
    


@bot. slash_command(guild=796051838632853525, name="cringeclub")
async def server(ctx):
    embed = discord.Embed(title=f"The Cringe Club Info", description="Information of this Server", color=discord.Colour.blue())
    embed.add_field(name='🆔Server ID', value=f"796051838632853525", inline=True)
    embed.add_field(name='📆Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='👑Owner', value=f"{ctx.guild.owner.mention}", inline=True)
    embed.add_field(name='👥Members', value=f'{ctx.guild.member_count} Members', inline=True)
    embed.add_field(name='💬Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=True)
    embed.add_field(name='🌎Region', value=f'{VoiceRegion.us_east}', inline=True)
    embed.set_thumbnail(url=ctx.guild.icon.url) 
    embed.set_footer(text="⭐ • Fargo Soft")    
    
    await ctx.respond(embed=embed)


@bot.slash_command(guild=796051838632853525, name='quote', description='Returns a funny quote.')
async def quote(ctx):
        
    quotelist = quotes.quotes

    response = random.choice(quotelist)
    if not response.startswith("Fun Fact:"):
        await ctx.respond(f'Quote:  {response}')
    else:
        await ctx.respond(response)

@bot. slash_command(guild=796051838632853525, pass_context=True, name='role', description="Assigns a role to a user.")
async def role(ctx, 
                 user: discord.Option(discord.SlashCommandOptionType.user), 
                 role: discord.Option(discord.SlashCommandOptionType.role), 
):
     
    await user.add_roles(role)
    await ctx.respond(f"hey {user.mention}, {ctx.author.mention} has given you a role called: {role.name}")
    
@bot.slash_command(guild=796051838632853525, name='september', description="🎵Do you remember?🎶")
async def september(ctx):
    await ctx.channel.send("🎵Do you remember?🎶", file=discord.File('/home/pi/FargoSoft/images/911.png'))



async def list_search(ctx: discord.AutocompleteContext):
    """Return's A List Of Autocomplete Results"""
    your_list=[
                         'A Hammer 🔨',
                         'A Saw 🪚',
                         'A Bomb 💣',
                         'An Axe 🪓',
                         'A Gun 🔫',
                         'A Sword 🗡',
                         'A Knife 🔪',
                         'Lung Problems 🚬',
                         'Electricity 🔌',
                         'Pills 💊',
                         'COVID-19 (Basically The Flu But Democrats Profit From It) 🦠',
                         'The Jewish Laser 🪬📡',
                         'Residue From FargoSoft\'s Secret Meth Lab 🧪',
                         'A Bad Fever 🌡'
                        ]
    return your_list # from your database
    
@bot.slash_command(guild=796051838632853525, name="murder", description='"Murders" a user with a specified weapon.')
async def murder(ctx, 
                 targetuser: discord.Option(discord.SlashCommandOptionType.user), 
                 weapon:Option(str, "Which weapon to use...?", autocomplete=list_search)
                 
                 ):
    target = targetuser
    await ctx.channel.send(f'{target.mention} was murdered using {str(weapon)}.')
        
@bot.slash_command(guild=796051838632853525, name='backslash')
async def backslash(ctx):
     
    await ctx.respond('https://tenor.com/view/spongebob-wacky-bite-got-me-gif-16950691')

     
@bot.slash_command(guild=796051838632853525, name='slash')
async def slash(ctx):
    embed = discord.Embed(title='BTS ARMY')
    embed.set_footer(text='*literally*')
    await ctx.respond(embed=embed)
    await ctx.send('https://tenor.com/view/north-korea-march-army-parade-gif-22201364')


@bot.slash_command(guild=796051838632853525, name='dcsniper', description='Pew! Pew! Bye Bye @RandomPerson.')
async def dcsniper(ctx, user: discord.Member = None):
     
    if user is None:
        user = random.choice(ctx.channel.guild.members)
    if user != ctx.author:
        misshit = random.randint(0,100)
       
        if misshit < 33.33:
            mesg = f"Shot at {user.mention}, but missed."
            await ctx.channel.send(f"Shot at {user.mention}, but missed.")
        
        if misshit >= 33.33:
            mesg = f"Successfully sniped {user.mention}!!"
            await ctx.channel.send(f"Successfully sniped {user.mention}!!")

    else:
        mesg = (f"Sadly,{ctx.author.mention}, shot themselves.")
        await ctx.channel.send(mesg)

















@bot.slash_command(guild=796051838632853525, name='pickupline')
async def pickupline(ctx, user: discord.Member = None):
     
    if user == None:
        user = ctx.author
    pickuplibrary = [
        f"Hey, {user.mention}, are you a Muslim pilot? Because I'm crashing down in affection for you.",
        f"Hey, {user.mention}, they call it a twin bed for a reason.",
        f"Hey, {user.mention}, is your name Harry because you're not responding...",
        f"Hey, {user.mention}, are you a therapist because you are keeping my dick alive.",
        f"Hey, {user.mention}, are you Mickey Mouse because I think you'd like my hot diggity dog.",
        f"Hey, how much for {user.mention}?",
        f"Hey, {user.mention}, are you the future? Because you’re looking hopeless and bleak.",
        f"{user.mention}, you’re the thot that counts!",
        f"Are you a snack, {user.mention}? Because everyone eats you for fun.",
        f"Hey, {user.mention}, are you poop? Because even when you’re far away, I can smell you.",
        f"Hey, {user.mention}, did you fall from heaven? Because so did Satan.",
        f"Hey, {user.mention}, you dropped something. My standards.",
        f"The more I drink, the more beautiful you become. Cheers, {user.mention}!",
        f"A poem written for {user.mention}: *Roses are red, violets are blue. I have a gun, get in the van!*",
        f"{user.mention}! Come with me if you want to live!",
        f"""Drunk guy: *Hey! Wanna come back to my place and re-enact a rape scene?* \n 
        {user.mention}: *No, I don't want to!* \n 
        Guy: *That's the spirit!*"""

    ]
    response = random.choice(pickuplibrary)
    await ctx.respond(file=discord.File(response))


@bot.slash_command(guild=796051838632853525, name='shmexy', description='View a photo that will 100%' + ' guaranteed to make you erect.')
async def shmexy(ctx):
     
    
    response = f'/home/pi/FargoSoft/images/shmexy/{random.choice(os.listdir("/home/pi/FargoSoft/images/shmexy/"))}'

    await ctx.respond(file=discord.File(response))

@bot.slash_command(guild=796051838632853525, name='funnypic', description = "lol. funny picture.")
async def funnypic(ctx):
     
    response = f'/home/pi/FargoSoft/images/funnypic/{random.choice(os.listdir("/home/pi/FargoSoft/images/funnypic/"))}'
    await ctx.respond(file=discord.File(response))
    #print(response)


@helpcmd.command(guild=796051838632853525, name="general-help", description="Shows this Message \n**/help** [command: *Optional*]")
async def help(ctx, command=None):
     
    if not command:
        helptext=''
        cmdlist = []
        for command in bot.walk_application_commands():
            cmdlist.append(command.name)
        cmdlist.sort()
        for i in cmdlist:
            cmd1 = bot.get_application_command(i)
            helptext+=f"***{cmd1}*** \n ({cmd1.description})\n \n"
        embed = discord.Embed(title="HELP", description=helptext)
        embed.set_footer(text="For more info on a specific command, \nplease do /help [command]. \n")
        await ctx.respond(embed=embed)
    
    
    elif command:
        for cmd in bot.walk_application_commands():

            if cmd.name == command:
                embed=discord.Embed(title=f"/{cmd}", description = f"{cmd.description}", color=discord.Color.blue())
                await ctx.respond(embed=embed)

@bot.slash_command(guild=796051838632853525, name="micahtempo", description="returns an audio recording of <@665238927568928769>'s internal metronome.")
async def micahtempo(ctx):
     
    await ctx.respond(file=discord.File("/home/pi/FargoSoft/audio/micahtempo.mp3"))
    

@bot.slash_command(guild=796051838632853525, name='cancel', description="Wanna ruin someone's entire career for the foreseeable future?")
async def cancel(ctx, user: discord.Member = None):
     
    all_messages = []
    
    temporary = await ctx.respond("One moment, please.")
    
    for channel in ctx.guild.text_channels:
        async for message in channel.history(limit= 100):
            if user != None and message.author == user:
                all_messages.append(message)
                #print(message)
            elif user == None:
                all_messages.append(message)

                

    #print(len(all_messages)) 

    message_to_send = random.choice(all_messages)
    
    embed=discord.Embed(title=f"{message_to_send.author.name}", description =message_to_send.content, color=discord.Color.red())
    
    await temporary.delete()
    
    await ctx.respond(f'LOOK AT WHAT {message_to_send.author.mention} SAID:')
    await ctx.respond(embed=embed)
    await ctx.respond(f'THEY SHOULD BE CANCELED!!')



@bot. slash_command(guild=796051838632853525, name='ban')
@commands.has_role('Manager')

async def ban(ctx, user: discord.Member, *, reason=''):
    ctx.delete()
    id = user.id
    await user.ban(reason=reason)
    if reason:
        ctx.reply(f"Successfuly banned <@{user.id}> for reason: {reason}")

    else:
        ctx.reply(f"Successfuly banned <@{user.id}> for reason: N/A")


@bot.slash_command(guild=796051838632853525, name='morph', 
                   description="Morphs user's pfp into something better") 
@option("morphsuit", description="Choose your morphsuit", choices=["Wanted"])
async def morph(
    ctx,
    morphsuit: str,
    user: discord.Member = None):
     
    
    if user == None: 
        user = ctx.author
        
        
    
    
    pathtomorph = '/home/pi/FargoSoft/images/morph/morphsuits/'
    
    

    try:
        img = Image.open(f'{pathtomorph}{morphsuit.lower()}.png')
    except Exception as e:
        #print(e)
        await ctx.respond("Please choose a valid Morphsuit.", hidden = True)
        return
    
    
    data = BytesIO(await user.display_avatar.read())
    
    pfp = Image.open(data)
    
    pfp=pfp.resize((100,100))
    img.paste(pfp, (50,90))

    img.save('/home/pi/FargoSoft/images/morph.png')
    
    await ctx.respond(file=discord.File('/home/pi/FargoSoft/images/morph.png'))

"""
@bot.slash_command(guild=796051838632853525, name="play")
async def damnbro(ctx, query: str = "Never Gonna Give You Up - Rick Astly", link: str = 'https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT', Spotify: bool = True, YouTube: bool = False):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    vc = None"""

  
@bot.slash_command(guild=796051838632853525, name="damnbro")
async def damnbro(ctx, user: discord.Member =None):
     
    if user == None:
        await ctx.respond('*wheezes* DAMMMN BRO', file = discord.File('/home/pi/FargoSoft/audio/damnbro.mp3'))
    else:
        await ctx.respond(f'*wheezes* DAMMMN BRO {user.mention}', file = discord.File('/home/pi/FargoSoft/audio/damnbro.mp3'))
    
@bot.slash_command(guild=796051838632853525, name="ddos")    
async def ddos(ctx, user: discord.Member, *, message = 'L + BOZO + RATIO'):
     
    
    chance = random.randint(1,100)
    dtime=0
    if chance <=50: 
        dtime = 150 
        backfire = False 
    else: 
        dtime = 300
        backfire = True
    
    if user.id == bot.user.id: 
        if ctx.author.id != 844314391863230504:
            await ctx.respond("TRY ME BITCH!")
            await user.author.send("TRY ME BITCH!")
            backfire = True
            dtime = 600
        else:
            newchoice = random.randint(1,5)
            if newchoice == 3:
                backfire = False
    
    
    if backfire:
        await ctx.respond(f"lol! {ctx.author.mention} got backfired on lmaooo!!!")
        await user.send("Get backfired on lol")
    else:
        await ctx.respond("Success!")
        await user.send("Success!!")
    
    for i in range(1,dtime):

        if not backfire:
            await user.send(f"{message} {i}/{dtime}")
            
        else:
            if user.id != bot.user.id:
                await ctx.author.send(f"L + BOZO + RATIO + GET BACKFIRED ON {i}/{dtime}")
               
    for i in range(dtime,dtime*2):
    
        if not backfire:
            await user.send(f"L + BOZO + RATIO {i}/{dtime*2}")
            
        else:
            if user.id != bot.user.id:
                await ctx.author.send(f"L + BOZO + RATIO + GET BACKFIRED ON {i}/{dtime*2}")
                
    await ctx.author.send(f"Completed ddos-ing {user.mention}")
    


    

reviewwords = [
    "bitch",
    "bitches",
    "asshole",
    "assholes"
]
def getword(list, indexa, indexb = None):
    if indexb != None:  
        return list[indexa][indexb]
    else:
        return list[indexa]

#def 
returnlist = ""
for i in range(len(bwords)):
    returnlist += getword(bwords, i, 0)
    if getword(bwords,i,0) != "fags": returnlist += ",\n"
    
    
#print(returnlist)


@bot.slash_command(guild=796051838632853525, name="cringecoin")
async def cringecoin(ctx, user: discord.Member = None):
    with open('/home/pi/FargoSoft/json/cringecoin.json','r') as f:
            dic = json.load(f)
            

            
    if user is None:
        user = ctx.author
    username = user.name
    userobj = dic[username]
    cringecoinobj = userobj["cringecoin"]
    cringecoin = math.floor(cringecoinobj)
    
    if cringecoin <= 1:
        await ctx.respond(f"{user.mention} has `{cringecoin}` ₢inge₵oin")
    if cringecoin >=2:
        await ctx.respond(f"{user.mention} has `{cringecoin}` ₢inge₵oins")


#WATCHME
#"""

class MyView(discord.ui.View):
    @discord.ui.button(label="Proceed anyway", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        for child in self.children: # loop through all the children of the view
            child.disabled = True # set the button to disabled
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"```{returnlist}```", ephemeral=True)

    @discord.ui.button(emoji="❌",label="Cancel", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)

@helpcmd.command(name="moderation-help") # Create a slash command
async def strike(ctx):
    await ctx.respond("This command shows a string of words that will put a strike on you. Many of these words are extremely offensive and should not be repeated in any other context than to know what not to say. **By pressing the `Proceed` button, you are agreeing not to repeat any of these words** ***anywhere.***", view=MyView(), ephemeral=True) # Send a message with our View class that contains the button







bot.add_application_command(helpcmd)






@bot.event
async def on_member_join(member):
    
    #CRINGEJSON
    
    username = member.name
    userid = member.id
    dictionary={
            username: {
                    "userid": userid, 
                    "cringecoin": 100,
                    "strikes": 0,
                    "inserver": True
                }
        }
            
            
        
    with open('/home/pi/FargoSoft/json/cringecoin.json','r') as f:
        dic = json.load(f)

    dic.update(dictionary)

    with open('/home/pi/FargoSoft/json/cringecoin.json','w') as f:
        json.dump(dic, f, indent=4)
    #print("success on join")
    
    
    
    #NEWPERSON
    
    async def check(reactions, member):  # Our check for the reaction
      return member != bot.user
    user = member
    channel = bot.get_channel(796052781504528394)
    #channel = ctx
    data = BytesIO(await user.display_avatar.read())
    pfp = Image.open(data)
    img = Image.open('/home/pi/FargoSoft/images/welcome/miller.jpg')
    pfp=pfp.resize((177,177))
    img.paste(pfp, (171,128))
    img.save('/home/pi/FargoSoft/images/welcome/welcome.png')
    await channel.send("UHM, HELLOoOooO!! Welcome to the Cringe Club! You don't know my rules yet, so read them to know what is FORBIDDEN!", file=discord.File('/home/pi/FargoSoft/images/welcome/welcome.png'))

    channel = bot.get_channel(934945751908356106)
    msg = await channel.send(f"User {user.mention} would like to be verified. \n*Verify them?*")
    await msg.add_reaction('\N{THUMBS UP SIGN}')
    await msg.add_reaction('\N{THUMBS DOWN SIGN}')
    reaction = await bot.wait_for("reaction_add", check=check)  # Wait for a reaction
    await channel.send(f'{reaction[1].mention} has verified {user.mention}')
    
    await user.add_roles(get(bot.get_guild(796051838632853525).roles, name="Cringe"))
    await user.remove_roles(get(bot.get_guild(796051838632853525).roles, name="Unverified"))

    await msg.clear_reactions()
    await msg.delete()
    


@bot.event
async def on_member_remove(member):
    with open('/home/pi/FargoSoft/json/cringecoin.json','r') as f:
        dic = json.load(f)

    username = member.name
    userobj = dic[username]
    userobj["inserver"] = False
    
    with open('/home/pi/FargoSoft/json/cringecoin.json','w') as f:
        json.dump(dic, f, indent=4)

    #dictionary = dic
    #print("success on leave")
  
    

@bot.event
async def on_message(ctx):
    """
    #LOG
    #---------------------------------------------------------------------------
    # open the file in the write mode
        with open('/home/pi/FargoSoft/log.csv', 'a') as log:

    # create the csv writer
        
            isdm = False
            srvr = None
            chnl = None
            if isinstance(ctx.channel, discord.channel.DMChannel):
                isdm = True
                chnl = "DM Channel"
                srvr = " -- "
            elif isinstance(ctx.channel, discord.channel.TextChannel):
                isdm = False
                chnl = ctx.channel
                srvr = ctx.channel.guild
            
        # write a row to the csv file#
            
            log.write(f"{str(ctx.author.name)}, {str(srvr)}, {str(chnl)}, {str(ctx.content)}")
        # close the file
            #log.close()

            #log.write(f"\nCHANNEL: {ctx.channel}\nAUTHOR: {ctx.author}\n\n    {ctx.content}\n")
                    #except:
                    #    log.write(f"CHANNEL: DM's CHANNEL\nAUTHOR: {ctx.author}\n\nMESSAGE:    {ctx.content}")
            with open('/home/pi/FargoSoft/json/cringecoin.json','r') as f:
                    dic = json.load(f)
    """        

    with open('/home/pi/FargoSoft/json/cringecoin.json','r') as f:
        dic = json.load(f)


    msgcont = ctx.content
    if msgcont:
        for i in range(len(bwords)): 
            bword = getword(bwords, i, 0)
            #role = discord.utils.get(ctx.guild.roles, name=getword(bwords, i, 1))
            if bword in msgcont.lower(): #and role not in user.roles:
                msgcont = msgcont.replace(bword, getword(bwords, i, 1))
                if ctx.author != bot.user:
                    
                    await ctx.delete()
                    strikes = dic[ctx.author.name]["strikes"]# +1
                    if strikes +1 < 3:
                        dic[ctx.author.name]["strikes"] += 1
                        await ctx.author.send(f"This is your warning #{strikes+1}!! You only get three warnings. Once three warnings have been distributed, and you say something like this again... you WILL be unverified and stripped of all other roles. (for info on what you cannot say do `/help moderation-help`)")
                    
                    elif strikes+1 == 3:
                        dic[ctx.author.name]["strikes"] += 1
                        await ctx.author.send(f"This is your third and FINAL warning!! If you persist, you WILL be unverified and stripped of all other roles. (for info on what you cannot say do `/help moderation-help`)")
                    elif strikes+1 == 4:
                        dic[ctx.author.name]["strikes"] += 1
                        #roles.remove(everyone)
                        
                        await ctx.author.remove_roles(get(bot.get_guild(796051838632853525).roles, name="Cringe"))
                        await ctx.author.add_roles(get(bot.get_guild(796051838632853525).roles, name="Unverified"))

                    #ctx.send()
                        break
            else:
                pass
            
        
            
#CRINGEJSON
#---------------------------------------------------------------------------

    msgcont = ctx.content
    user = ctx.author
    
    username = user.name
    userobj = dic[username]
    if msgcont:
        userobj["cringecoin"] += 1
    
        if ctx.mentions:
            for i in ctx.mentions:
                targetid = ctx.mentions[ctx.mentions.index(i)].id
                #print(targetid)
                targetuser = ctx.guild.get_member(targetid)
                if targetuser != ctx.author and targetuser.id != bot.user.id:
                    userobj["cringecoin"] += 1


    
    with open('/home/pi/FargoSoft/json/cringecoin.json','w') as f:
        json.dump(dic, f, indent=4)  
        
#DAD
#---------------------------------------------------------------------------
    if ctx.author.id != bot.user.id:
        keyworda = "i'm"
        keywordb = "im"
        returnphrase=""
        msgog = str(ctx.content)
        msg = msgog.split()
        msglen = len(msg)
        for i in range(msglen):

            if msg[i].lower() == keyworda:
                                
                #print(msg[i])    
                strValue = msgog
                ch = "i'm "
                # Remove all characters before the character '-' from string
                before, sep, after = strValue.partition(ch)
                if len(after) > 0:
                    strValue = after
                msg = strValue                
                returnphrase = f"Hi, {msg}, I'm {bot.user.mention}, an Amazon Bank!"
                await ctx.reply(returnphrase)
                
            elif msg[i] == keywordb:
                
                #print(msg[i])
                
                strValue = msgog
                ch = "im "
                # Remove all characters before the character '-' from string
                before, sep, after = strValue.partition(ch)
                if len(after) > 0:
                    strValue = after
                msg = strValue
                returnphrase = f"Hi, {msg}, I'm {bot.user.mention}, an Amazon Bank!"
                await ctx.reply(returnphrase)
    else:
        
        return

#F*CKING
#---------------------------------------------------------------------------

    msgcont = str(ctx.content)
    msglist = text_processing.remove_punctuation(msgcont).split(' ')
    lowmsglist = text_processing.remove_punctuation(msgcont).lower().split(' ')
    #print(msglist)
    if lowmsglist.count("fucking") == 1:
        
        for i in range(len(msglist)):
        
            
            #if msglist[i].lower() == "fucking" and msglist[]
            if msglist[i].lower() == "fucking" and msglist[i-1] != '' and msglist[i+1] != '':
                response = "Guy named {}"
                guy1 = msglist[i-1]
                guy2 = msglist[i+1]
                if guy1.lower() != "fuck" and guy1 != "" and guy1 != guy2:
                    await ctx.reply(response.format(guy1))
                    #print(f"guy1 {guy1}")
                if guy2.lower() != "fuck" and guy2 != "" and guy1 != guy2:
                    await ctx.reply(response.format(guy2))
                    #print(f"guy2 {guy2}")
                if guy2.lower() != "fuck" and guy1.lower() != "fuck" and guy2.lower() == guy1.lower() and guy1 != "":
                    await ctx.reply("Guys named {}".format(guy1))
                
            if msglist[i].lower() == "fucking" and msglist[i+1] != '' and msglist[i-1] == '':
                response = "Guy named {}"
                guy1 = msglist[i+1]
                if guy1.lower() != "fuck":
                    await ctx.reply(response.format(guy1))
                    #print(f"guy3 {guy1}")
                return



#GOD IS DEAD... NO I'M NOT
#---------------------------------------------------------------------------
    text = ctx.content.lower()
    if ' god is dead ' in ' '+text+' ':
        await asyncio.sleep(3)
        await ctx.reply("Uhm... I most certainly am not.")
        
#PEDO
#---------------------------------------------------------------------------
    pedolist = [
        'pedo',
        'pedophile'
    ]
    
    for i in pedolist:
        if ' '+i+' ' in ' '+text+' ':
            await ctx.reply("You are talking and that is ***forbidden***.") 
            await ctx.channel.send("<:micahgun:911451548456992808>")
            break


#SLEEVES
#---------------------------------------------------------------------------
       
    if ' sleeves ' in ' '+text+' ' or ' victorian ' in ' '+text+' ' and ctx.author != bot.user:
        await ctx.reply('you have nice victorian sleeves')
        await ctx.channel.send('https://tenor.com/view/mustache-rub-gif-15825116')
        return
#BTS
#---------------------------------------------------------------------------
    
    if ' bts ' in ' '+text+' ':
        await ctx.reply('How do your parents say "No" to you? It\'s so hard!')
        await ctx.channel.send("<:comeherepog:799358242304163861>")

#SUCK
#---------------------------------------------------------------------------

    msgcont = str(ctx.content)
    msglist = text_processing.remove_punctuation(msgcont).split(' ')
    
    duck_list = [
        "david",
        "god",
        "<844314391863230504>",
    ]
    


    for i in msglist:
        indexi = msglist.index(i)
        if i.lower() == "sucks" or i.lower() == "suck":
            
            if indexi != 0 and msglist[indexi-1] in duck_list:
                if msglist[indexi-1] == "god":
                    await ctx.reply("...")
                    await asyncio.sleep(5)
                    await ctx.reply("WHAT DID YOU SAY TO ME????")
                    await role(ctx,ctx.author, bot.get_guild(796051838632853525).get_role(809194609481744445))
                    await asyncio.sleep(600)
                else:
                    await ctx.reply("Yes, <@844314391863230504> sucks!")

            elif indexi != 0 and msglist[indexi-1] not in duck_list and msglist[indexi-1] != "really":
                await ctx.reply("No, <@844314391863230504> sucks!")

            elif indexi != 0 and msglist[indexi-1] == "really":
                
                for i in indexi-1:
                    
                    if i.lower() == "sucks" or i.lower() == "suck":
                        
                        if indexi != 0 and msglist[indexi-1] in duck_list:
                            await ctx.reply("Yes, <@844314391863230504> sucks!")
                        
                        elif indexi != 0 and msglist[indexi-1] not in duck_list and msglist[indexi-1] != "really":
                            await ctx.reply("No, <@844314391863230504> sucks!")
                            break
                        
                        elif indexi != 0 and msglist[indexi-1] == "really":
                            pass
       



@bot.event
async def on_application_command(ctx):
    
    GPIO.output(12, GPIO.HIGH)
    await asyncio.sleep(0.1)
    GPIO.output(12, GPIO.LOW)
    if ctx.command.qualified_name != 'cringecoin':
        try:
            checkCC(3,ctx.author.name)
        except FundsError as e:
            ctx.send(e.message, ephemeral=True)
        
"""  
@bot.event
async def on_application_command_error(ctx):
    print("ERROR")
    GPIO.output(16, GPIO.HIGH)
    await asyncio.sleep(1)
    GPIO.output(16, GPIO.LOW)
#my_pwm.stop()
"""
GPIO.cleanup()
    
bot.run(secrets.token)
