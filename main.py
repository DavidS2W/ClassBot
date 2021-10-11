import discord
import random
from discord.ext import commands
from datetime import datetime
import json
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

client = commands.Bot(command_prefix=';')
client.remove_command("help")

colors=[0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300]

linka = {
    "Sejarah": "https://meet.google.com/tnw-iszh-uco?authuser=1",
    "Chemistry": "https://us04web.zoom.us/j/3521671572?pwd=Z3ROazdGZWZIaFUxa0NqTXQ1MEZOUT09",
    "Physics": "https://us02web.zoom.us/j/4437107088?pwd=T280alhFWlFHRFlIQWptNmNaakkrQT09",
    "AddMaths": "https://meet.google.com/edv-bwbn-dgk",
    "Biology": "https://meet.google.com/lookup/f72so6bywc?authuser=1&hs=179",
    "Maths": "https://meet.google.com/lookup/buoso3o6oh",
    "English": "https://zoom.us/j/99255655878?pwd=MnpzRzVFMHUwNmxpV2g3MFo1SEdidz09",
    "BM": "https://meet.google.com/eyz-finr-iws?authuser=1",
    "BK": "https://us02web.zoom.us/j/902764764?pwd=emp0MlJQamZqejRVcGZVR25XQktpUT09",
    "RE": "https://meet.google.com/jfu-wyua-rxp?authuser=1",
    "Moral": "https://meet.google.com/pgr-wmjq-hqb?authuser=1"
}

mondict = [{"name": "Maths", "hour": 8, "minute": 28}, {"name": "BM", "hour": 9, "minute": 28}, {"name": "Chemistry", "hour": 10, "minute": 58}, {"name": "English", "hour": 11, "minute": 55}, {"name": "Sejarah", "hour": 13, "minute": 28}, {"name": "Physics", "hour": 14, "minute": 28}]

tuedict = [{"name": "RE", "hour": 7, "minute": 28}, {"name": "Chemistry", "hour": 8, "minute": 28}, {"name": "Sejarah", "hour": 9, "minute": 28}, {"name": "BM", "hour": 10, "minute": 58}, {"name": "BK", "hour": 11, "minute": 58}, {"name": "Maths", "hour": 13, "minute": 28}]

weddict = [{"name": "Moral", "hour": 8, "minute": 28}, {"name": "English", "hour": 9, "minute": 28}, {"name": "Biology", "hour": 11, "minute": 58}, {"name": "Physics", "hour": 11, "minute": 58},  {"name": "BM", "hour": 13, "minute": 28}, {"name": "AddMaths", "hour": 14, "minute": 28}]

thudict = [{"name": "Physics", "hour": 8, "minute": 28}, {"name": "Chemistry", "hour": 10, "minute": 58}, {"name": "Biology", "hour": 13, "minute": 28}, {"name": "BM", "hour": 14, "minute": 28}]

fridict = [{"name": "AddMaths", "hour": 8, "minute": 28}, {"name": "Moral", "hour": 10, "minute": 58}, {"name": "Physics", "hour": 11, "minute": 58}, {"name": "Biology", "hour": 13, "minute": 28}]

def code(dayem, day):
  if day == 'mon':
    for item in mondict:
      coda = f'{item["hour"]}{item["minute"]}'
      if int(coda) == int(dayem):
        return item["name"]
      else:
        pass
  elif day == 'tue':
    for item in tuedict:
      coda = f'{item["hour"]}{item["minute"]}'
      if int(coda) == int(dayem):
        return item["name"]
      else:
        pass
  elif day == 'wed':
    for item in weddict:
      coda = f'{item["hour"]}{item["minute"]}'
      if int(coda) == int(dayem):
        return item["name"]
      else:
        pass
  elif day == 'thu':
    for item in thudict:
      coda = f'{item["hour"]}{item["minute"]}'
      if int(coda) == int(dayem):
        return item["name"]
      else:
        pass
  elif day == 'fri':
    for item in fridict:
      coda = f'{item["hour"]}{item["minute"]}'
      if int(coda) == int(dayem):
        return item["name"]
      else:
        pass
      
@client.event
async def on_ready():
  print('We are now logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{prefix}help'))

  scheduler = AsyncIOScheduler()

  for item in mondict:
    async def helpem():
      IST = pytz.timezone('Asia/Shanghai')
      datetime_ist = datetime.now(IST)
      dayem = datetime_ist.strftime('%H%M')
      chan = client.get_channel(739047904257507338)
      kod = code(dayem, 'mon')
      link = linka[kod]
      em = discord.Embed(title=f'{kod} in 2 minutes!', description=link, color=random.choice(colors))
      em.set_thumbnail(url='https://img.icons8.com/clouds/500/google-meet.png')
      em.set_footer(text='© Miyuki404. Used with permission by Iridian.')
      await chan.send('<@&866568384496533555>', embed=em)
    scheduler.add_job(helpem, CronTrigger(day_of_week=0, hour=item["hour"], minute=item["minute"], second="0", timezone="Asia/Shanghai"))

  for item in tuedict:
    async def helpem():
      IST = pytz.timezone('Asia/Shanghai')
      datetime_ist = datetime.now(IST)
      dayem = datetime_ist.strftime('%H%M')
      chan = client.get_channel(739047904257507338)
      kod = code(dayem, 'tue')
      link = linka[kod]
      em = discord.Embed(title=f'{kod} in 2 minutes!', description=link, color=random.choice(colors))
      em.set_thumbnail(url='https://img.icons8.com/clouds/500/google-meet.png')
      em.set_footer(text='© Miyuki404. Used with permission by Iridian.')
      await chan.send('<@&866568384496533555>', embed=em)
    scheduler.add_job(helpem, CronTrigger(day_of_week=1, hour=item["hour"], minute=item["minute"], second="0", timezone="Asia/Shanghai"))

  for item in weddict:
    async def helpem():
      IST = pytz.timezone('Asia/Shanghai')
      datetime_ist = datetime.now(IST)
      dayem = datetime_ist.strftime('%H%M')
      chan = client.get_channel(739047904257507338)
      kod = code(dayem, 'wed')
      link = linka[kod]
      em = discord.Embed(title=f'{kod} in 2 minutes!', description=link, color=random.choice(colors))
      em.set_thumbnail(url='https://img.icons8.com/clouds/500/google-meet.png')
      em.set_footer(text='© Miyuki404. Used with permission by Iridian.')
      await chan.send('<@&866568384496533555>', embed=em)
    scheduler.add_job(helpem, CronTrigger(day_of_week=2, hour=item["hour"], minute=item["minute"], second="0", timezone="Asia/Shanghai"))

  for item in thudict:
    async def helpem():
      IST = pytz.timezone('Asia/Shanghai')
      datetime_ist = datetime.now(IST)
      dayem = datetime_ist.strftime('%H%M')
      chan = client.get_channel(739047904257507338)
      kod = code(dayem, 'thu')
      link = linka[kod]
      em = discord.Embed(title=f'{kod} in 2 minutes!', description=link, color=random.choice(colors))
      em.set_thumbnail(url='https://img.icons8.com/clouds/500/google-meet.png')
      em.set_footer(text='© Miyuki404. Used with permission by Iridian.')
      await chan.send('<@&866568384496533555>', embed=em)
    scheduler.add_job(helpem, CronTrigger(day_of_week=3, hour=item["hour"], minute=item["minute"], second="0", timezone="Asia/Shanghai"))

  for item in fridict:
    async def helpem():
      IST = pytz.timezone('Asia/Shanghai')
      datetime_ist = datetime.now(IST)
      dayem = datetime_ist.strftime('%H%M')
      chan = client.get_channel(739047904257507338)
      kod = code(dayem, 'fri')
      link = linka[kod]
      em = discord.Embed(title=f'{kod} in 2 minutes!', description=link, color=random.choice(colors))
      em.set_thumbnail(url='https://img.icons8.com/clouds/500/google-meet.png')
      em.set_footer(text='© Miyuki404. Used with permission by Iridian.')
      await chan.send('<@&866568384496533555>', embed=em)
    scheduler.add_job(helpem, CronTrigger(day_of_week=4, hour=item["hour"], minute=item["minute"], second="0", timezone="Asia/Shanghai"))
  scheduler.start()

prefix=';'

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    pass

@client.command()
async def hw(ctx):
  chan = client.get_channel(859668510761680906)
  msgs = await chan.history(limit=100).flatten()
  embed = discord.Embed(title='Showing homework for F4 Phi', description=f'There is a current total of {len(msgs)} entries', color=random.choice(colors))
  for item in msgs:
    c = str(msgs.index(item) + 1)
    embed.add_field(name=f'{c}. {item.content}', value=f'`ID: {item.id}`', inline=False)
  await ctx.send(embed=embed)

@client.command()
async def rhw(ctx, arg1):
  chan = client.get_channel(859668510761680906)
  msgs = await chan.history(limit=100).flatten()

  a = msgs[int(arg1)-1]
  b = await chan.fetch_message(a.id)
  await b.delete()
  await ctx.send(f'{a.content} has been deleted.')

@rhw.error
async def rhw_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.send('The homework you are trying to delete does not exist!')
  else:
    await ctx.send('Please specify the index of the homework you are trying to remove!')

@client.command()
async def nhw(ctx, *, arg1):
  chan = client.get_channel(859668510761680906)
  await chan.send(arg1)
  await ctx.send(f'{arg1} has been added to the list of homework.')

@nhw.error
async def nhw_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.send('The homework you are trying to delete does not exist!')
  else:
    await ctx.send('Please specify the homework you are trying to add to the list!')

@client.command()
async def rems(ctx):
  chan = client.get_channel(866508122108330016)
  msgs = await chan.history(limit=100).flatten()
  embed = discord.Embed(title='Showing reminders for F4 Phi', description=f'There is a current total of {len(msgs)} entries', color=random.choice(colors))
  for item in msgs:
    c = str(msgs.index(item) + 1)
    embed.add_field(name=f'{c}. {item.content}', value=f'`ID: {item.id}`', inline=False)
  await ctx.send(embed=embed)

@client.command()
async def rrems(ctx, arg1):
  chan = client.get_channel(866508122108330016)
  msgs = await chan.history(limit=100).flatten()

  a = msgs[int(arg1)-1]
  b = await chan.fetch_message(a.id)
  await b.delete()
  await ctx.send(f'{a.content} has been deleted.')

@rhw.error
async def rrems_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.send('The homework you are trying to delete does not exist!')
  else:
    await ctx.send('Please specify the index of the homework you are trying to remove!')

@client.command()
async def nrems(ctx, *, arg1):
  chan = client.get_channel(866508122108330016)
  await chan.send(arg1)
  await ctx.send(f'{arg1} has been added to the list of homework.')

@nhw.error
async def nrems_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.send('The homework you are trying to delete does not exist!')
  else:
    await ctx.send('Please specify the homework you are trying to add to the list!')

@client.command()
async def announcement(ctx, *, arg1):
  emeet = discord.Embed(title=f'**Important announcement from {ctx.author.name}!**', description= arg1, color=random.choice(colors))
  await ctx.send('<@&799921554338086912>', embed=emeet)
  
@client.command(aliases = ['tt'])
async def timetable(ctx):
  with open('sciclassg.json', 'r') as f:
    count1 = json.load(f)
  
  if count1['setting'] == 0:
    em = discord.Embed()
    em.title = 'Showing the online timetable for F4 Phi'
    em.set_image(url='https://i.imgur.com/vcygTzt.png')
    em.color=random.choice(colors)
    await ctx.send(embed=em)
  else:
    em = discord.Embed()
    em.title = 'Showing the physical timetable for F4 Phi'
    em.set_image(url='https://i.imgur.com/mfIh2Lg.png')
    em.color = random.choice(colors)
    await ctx.send(embed=em)

@announcement.error
async def announcement_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify the topic of your annoucement.')

@client.command()
async def ping(ctx):
  ping_info=round(client.latency*1000)
  await ctx.send(f'The latency is {ping_info}ms')

@client.command(aliases = ['wk'])
async def logs(ctx, arg1):
  with open('sciclassg.json', 'r') as f:
    sett = json.load(f)
  if sett['setting'] == 1:
    with open(f'{arg1}.json', 'r') as f:
      wk = json.load(f)

    yves = discord.Embed()
    yves.title = f'Showing daily logs for {arg1}'
    yves.color = random.choice(colors)
    for item in wk:
      yves.add_field(name=item, value=wk[item], inline=False)
    await ctx.send(embed=yves)
  elif sett['setting'] == 0:
    with open(f'{arg1}online.json', 'r') as f:
      wk = json.load(f)

    yves = discord.Embed()
    yves.title = f'Showing daily logs for {arg1}'
    yves.color = random.choice(colors)
    for item in wk:
      yves.add_field(name=item, value=wk[item], inline=False)
    await ctx.send(embed=yves)

@logs.error
async def logs_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.send('The day you have entered is invalid. Use only `mon,tue, wed, thu or fri`.')
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify the day you want to view work for `mon,tue, wed, thu or fri`.')

subjects = ["Chemistry", "AddMaths","BM","English","Physics","Maths", "Sejarah", "Moral", "Biology", "BK", "RE"]

@client.command(aliases=['addwk'])
async def addlogs(ctx, arg0, arg1, *, arg2):
  with open('sciclassg.json', 'r') as f:
    sett = json.load(f)

  if sett['setting'] == 1:
    if arg1 not in subjects:
      await ctx.send(f'You have entered an invalid subject. Use only `Chemistry, AddMaths, BM, English, Physics, Maths, Sejarah, Moral, Biology, BK, RE`.')
    else:
      with open(f'{arg0}.json', 'r') as f:
        wk = json.load(f)

        wk[arg1] = arg2

      with open(f'{arg0}.json', 'w') as f:
        json.dump(wk, f, indent=4)
      await ctx.send(f'{arg2} has been added for {arg1} on {arg0}.\nThanks for your contribution!')
  elif sett['setting'] == 0:
    if arg1 not in subjects:
      await ctx.send(f'You have entered an invalid subject. Use only `Chemistry, AddMaths, BM, English, Physics, Maths, Sejarah, Moral, Biology, BK, RE`.')
    else:
      with open(f'{arg0}online.json', 'r') as f:
        wk = json.load(f)

        wk[arg1] = arg2

      with open(f'{arg0}online.json', 'w') as f:
        json.dump(wk, f, indent=4)
      await ctx.send(f'{arg2} has been added for {arg1} on {arg0}.\nThanks for your contribution!')

@addlogs.error
async def addlogs_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify the day, subject and work you want to add.\n;addwk <day> <subject> <work>')
  else:
    await ctx.send('The day you have entered is invalid. Use only `mon,tue, wed, thu or fri`.')
  
@client.command(aliases=['clearwk'])
async def clearlogs(ctx, arg1):
  with open('sciclassg.json', 'r') as f:
    sett = json.load(f)
  if sett['setting'] == 1:
    with open(f'{arg1}.json', 'r') as f:
      wk = json.load(f)
    
    for item in wk:
      wk[item] = "Nothing added"
    
    with open(f'{arg1}.json', 'w') as f:
      json.dump(wk, f, indent=4)
    await ctx.send(f'The work for {arg1} has been cleared.')
  elif sett['setting'] == 0:
    with open(f'{arg1}online.json', 'r') as f:
      wk = json.load(f)
    
    for item in wk:
      wk[item] = "Nothing added"
    
    with open(f'{arg1}online.json', 'w') as f:
      json.dump(wk, f, indent=4)
    await ctx.send(f'The work for {arg1} has been cleared.')

@clearlogs.error
async def clearlogs_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify the day you want to clear.\n;clearwk <day>')
  elif isinstance(error, commands.CommandInvokeError):
    await ctx.send('The day you have specified is invalid.Use only `mon,tue, wed, thu or fri`.') 

@client.command(aliases = ['settings'])
async def setting(ctx, arg1):
  with open('sciclassg.json', 'r') as f:
    count1 = json.load(f)

  if arg1 == 'Physical' or arg1 == 'physical':
    count1['setting'] = 1
  elif arg1 == 'Online' or arg1 == 'online':
    count1['setting'] = 0
  else:
    await ctx.send('Please specify whether you want to change the class info settings to `online` or `physical`.')
    return
  
  with open('sciclassg.json', 'w') as f:
    json.dump(count1, f, indent=4)
  await ctx.send(f'The settings for class info have been changed to {arg1}.')
  
@setting.error
async def setting_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify whether you want to change the settings to `online` or `physical`.')
  
@client.command(aliases = ['class'])
async def classa(ctx, arg1):
  with open('sciclassg.json', 'r') as f:
    count1 = json.load(f)
  
  if count1['setting'] == 0:
    with open('links.json', 'r') as f:
      link = json.load(f)

    with open(f'{arg1}online.json', 'r') as f:
      day = json.load(f)

    classa = discord.Embed(title=f'Showing classes for {arg1}', description = f'`Requested by {ctx.author.name}`', color=random.choice(colors))
    classa.set_thumbnail(url='https://i.pinimg.com/originals/20/9b/e8/209be8b95ef7f87e37f5052f94e4dbf0.png')
    for item in day:
      classa.add_field(name=item, value=link[item], inline=False)
    await ctx.send(embed=classa)
  else:
    with open('inventory.json', 'r') as f:
      inv = json.load(f)
  
    with open(f'{arg1}.json', 'r') as f:
      day = json.load(f)

    dayem = discord.Embed(title=f'Showing what to bring for {arg1}', description = 'Remember to check the reminder list for extra stuff!', color=random.choice(colors))
    dayem.set_thumbnail(url='https://i.pinimg.com/originals/20/9b/e8/209be8b95ef7f87e37f5052f94e4dbf0.png')

    for item in day:
      dayem.add_field(name=item, value=inv[item], inline=False)
    await ctx.send(embed=dayem)

@classa.error
async def classa_error(ctx, error):
  IST = pytz.timezone('Asia/Kuala_Lumpur')
  datetime_ist = datetime.now(IST)
  dayem = (datetime_ist.strftime('%A')).lower()
  day = dayem[:3]
  if isinstance(error, commands.MissingRequiredArgument):
    with open('sciclassg.json', 'r') as f:
      count1 = json.load(f)
    counter = count1['setting']
    if counter == 0:
      try:
        with open('links.json', 'r') as f:
          link = json.load(f)

        with open(f'{day}online.json', 'r') as f:
          day = json.load(f)

        classa = discord.Embed(title=f'Showing classes for {dayem}', description = f'`Requested by {ctx.author.name}`', color=random.choice(colors))
        classa.set_thumbnail(url='https://i.pinimg.com/originals/20/9b/e8/209be8b95ef7f87e37f5052f94e4dbf0.png')
        for item in day:
          classa.add_field(name=item, value=link[item], inline=False)
        await ctx.send(embed=classa)
      except:
        await ctx.send('Please specify the day you want links for.\n;class <day>')
    else:
      with open('inventory.json', 'r') as f:
        inv = json.load(f)
  
      with open(f'{day}.json', 'r') as f:
        daya = json.load(f)

      dayem = discord.Embed(title=f'Showing what to bring for {day}', description = 'Remember to check the reminder list for extra stuff!', color=random.choice(colors))
      dayem.set_thumbnail(url='https://i.pinimg.com/originals/20/9b/e8/209be8b95ef7f87e37f5052f94e4dbf0.png')

      for item in daya:
        dayem.add_field(name=item, value=inv[item], inline=False)
      await ctx.send(embed=dayem)

  elif isinstance(error, commands.CommandInvokeError):
    await ctx.send('The day you have specified is invalid. Use only `mon,tue, wed, thu or fri`.')

@client.command()
async def linkset(ctx, arg1, *, arg2):
  with open('links.json', 'r') as f:
    link = json.load(f)
  
  if arg1 in subjects:

    link[arg1] = arg2

    with open('links.json', 'w') as f:
      json.dump(link, f, indent=4)
    await ctx.send(f'The link for {arg1} has been updated!')
  else:
    await ctx.send('The day you have specified is invalid. Use only `mon,tue, wed, thu or fri`.')


@linkset.error
async def linkset_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please specify the subject and the new link for it.\n;linkset <subject> <link>")

@client.command()
async def help(ctx):
  help_embed=discord.Embed(title='A list of commands for ClassBot', description='Get info about almost everything related to school here!', color=(random.choice(colors)))
  help_embed.add_field(name="Prefix", value=f"{prefix}", inline=False)
  help_embed.add_field(name="View homework", value=f"{prefix}hw", inline=True)
  help_embed.add_field(name="Add homework", value=f"{prefix}nhw", inline=True)
  help_embed.add_field(name="Remove homework", value=f"{prefix}rhw", inline=True)
  help_embed.add_field(name="View reminders", value=f"{prefix}rems", inline=True)
  help_embed.add_field(name="Add reminders", value=f"{prefix}nrems", inline=True)
  help_embed.add_field(name="Remove reminders", value=f"{prefix}rrems", inline=True)
  help_embed.add_field(name="View logs for a day", value=f"{prefix}logs", inline=True)
  help_embed.add_field(name="Add logs", value=f"{prefix}addlogs", inline=True)
  help_embed.add_field(name="Clear logs", value=f"{prefix}clearlogs", inline=True)
  help_embed.add_field(name="Make an important announcement", value=f"{prefix}announcement", inline=False)
  help_embed.add_field(name="Get class information", value=f"{prefix}class", inline=False)
  help_embed.add_field(name="Set the bot to give you class data for physical or online settings", value=f"{prefix}setting", inline=False)
  help_embed.add_field(name="Change online class links.", value=f"{prefix}linkset", inline=False)
  help_embed.add_field(name="Get the latest school circular", value=f"{prefix}circ", inline=False)
  help_embed.add_field(name="Find out how high the latency is", value=f"{prefix}ping", inline=False)
  help_embed.set_thumbnail(url='https://i.pinimg.com/originals/20/9b/e8/209be8b95ef7f87e37f5052f94e4dbf0.png')
  help_embed.set_footer(text="Bug? Contact Dav via WhatsApp or dms!")
  await ctx.send(embed=help_embed)

@client.command()
async def circ(ctx):
  circ_embed=discord.Embed(title="The latest circular for SJPS!", description="[Click this link to access the latest circular](https://drive.google.com/file/d/1k5r73K5Tv72GzF0ovM_47hrHHU6TP0Fs/view)", color=(random.choice(colors)))
  circ_embed.add_field(name='School Diary', value='[Click here](https://docs.google.com/document/d/17DWwZV9e3Ii19PJhg0E1fcjK293pP_zTYJPlA99aKdA/edit?usp=sharing)', inline=True)
  circ_embed.add_field(name='SJPS Website', value='[Click here](https://stjosephkuching.edu.my/)', inline=True)
  circ_embed.set_thumbnail(url='https://i.pinimg.com/originals/20/9b/e8/209be8b95ef7f87e37f5052f94e4dbf0.png')
  await ctx.send(embed=circ_embed)

@client.command()
async def invite(ctx):
  inv = discord.Embed(title='The invite link for ClassBot!', description = 'https://discord.com/api/oauth2/authorize?client_id=793384336782655530&permissions=268958961&scope=bot', color=random.choice(colors))
  inv.set_thumbnail(url=client.user.avatar_url)
  await ctx.send(embed=inv)

client.run('ODQwNTA2NzMzMDU4MDY0NDA0.YJZM5Q.cPUwLHYM2XSFZ8r0ythFpMcA8Ao')
