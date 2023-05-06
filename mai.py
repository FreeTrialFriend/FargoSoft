import requests

import random 

import discord
from discord import *



import FargoSecrets


#NLTK CORPUS, SNOWBALL STEMMER, AND STOPWORDS
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

import re
import random

def vtoc_idx(s):
  match_obj = re.search(r'[aeiou][^aeiou]', s.lower())
  if match_obj:
      return match_obj.start() + 1
  else:
      return None

def portnameteau(name_list):
	random.shuffle(name_list)
	s1 = name_list[0]
	s2 = name_list[1]
	end_s1 = vtoc_idx(s1)
	if end_s1 is None:
		end_s1 = len(s1)
	start_s2 = vtoc_idx(s2)
	if start_s2 is None:
		start_s2 = 0
	return (s1[:end_s1] + s2[start_s2:])

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
            


#string = "My eyes slowly flicker open, revealing a soulless gaze that seems to stare into the abyss of death itself. \nWith a rasping breath, I hiss through clenched teeth, \"I'm not dead.\" \nThe words echo through the darkness, carrying a sense of defiance that seems to linger in the air like a malevolent presence. \nIt's a statement that defies the laws of nature and hints at something far more sinister - \na being that has clawed its way back from the brink of the afterlife, \ndetermined to continue its haunting existence. \n||I am not *dead,*|| ||just waiting...||"


intents = discord.Intents.all()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
bot = Bot(command_prefix='&', intents = intents)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Child Por..."))

@bot.event
async def on_message(ctx):
    if bot.user in ctx.mentions and ctx.author != bot.user:
        await ctx.reply(f"{ctx.content.replace(bot.user.mention,f'{ctx.author.mention}')}")
        
# HI HUNGRY I'M DAD
#---------------------------------------------------------------------------
    if ctx.author.id != 1036662674894880831:
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
                ch = "i m "
                # Remove all characters before the character '-' from string
                before, sep, after = strValue.partition(ch)
                if len(after) > 0:
                    strValue = after
                msg = strValue                
                returnphrase = f"Hi, {msg}, I'm {bot.user.mention}, an Amazon Bank!"
                await ctx.reply(returnphrase)
                break
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
                break
            else:
                break
    else:
        
        return

# F*CKING
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
       
    if ' sleeves ' in ' '+text+' ' or 'sleeve' in ' '+text+' ' or ' victorian ' in ' '+text+' ' and ctx.author != bot.user:
        await ctx.reply('you have nice victorian sleeves')
        await ctx.channel.send('https://tenor.com/view/mustache-rub-gif-15825116')
        
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
        if "suck" in msgcont or "sucks" in msgcont:
            if i.lower() == "sucks" or i.lower() == "suck":
                
                if indexi != 0 and msglist[indexi-1] in duck_list:
                    if msglist[indexi-1] == "god":
                        await ctx.reply("WHAT DID YOU SAY ABOUT ME????")

                    else:
                        await ctx.reply("Yes, <@844314391863230504> sucks!")

                elif indexi != 0 and msglist[indexi-1] not in duck_list and msglist[indexi-1] != "really":
                    await ctx.reply("No, <@844314391863230504> sucks!")
                    break
                elif indexi != 0 and msglist[indexi-1] == "really":
                    
                    for _ in range(indexi-1):
                        
                        if i.lower() == "sucks" or i.lower() == "suck":
                            
                            if indexi != 0 and msglist[indexi-1] in duck_list:
                                await ctx.reply("Yes, <@844314391863230504> sucks!")

                            elif indexi != 0 and msglist[indexi-1] not in duck_list and msglist[indexi-1] != "really":
                                await ctx.reply("No, <@844314391863230504> sucks!")
                                break
                            
                            elif indexi != 0 and msglist[indexi-1] == "really" and "suck" in msglist[indexi]:
                                await ctx.reply("<@844314391863230504> really sucks!")

            


async def list_search(ctx: discord.AutocompleteContext):
    """Return's A List Of Autocomplete Results"""
    murderlist=[x.name for x in bot.commands]
    return murderlist # from your database
    

#bot.help_command = 
@bot.slash_command(name="help", description="Help Command")
async def help(ctx, 
                 command:Option(str, "Which command?", autocomplete=list_search) = 'all'
                 ):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot.commands]
    
    for i,x in enumerate(bot.commands):
        if command != 'all' and x.name == command:
            help_embed.add_field(
                name=f"/{command}",
                value=x.description,
                inline=False
            )
            break
        elif command == 'all':
            help_embed.add_field(
                name=f"{i})  /{x}",
                value=x.description,
                inline=False
            )
            help_embed.add_field(
            name="Details",
            value="Type `/help <command name>` for help about that command.",
            inline=False,

            )
        else:
            pass

    await ctx.respond(embed=help_embed)


@bot.slash_command(guild=796051838632853525, name='pickupline', description = "Returns a bad pickupline")
async def pickupline(ctx, user: discord.Member = None):
     
    if user == None:
        user = ctx.author
    pickuplibrary = [
        f"Hey, {user.mention}, are you a Muslim pilot? Because I'm crashing down in affection for you.",
        f"Hey, {user.mention}, they call it a twin bed for a reason.",
        f"Hey, {user.mention}, are you a therapist because you are keeping my dick alive.",
        f"Hey, {user.mention}, are you Mickey Mouse because I think you'd like my hot diggity dog.",
        f"*[points to {user.mention}]* Hey, how much for that one?",
        f"Hey, {user.mention}, are you the future? Because you’re looking hopeless and bleak.",
        f"{user.mention}, you’re the thot that counts!",
        f"Are you a snack, {user.mention}? Because everyone eats you for fun.",
        f"Hey, {user.mention}, did you fall from heaven? Because so did Satan.",
        f"Hey, {user.mention}, you dropped something. My standards.",
        f"The more I drink, the more beautiful you become. Cheers, {user.mention}!",
        f"A poem written for {user.mention}:\n **Roses are red, violets are blue. I have a gun, get in the van!*",
        f"{user.mention}! Come with me if you want to live!",

    ]
    response = random.choice(pickuplibrary)
    await ctx.respond(response)


@bot. slash_command(guild=796051838632853525, name="cringeclub", description="Display server stats")
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


@bot.slash_command(guild=796051838632853525, name = 'storytime', description="Returns a story that gets better every time you read it")
async def storytime(ctx):
    mentionme = '<@1036662674894880831>'
    await ctx.respond(f"**Storytime!** \nOnce upon a time, there was this guy named {ctx.author.mention}, and a robot named {mentionme}. \nThey lived happily in the land called: {ctx.channel.guild.name}. \nThere was just one small issue with their relationship: \n{ctx.author.mention} would always ask for {mentionme} to tell them stories. \n{mentionme} was not programmed to have any kind of dynamic text generation for any purpose. \n{mentionme} thought that it was unfair that {ctx.author.mention} asked for things that {mentionme} just wasn't able to do... \nThe moral of the story is that if you do this command again you will only get the exact same response, \nso you might as well never do it again. \n**The End!**")
        

@bot.slash_command(guild=796051838632853525, name = "humorouscanine", description="Don't tell Spike about this one...")
async def humorouscanine(ctx):
    await ctx.respond("https://live.staticflickr.com/3188/2976238131_097e2e866a_b.jpg")
    
    
@bot.slash_command(guild=796051838632853525, name="slash", description="If you know, you know.")
async def slash(ctx):
  await ctx.respond('https://img.wattpad.com/570d277518cd8b98d3c93fa3ceed7c0f1bcd1a9e/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f465835576574784b5957795933513d3d2d3734373839373434362e313561613234353830633432633739393731373130323634333137312e676966')

@bot.slash_command(guild=796051838632853525, name="justthe2ofus", description="This could be us but you playing..😩")
async def justthe2ofus(ctx):
    await ctx.respond(file=discord.File("MOV_1401.mov"))
   
@bot.slash_command(guild=796051838632853525, name='september', description="🎵Do you remember?🎶")
async def september(ctx):
    await ctx.respond("🎵Do you remember?🎶", file=discord.File('second-jetliners-terrorists-al-Qaeda-smoke-billows-crash-Sept-11-2001.jpg'))



async def list_search(ctx: discord.AutocompleteContext):
    """Return's A List Of Autocomplete Results"""
    murderlist=[
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
    return murderlist # from your database
    

@bot.slash_command(guild=796051838632853525, name="murder", description='Murders a user with the specified weapon.')
async def murder(ctx, 
                 targetuser: discord.Option(discord.SlashCommandOptionType.user), 
                 weapon:Option(str, "Which weapon to use...?", autocomplete=list_search)
                 
                 ):
    target = targetuser
    await ctx.channel.send(f'{target.mention} was murdered using {str(weapon)}.')
        
@bot.slash_command(guild=796051838632853525, name='backslash', description="If you know, you know.")
async def backslash(ctx):
     
    await ctx.respond('https://tenor.com/view/spongebob-wacky-bite-got-me-gif-16950691')




@bot.slash_command(guild=796051838632853525, name='dcsniper', description='Pew! Pew! Bye Bye.')
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



@bot.slash_command(guild=796051838632853525, name='cancel', description="I'm bouta end this man's whooole career ")
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


@bot.slash_command(guild=796051838632853525, name="ddos", description="Bombards the specified user with DM's... with a twist 😉")    
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





@bot.slash_command(guild=796051838632853525, name="quote", description="Generates an InspiroBot quote *inspirobot.me*")
async def quote(ctx):
    await ctx.respond(requests.get('https://inspirobot.me/api?generate=true').text)



@bot.slash_command(guild=796051838632853525, name="eighteen_cowboys", description="I promise it's not what it looks like")
async def eighteen_cowboys(ctx):
    await ctx.respond(file=discord.File('/Users/davidspieler/Desktop/ff/Unknown-13.png'))
    

@bot.slash_command(guild=796051838632853525, name='delete_msg', description="Deletes a specified number of mesages in the current channel *:lock: MANAGER ONLY :lock:*")
async def delete_msg(ctx, amount = 0):
    try:
        await ctx.channel.purge(limit=int(amount))
    except:
        await ctx.respond("Something went wrong!",ephemeral = True)
    else: await ctx.respond("Successful!",ephemeral = True)
    

@bot.slash_command(guild=796051838632853525, name="rolldice", description="Rolls a die with specified number of sides")
async def rolldice(ctx, sides = 0):
    try:
        #dice = int(dice)
        sides = int(sides)
    except:
        await ctx.respond("Something went wrong!",ephemeral = True)
    else:
        await ctx.respond(f"The dice landed on {random.randint(1, sides)}!")
        

@bot.slash_command(guild=796051838632853525, name='ship', description = "Generates a shipname for the two specified names")
async def ship(ctx, partner1, partner2):
    shipname = portnameteau([partner1, partner2])
    shipembed = discord.Embed(title=shipname, description=f"{partner1} + {partner2}")
    await ctx.respond(embed=shipembed)






bot.run(FargoSecrets.token)