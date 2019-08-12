import discord
import gspread
import csv
import asyncio
from datetime import datetime
from redbot.core import commands
from redbot.core.data_manager import bundled_data_path
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from oauth2client.service_account import ServiceAccountCredentials
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.predicates import MessagePredicate
from redbot.core.utils.menus import start_adding_reactions


# use creds to create a client to interact with the Google Drive API


# Find a workbook by name and open the first sheet
# Make sure you use the right name here.


class Mycog(commands.Cog):
    """My custom cog"""


    @commands.command()
    async def test(self, ctx):
        """Test Code"""
        # Your code will go here
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        file_path = bundled_data_path(self) / 'client_secret.json'
        creds = ServiceAccountCredentials.from_json_keyfile_name(file_path, scope)
        client = gspread.authorize(creds)
        sheet = client.open("DragonBot Tester").sheet1
        row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
        index = 2
        sheet.insert_row(row, index)

    @commands.command()
    async def cmd(self, ctx):
        msg = await ctx.send("Yes or no?")
        start_adding_reactions(msg, ReactionPredicate.YES_OR_NO_EMOJIS)
        
        pred = ReactionPredicate.yes_or_no(msg, ctx.author)
        await ctx.bot.wait_for("reaction_add", check=pred)
        if pred.result is True:
        # User responded with tick
            await ctx.send('yes')
        else:
        # User responded with cross
            await ctx.send('no')
    
    
    @commands.command()
    async def cmd2(self, ctx):
        msg = await ctx.send("React to me!")
        emojis = ReactionPredicate.ALPHABET_EMOJIS[:5]
        start_adding_reactions(msg, emojis)

        pred = ReactionPredicate.with_emojis(emojis, msg)
        await ctx.bot.wait_for("reaction_add", check=pred)
        # pred.result is now the index of the letter in `emojis`
        await ctx.send(pred.result)
    
    @commands.command()
    async def cmd3(self, ctx):
        def check(m):
            return m.channel.id == ctx.channel.id and ctx.author.id == ctx.message.author.id

        await ctx.send("Email Address?")
        email = await ctx.bot.wait_for("message", check=check)

        await ctx.send("First Name?")
        firstname = await ctx.bot.wait_for("message", check=check)        
        
        await ctx.send("Last Name?")
        lastname = await ctx.bot.wait_for("message", check=check)  
        
        await ctx.send("Pirate Name?")
        piratename = await ctx.bot.wait_for("message", check=check)  
        
        await ctx.send("Phone Number?")
        phonenumber = await ctx.bot.wait_for("message", check=check)  

        msg1 = await ctx.send("Do you have an Emergency Contact? Y/N")
        start_adding_reactions(msg1, ReactionPredicate.YES_OR_NO_EMOJIS)
        
        pred = ReactionPredicate.yes_or_no(msg1, ctx.author)
        await ctx.bot.wait_for("reaction_add", check=pred)
        if pred.result is True:
        # User responded with tick
            await ctx.send("Emergency Contact Name?")
            emgname = await ctx.bot.wait_for("message", check=check)  
        
            await ctx.send("Emergency Contact Phone Number?")
            emgphone = await ctx.bot.wait_for("message", check=check)

            await ctx.send("Emergency Contact Relationship?")
            emgrelation = await ctx.bot.wait_for("message", check=check)

        
        

        # Begin posting data to Spreedsheet
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        file_path = bundled_data_path(self) / 'client_secret.json'
        creds = ServiceAccountCredentials.from_json_keyfile_name(file_path, scope)
        client = gspread.authorize(creds)
        
        sheet = client.open("DragonBot Tester").sheet1
        index = 2
        now = datetime.now()
        ts = int(datetime.timestamp(now))
        

        row = [datetime.utcfromtimestamp(ts).strftime('%m/%d/%Y %H:%M:%S'),email.content,firstname.content,lastname.content,piratename.content,phonenumber.content]
        sheet.insert_row(row, index)
        
