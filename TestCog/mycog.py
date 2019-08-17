import discord
import gspread
import csv
import asyncio

import httplib2

from datetime import datetime
from redbot.core import commands
from redbot.core.data_manager import bundled_data_path
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from oauth2client.service_account import ServiceAccountCredentials

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import io

from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.predicates import MessagePredicate
from redbot.core.utils.menus import start_adding_reactions

from discord.utils import get


# use creds to create a client to interact with the Google Drive API


# Find a workbook by name and open the first sheet
# Make sure you use the right name here.


class Mycog(commands.Cog):
    """My custom cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("BossMan")
    async def test(self, ctx):
        await ctx.send('Has Role')

    @commands.command()
    @commands.has_any_role("BossMan")
    async def lookup2(self, ctx, *, name):
        """Lookup contact info"""
        # Your code will go here
        member = ctx.author
        message = await member.send('Fetching Information, Please Wait')

        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        file_path = bundled_data_path(self) / 'client_secret.json'
        creds = ServiceAccountCredentials.from_json_keyfile_name(file_path, scope)
        client = gspread.authorize(creds)
        sheet = client.open("Draconian Fleet Contact Sheet").sheet1


        try:
            cell = sheet.find(name.capitalize())
            row = cell.row
            values_list = sheet.row_values(row)
            
            discordid = discord.Member

            fname = values_list[0]
            lname = values_list[1]
            pname = values_list[3]
            dob = values_list[4]
            email = values_list[5]
            phone = values_list[6]
            
            ship = values_list[7]
            rank = values_list[8]
            homeaddr = values_list[9]
            mailaddr = values_list[10]
            paypale = values_list[11]
            prefcont = values_list[12]
            allerg1 = values_list[13]
            allerg2 = values_list[14]
            cname = values_list[15]
            cphone = values_list[16]
            crel = values_list[17]
            faceurl = values_list[18]
            discordid = values_list[19]
            updated = values_list[20]
            wname = fname + ' ' + lname
            userid = self.bot.get_user(int(discordid))
            discordav = userid.avatar_url
            discordhandle = userid.name

            contact1 = '**Pirate Name:** ' + pname + '\n**Phone:** ' + phone + '\n**Email:** ' + email + '\n**Discord:** ' + discordhandle
            contact2 = '**Name:** ' + cname + '\n**Phone:** ' + cphone + '\n**Relationship:** ' + crel
            contact3 = '**Medical Allergies:** ' + allerg1 + '\n**Food Allergies:** ' + allerg2
            contact4 = '**Birthday:** ' + dob
            contact5 = '**Ship:** ' + ship + '\n**Rank:** ' + rank

            embed = discord.Embed(colour=discord.Colour(0x106bca))
            embed.set_author(name=wname, icon_url="https://i2.wp.com/www.draconianfleet.com/wp-content/uploads/2017/09/cropped-frame-DF2-1.png?w=250&ssl=1")
            embed.set_thumbnail(url=discordav)
            embed.set_image(url=faceurl)
            embed.add_field(name="Contact Info", value=contact1, inline=True)
            embed.add_field(name="Emergency Contact", value=contact2, inline=True)
            embed.add_field(name="Allergies", value=contact3, inline=True)
            embed.add_field(name="Personal", value=contact4, inline=True)
            embed.add_field(name="Fleet Alignment", value=contact5, inline=False)
            
            await message.edit(content="", embed=embed)

        except gspread.exceptions.CellNotFound:
            await message.edit('Name not found')

    @commands.command()
    async def avatar(self, ctx):
        """Shows your Avatar"""
        idnum = ctx.author.id
        user = self.bot.get_user(int(idnum))
        u = user.avatar_url    
        embed = discord.Embed(description=user.name, timestamp=user.created_at ,colour=discord.Colour.blue())
        embed.set_image(url=u)

        await ctx.send(embed=embed)

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
        
