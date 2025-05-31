import discord
from discord.ext import commands

from config import Config


# 管理用のコグを表します。
class AdminCog(commands.Cog):

    # コンストラクタ
    def __init__(self, bot: commands.Bot, config: Config):
        self.bot = bot
        self.config = config

    # 現在の設定を取得します。
    @commands.command(name="config")
    @commands.is_owner()
    async def show_config(self, ctx: commands.Context):
        string = '\n'.join(f"{k}:{v}" for k, v in self.config.__dict__.items())        
        await ctx.send(f"```{string}```")