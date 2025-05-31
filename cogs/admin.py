import discord
from discord.ext import commands

from config import Config


# 管理用のコグを表します。
class AdminCog(commands.Cog):

    # コンストラクタ
    def __init__(self, bot: commands.Bot, config: Config):
        self.bot = bot
        self.config = config