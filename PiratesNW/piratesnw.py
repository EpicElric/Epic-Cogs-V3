import discord
from redbot.core import commands
from redbot.core.data_manager import bundled_data_path

class PiratesNW(commands.Cog):
    """Pirates of the Pacific Northwest"""
    def __init__(self, bot):
        self.bot = bot

    def localfile(self, file):
        fh = bundled_data_path(self) / file
        return fh


    @commands.command()
    async def eventmap(self, ctx, event = None):
        """Shows Event Maps, tortuga19, seadog19, etc """
        if event == None:
            await ctx.send(content= "Please Select one of the following maps using ?eventmap <mapname>\n**Available Maps**:\n**tortuga19** = Port Nassau: Tortuga Nights 2019\n**tortuga19constab** = Port Nassau: Tortuga Nights 2019 Block Constab Map\n**seadog19** = Port Nassau: Seadog's Refuge 2019\n**tortuga18** = Tortuga 2018\n**seadog18** = Seadog Nights & Gypsy Carnival 2018\n**seadog18merchant** = Seadog Nights & Gypsy Carnival 2018 Merchant Map\n**seadog17** = Seadog Nights & Gypsy Carnival 2017\n**seadog17merchant** = Seadog Nights & Gypsy Carnival 2017 Merchant Map\n**seadog17galley** = Seadog Nights & Gypsy Carnival 2017 Galley Map\n**tortuga16** = Tortuga 2016\n**seadog16** = Seadog Nights & Gypsy Carnival 2016\n**tortuga15** = Tortuga 2015\n**seadog15** = Seadog Nights & Gypsy Carnival 2015\n**seadog14** = Seadog Nights & Gypsy Carnival 2014")
        elif event == "tortuga19":
            fh = self.localfile('tortuga19.jpg')
            await ctx.send(content= "Port Nassau: Tortuga Nights 2019", file=discord.File(fh, filename="tortugamap19.jpg"))
        elif event == "tortuga19constab":
            fh = self.localfile('tortuga19constab.jpg')
            await ctx.send(content= "Port Nassau: Tortuga Nights 2019 Block Constab Map", file=discord.File(fh, filename="tortugamap19constab.jpg"))
        elif event == "seadog19":
            fh = self.localfile('seadog19.jpg')
            await ctx.send(content= "Port Nassau: Seadog's Refuge 2019", file=discord.File(fh, filename="seadogmap19.jpg"))
        elif event == "tortuga18":
            fh = self.localfile('tortuga18.jpg')
            await ctx.send(content= "Tortuga 2018 Event Map", file=discord.File(fh, filename="tortugamap18.jpg"))
        elif event == "seadog18":
            fh = self.localfile('seadog18.jpg')
            await ctx.send(content= "Seadog Nights & Gypsy Carnival 2018 Event Map", file=discord.File(fh, filename="seadogmap18.jpg"))
        elif event == "seadog18mechant":
            fh = self.localfile('seadog18merchant.jpg')
            await ctx.send(content= "Seadog Nights & Gypsy Carnival 2018 Merchant Map", file=discord.File(fh, filename="seadogmap18merchant.jpg"))
        elif event == "tortuga17":
            fh = self.localfile('tortuga17.jpg')
            await ctx.send(content= "Tortuga 2017 Event Map", file=discord.File(fh, filename="tortugamap17.jpg"))
        elif event == "seadog17":
            fh = self.localfile('seadog17.jpg')
            await ctx.send(content= "Seadog Nights & Gypsy Carnival 2017 Event Map", file=discord.File(fh, filename="seadogmap17.jpg"))
        elif event == "seadog17merchant":
            fh = self.localfile('seadog17merchant.jpg')
            await ctx.send(content= "Seadog Nights & Gypsy Carnival 2017 Merchant Map", file=discord.File(fh, filename="seadogmap17merchant.jpg"))
        elif event == "seadog17galley":
            fh = self.localfile('seadog17galley.jpg')
            await ctx.send(content= "Seadog Nights & Gypsy Carnival 2017 Galley Map", file=discord.File(fh, filename="seadogmap17galley.jpg"))
        elif event == "tortuga16":
            fh = self.localfile('tortuga16.jpg')
            await ctx.send(content= "Tortuga 2016 Event Map", file=discord.File(fh, filename="tortugamap16.jpg"))
        elif event == "seadog16":
            fh = self.localfile('seadog16.jpg')
            await ctx.send(content= "Seadog Nights & Gypsy Carnival 2016 Event Map", file=discord.File(fh, filename="seadogmap16.jpg"))
        elif event == "tortuga15":
            fh = self.localfile('tortuga15.jpg')
            await ctx.send(content= "Tortuga 2015 Event Map", file=discord.File(fh, filename="tortugamap15.jpg"))
        elif event == "seadog15":
            fh = self.localfile('seadog15.jpg')
            await ctx.send(content= "Seadog Nights & Gypsy Carnival 2015 Event Map", file=discord.File(fh, filename="seadogmap15.jpg"))
        elif event == "seadog14":
            fh = self.localfile('seadog14.jpg')
            await ctx.send(content= "Seadog Nights & Gypsy Carnival 2014 Event Map", file=discord.File(fh, filename="seadogmap14.jpg"))
        else:
            await ctx.send(content='Event Map not found')    
        