import logging
from random import randint
from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands
from redbot.core import Config
from redbot.core.bot import Red

from .utils import add_footer, kawaiiembed, rstats_embed, send_embed

log = logging.getLogger("red.sravan.perform")

class PerformCog(commands.Cog):
    """
    Perform different actions, like cuddle, poke etc.
    """

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self, identifier=8423644625413, force_registration=True
        )
        default_global = {
            "feed": [
                "https://media1.tenor.com/images/93c4833dbcfd5be9401afbda220066ee/tenor.gif?itemid=11223742",
                "https://media1.tenor.com/images/33cfd292d4ef5e2dc533ff73a102c2e6/tenor.gif?itemid=12165913",
                "https://media1.tenor.com/images/72268391ffde3cd976a456ee2a033f46/tenor.gif?itemid=7589062",
                "https://media1.tenor.com/images/4b48975ec500f8326c5db6b178a91a3a/tenor.gif?itemid=12593977",
                "https://media1.tenor.com/images/187ff5bc3a5628b6906935232898c200/tenor.gif?itemid=9340097",
                "https://media1.tenor.com/images/15e7d9e1eb0aad2852fabda1210aee95/tenor.gif?itemid=12005286",
                "https://media1.tenor.com/images/d08d0825019c321f21293c35df8ed6a9/tenor.gif?itemid=9032297",
                "https://media1.tenor.com/images/571da4da1ad526afe744423f7581a452/tenor.gif?itemid=11658244",
                "https://media1.tenor.com/images/6bde17caa5743a22686e5f7b6e3e23b4/tenor.gif?itemid=13726430",
                "https://media1.tenor.com/images/fd3616d34ade61e1ac5cd0975c25a917/tenor.gif?itemid=13653906",
                "https://imgur.com/v7jsPrv",
            ],
            "spank": [
                "https://media1.tenor.com/images/ef5f040254c2fbf91232088b91fe2341/tenor.gif?itemid=13569259",
                "https://media1.tenor.com/images/fa2472b2cca1e4a407b7772b329eafb4/tenor.gif?itemid=21468457",
                "https://media1.tenor.com/images/2eb222b142f24be14ea2da5c84a92b08/tenor.gif?itemid=15905904",
                "https://media1.tenor.com/images/86b5a47d495c0e8c5c3a085641a91aa4/tenor.gif?itemid=15964704",
                "https://media1.tenor.com/images/31d58e53313dc9bbd6435d824d2a5933/tenor.gif?itemid=11756736",
                "https://media1.tenor.com/images/97624764cb41414ad2c60d2028c19394/tenor.gif?itemid=16739345",
                "https://media1.tenor.com/images/f21c5c56e36ce0dfcdfe7c7993578c46/tenor.gif?itemid=21371415",
                "https://media1.tenor.com/images/58f5dcc2123fc73e8fb6b76f149441bc/tenor.gif?itemid=12086277",
                "https://media1.tenor.com/images/eafb13b900645ddf3b30cf9cc28e9f91/tenor.gif?itemid=4603671",
                "https://media1.tenor.com/images/be2bb9db1c8b8dc2194ec6a1b3d96b89/tenor.gif?itemid=18811244",
                "https://media.giphy.com/media/OoCuLoM6iEhYk/giphy.gif",
                "https://media.giphy.com/media/Qo3qovmbqaKT6/giphy.gif",
            ],
            "nut": [
                "https://c.tenor.com/2U9tTXuO_gUAAAAC/kick-anime.gif",
                "https://c.tenor.com/uHQL8xtAwaUAAAAd/kick-in-the-balls-anime.gif",
                "https://c.tenor.com/D67kRWw_cEEAAAAC/voz-dap-chym-dap-chym.gif",
                "https://c.tenor.com/_mW88MVAnrYAAAAC/heion-sedai-no-idatentachi-paula.gif",
                "https://c.tenor.com/CZT8alpjzzwAAAAd/ball-kick.gif",
                "https://c.tenor.com/KlvWYCEumXAAAAAd/kick-anime.gif",
                "https://c.tenor.com/9x-loeWpLyoAAAAC/talho-eureka-seven.gif",
                "https://c.tenor.com/6qtGbz6_894AAAAC/kick.gif",
                "https://c.tenor.com/NpMUvPFLwCEAAAAC/ow-balls-kick.gif",
                "https://c.tenor.com/pbyIf8fSIJsAAAAC/kick-balls-kick-in-the-balls.gif",
            ],
            "footer": True,
        }
        default_member = {
            "cuddle_s": 0,
            "poke_s": 0,
            "kiss_s": 0,
            "hug_s": 0,
            "slap_s": 0,
            "pat_s": 0,
            "tickle_s": 0,
            "smug_s": 0,
            "lick_s": 0,
            "cry": 0,
            "sleep": 0,
            "spank_s": 0,
            "pout": 0,
            "blush": 0,
            "feed_s": 0,
            "punch_s": 0,
            "confused": 0,
            "amazed": 0,
            "highfive_s": 0,
            "plead_s": 0,
            "clap": 0,
            "facepalm": 0,
            "facedesk": 0,
            "kill_s": 0,
            "love_s": 0,
            "hide": 0,
            "laugh": 0,
            "lurk": 0,
            "bite_s": 0,
            "dance": 0,
            "yeet_s": 0,
            "dodge": 0,
            "happy": 0,
            "cute": 0,
            "lonely": 0,
            "mad": 0,
            "nosebleed": 0,
            "protect_s": 0,
            "run": 0,
            "scared": 0,
            "shrug": 0,
            "scream": 0,
            "stare": 0,
            "wave_s": 0,
            "nut_s": 0,
        }
        default_target = {
            "cuddle_r": 0,
            "poke_r": 0,
            "kiss_r": 0,
            "hug_r": 0,
            "slap_r": 0,
            "pat_r": 0,
            "tickle_r": 0,
            "smug_r": 0,
            "lick_r": 0,
            "spank_r": 0,
            "feed_r": 0,
            "punch_r": 0,
            "highfive_r": 0,
            "plead_r": 0,
            "kill_r": 0,
            "love_r": 0,
            "bite_r": 0,
            "yeet_r": 0,
            "protect_r": 0,
            "wave_r": 0,
            "nut_r": 0,
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_member)
        self.config.init_custom("Target", 2)
        self.config.register_custom("Target", **default_target)
        self.cache = {}

        self.COMMANDS = [i.rstrip("_r") for i in default_target if i.endswith("_r")]

    __author__ = ["Onii-chan", "sravan"]
    __version__ = "5.8.3"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """
        Thanks Sinbad!
        """
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    @app_commands.command(name="cuddle", description="Cuddle a user!")
    async def cuddle(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "cuddled", "cuddle", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).cuddle_r()
        used = await self.config.user(interaction.user).cuddle_s()
        await add_footer(
            self, interaction, embed, used, "cuddles", target=target, word2="cuddled", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).cuddle_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).cuddle_r.set(
            target + 1
        )

    @app_commands.command(name="poke", description="Poke a user!")
    async def poke(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "poked", "poke", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).poke_r()
        used = await self.config.user(interaction.user).poke_s()
        await add_footer(
            self, interaction, embed, used, "pokes", target=target, word2="poked", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).poke_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).poke_r.set(
            target + 1
        )

    @app_commands.command(name="kiss", description="Kiss a user!")
    async def kiss(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "just kissed", "kiss", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).kiss_r()
        used = await self.config.user(interaction.user).kiss_s()
        await add_footer(
            self, interaction, embed, used, "kisses", target=target, word2="kissed", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).kiss_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).kiss_r.set(
            target + 1
        )

    @app_commands.command(name="hug", description="Hug a user!")
    async def hug(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "just hugged", "hug", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).hug_r()
        used = await self.config.user(interaction.user).hug_s()
        await add_footer(
            self, interaction, embed, used, "hugs", target=target, word2="hugged", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).hug_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).hug_r.set(target + 1)

    @app_commands.command(name="pat", description="Pat a user!")
    async def pat(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "just patted", "pat", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).pat_r()
        used = await self.config.user(interaction.user).pat_s()
        await add_footer(
            self, interaction, embed, used, "pats", target=target, word2="patted", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).pat_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).pat_r.set(target + 1)

    @app_commands.command(name="tickle", description="Tickle a user!")
    async def tickle(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "just tickled", "tickle", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).tickle_r()
        used = await self.config.user(interaction.user).tickle_s()
        await add_footer(
            self, interaction, embed, used, "tickles", target=target, word2="tickled", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).tickle_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).tickle_r.set(
            target + 1
        )

    @app_commands.command(name="smug", description="Be smug towards someone!")
    async def smug(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is acting so smug!", "smug")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).smug_s()
        await add_footer(self, interaction, embed, used, "smugs")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).smug_s.set(used + 1)

    @app_commands.command(name="lick", description="Lick a user!")
    async def lick(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "just licked", "lick", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).lick_r()
        used = await self.config.user(interaction.user).lick_s()
        await add_footer(
            self, interaction, embed, used, "licks", target=target, word2="licked", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).lick_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).lick_r.set(
            target + 1
        )

    @app_commands.command(name="slap", description="Slap a user!")
    async def slap(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "just slapped", "slap", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).slap_r()
        used = await self.config.user(interaction.user).slap_s()
        await add_footer(
            self, interaction, embed, used, "slaps", target=target, word2="slapped", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).slap_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).slap_r.set(
            target + 1
        )

    @app_commands.command(name="cry", description="Start crying!")
    async def cry(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is crying!", "cry")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).cry()
        await add_footer(self, interaction, embed, used, "cries")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).cry.set(used + 1)

    @app_commands.command(name="sleep", description="Act sleepy!")
    async def sleep(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is sleepy!", "sleepy")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).sleep()
        await add_footer(self, interaction, embed, used, "sleeps")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).sleep.set(used + 1)

    @app_commands.command(name="spank", description="Spank a user!")
    async def spank(self, interaction: discord.Interaction, user: discord.Member):
        images = await self.config.spank()
        mn = len(images)
        i = randint(0, mn - 1)

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=f"**{interaction.user.mention}** just spanked {f'**{str(user.mention)}**' if user else 'themselves'}!",
        )
        embed.set_author(
            name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar
        )
        embed.set_image(url=images[i])
        target = await self.config.custom("Target", interaction.user.id, user.id).spank_r()
        used = await self.config.user(interaction.user).spank_s()
        await add_footer(
            self, interaction, embed, used, "spanks", target=target, word2="spanked", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).spank_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).spank_r.set(
            target + 1
        )

    @app_commands.command(name="pout", description="Act pout!")
    async def pout(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is acting pout!", "pout")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).pout()
        await add_footer(self, interaction, embed, used, "pouts")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).pout.set(used + 1)

    @app_commands.command(name="blush", description="Act blush!")
    async def blush(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is blushing!", "blush")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).blush()
        await add_footer(self, interaction, embed, used, "blushes")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).blush.set(used + 1)

    @app_commands.command(name="feed", description="Feed a user!")
    async def feed(self, interaction: discord.Interaction, user: discord.Member):
        images = await self.config.feed()
        mn = len(images)
        i = randint(0, mn - 1)

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=f"**{interaction.user.mention}** feeds {f'**{str(user.mention)}**' if user else 'themselves'}!",
        )
        embed.set_author(
            name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar
        )
        embed.set_image(url=images[i])
        target = await self.config.custom("Target", interaction.user.id, user.id).feed_r()
        used = await self.config.user(interaction.user).feed_s()
        await add_footer(
            self, interaction, embed, used, "feeds", target=target, word2="fed", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).feed_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).feed_r.set(
            target + 1
        )

    @app_commands.command(name="punch", description="Punch a user!")
    async def punch(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "just punched", "punch", user)
        if embed is False:
            return await interaction.response.send_message("api is down")
        target = await self.config.custom("Target", interaction.user.id, user.id).punch_r()
        used = await self.config.user(interaction.user).punch_s()
        await add_footer(
            self, interaction, embed, used, "punches", target=target, word2="punched", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).punch_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).punch_r.set(
            target + 1
        )

    @app_commands.command(name="confuse", description="Act confused!")
    async def confuse(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is confused!", "confused")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).confused()
        await add_footer(self, interaction, embed, used, "confuses")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).confused.set(used + 1)

    @app_commands.command(name="amazed", description="Act amazed!")
    async def amazed(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is amazed!", "amazing")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).amazed()
        await add_footer(self, interaction, embed, used, "amazes")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).amazed.set(used + 1)

    @app_commands.command(name="highfive", description="Highfive a user!")
    async def highfive(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "highfived", "highfive", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).highfive_r()
        used = await self.config.user(interaction.user).highfive_s()
        await add_footer(
            self,
            interaction,
            embed,
            used,
            "highfives",
            target=target,
            word2="highfived",
            user=user,
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).highfive_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).highfive_r.set(
            target + 1
        )

    @app_commands.command(name="plead", description="Ask a user!")
    async def plead(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "is pleading", "ask", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).plead_r()
        used = await self.config.user(interaction.user).plead_s()
        await add_footer(
            self, interaction, embed, used, "pleads", target=target, word2="pleaded", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).plead_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).plead_r.set(
            target + 1
        )

    @app_commands.command(name="clap", description="Clap for someone!")
    async def clap(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is clapping!", "clap")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).clap()
        await add_footer(self, interaction, embed, used, "claps")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).clap.set(used + 1)

    @app_commands.command(name="facepalm", description="Do a facepalm!")
    async def facepalm(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is facepalming!", "facepalm")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).facepalm()
        await add_footer(self, interaction, embed, used, "facepalms")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).facepalm.set(used + 1)

    @app_commands.command(name="headdesk", description="Do a facedesk!")
    async def facedesk(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is facedesking!", "facedesk")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).facedesk()
        await add_footer(self, interaction, embed, used, "facedesks")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).facedesk.set(used + 1)

    @app_commands.command(name="kill", description="Kill a user!")
    async def kill(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "killed", "kill", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).kill_r()
        used = await self.config.user(interaction.user).kill_s()
        await add_footer(
            self, interaction, embed, used, "kills", target=target, word2="killed", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).kill_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).kill_r.set(
            target + 1
        )

    @app_commands.command(name="love", description="Love a user!")
    async def love(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "loves", "love", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).love_r()
        used = await self.config.user(interaction.user).love_s()
        await add_footer(
            self, interaction, embed, used, "loves", target=target, word2="loved", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).love_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).love_r.set(
            target + 1
        )

    @app_commands.command(name="hide", description="Hide yourself!")
    async def hide(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is hiding!", "hide")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).hide()
        await add_footer(self, interaction, embed, used, "hides")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).hide.set(used + 1)

    @app_commands.command(name="laugh", description="Start laughing!")
    async def laugh(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is laughing!", "laugh")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).laugh()
        await add_footer(self, interaction, embed, used, "laughs")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).laugh.set(used + 1)

    @app_commands.command(name="peek", description="Start lurking!")
    async def lurk(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is lurking!", "peek")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).lurk()
        await add_footer(self, interaction, embed, used, "lurks")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).lurk.set(used + 1)

    @app_commands.command(name="bite", description="Bite a user!")
    async def bite(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "is biting", "bite", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).bite_r()
        used = await self.config.user(interaction.user).bite_s()
        await add_footer(
            self, interaction, embed, used, "bites", target=target, word2="bit", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).bite_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).bite_r.set(
            target + 1
        )

    @app_commands.command(name="dance", description="Start dancing!")
    async def dance(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is dancing", "dance")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).dance()
        await add_footer(self, interaction, embed, used, "dances")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).dance.set(used + 1)

    @app_commands.command(name="yeet", description="Yeet someone!")
    async def yeet(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "yeeted", "yeet", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).yeet_r()
        used = await self.config.user(interaction.user).yeet_s()
        await add_footer(
            self, interaction, embed, used, "yeets", target=target, word2="yeeted", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).yeet_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).yeet_r.set(
            target + 1
        )

    @app_commands.command(name="dodge", description="Dodge something!")
    async def dodge(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is dodging!", "dodge")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).dodge()
        await add_footer(self, interaction, embed, used, "dodges")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).dodge.set(used + 1)

    @app_commands.command(name="happy", description="Act happy!")
    async def happy(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is happy!", "happy")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).happy()
        await add_footer(self, interaction, embed, used, "happiness")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).happy.set(used + 1)

    @app_commands.command(name="cute", description="Act cute!")
    async def cute(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is acting cute!", "cute")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).cute()
        await add_footer(self, interaction, embed, used, "cuteness")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).cute.set(used + 1)

    @app_commands.command(name="lonely", description="Act lonely!")
    async def lonely(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is lonely!", "lonely")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).lonely()
        await add_footer(self, interaction, embed, used, "loneliness")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).lonely.set(used + 1)

    @app_commands.command(name="mad", description="Act angry!")
    async def mad(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is angry!", "mad")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).mad()
        await add_footer(self, interaction, embed, used, "madness")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).mad.set(used + 1)

    @app_commands.command(name="nosebleed", description="Start bleeding from nose!")
    async def nosebleed(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "'s nose is bleeding!", "nosebleed")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).nosebleed()
        await add_footer(self, interaction, embed, used, "nosebleeds")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).nosebleed.set(used + 1)

    @app_commands.command(name="protect", description="Protect someone!")
    async def protect(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "is protecting!", "protect", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).protect_r()
        used = await self.config.user(interaction.user).protect_s()
        await add_footer(
            self,
            interaction,
            embed,
            used,
            "protects",
            target=target,
            word2="protected",
            user=user,
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).protect_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).protect_r.set(
            target + 1
        )

    @app_commands.command(name="run", description="Start running!")
    async def run(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is running!", "run")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).run()
        await add_footer(self, interaction, embed, used, "runs")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).run.set(used + 1)

    @app_commands.command(name="scared", description="Act scared!")
    async def scared(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is scared!", "scared")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).scared()
        await add_footer(self, interaction, embed, used, "scaredness")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).scared.set(used + 1)

    @app_commands.command(name="shrug", description="Start shrugging!")
    async def shrug(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is shrugging!", "shrug")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).shrug()
        await add_footer(self, interaction, embed, used, "shrugs")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).shrug.set(used + 1)

    @app_commands.command(name="scream", description="Start screaming!")
    async def scream(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is screaming!", "scream")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).scream()
        await add_footer(self, interaction, embed, used, "screams")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).scream.set(used + 1)

    @app_commands.command(name="stare", description="Stare at someone!")
    async def stare(self, interaction: discord.Interaction):
        embed = await kawaiiembed(self, interaction, "is staring!", "stare")
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        used = await self.config.user(interaction.user).stare()
        await add_footer(self, interaction, embed, used, "stares")
        await send_embed(self, interaction, embed)
        await self.config.user(interaction.user).stare.set(used + 1)

    @app_commands.command(name="wave", description="Wave to someone!")
    async def wave(self, interaction: discord.Interaction, user: discord.Member):
        embed = await kawaiiembed(self, interaction, "is waving", "wave", user)
        if not isinstance(embed, discord.Embed):
            return await interaction.response.send_message(embed)
        target = await self.config.custom("Target", interaction.user.id, user.id).wave_r()
        used = await self.config.user(interaction.user).wave_s()
        await add_footer(
            self, interaction, embed, used, "waves", target=target, word2="waved", user=user
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).wave_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).wave_r.set(
            target + 1
        )

    @app_commands.command(name="nutkick", description="Kick a user on the nuts!")
    async def kicknuts(self, interaction: discord.Interaction, user: discord.Member):
        images = await self.config.nut()
        mn = len(images)
        i = randint(0, mn - 1)

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=f"**{interaction.user.mention}** just kicked nuts of {f'**{str(user.mention)}**' if user else 'themselves'}!",
        )
        embed.set_author(
            name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar
        )
        embed.set_image(url=images[i])
        target = await self.config.custom("Target", interaction.user.id, user.id).nut_r()
        used = await self.config.user(interaction.user).nut_s()
        await add_footer(
            self,
            interaction,
            embed,
            used,
            "nutkicks",
            target=target,
            word2="nutkicked",
            user=user,
        )
        await send_embed(self, interaction, embed, user)
        await self.config.user(interaction.user).nut_s.set(used + 1)
        await self.config.custom("Target", interaction.user.id, user.id).nut_r.set(target + 1)

    @app_commands.command(name="performapi", description="Steps to get the API token needed for few commands.")
    @commands.is_owner()
    async def performapi(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="How to set API for perform cog",
            description=(
                """
                1. Go to https://kawaii.red/\n
                2. Login using your discord account\n
                3. Click on dashboard and copy your token\n
                4. Use `[p]set api perform api_key <token>`,
            """
            ),
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="performstats", description="View your roleplay stats")
    @commands.guild_only()
    async def performstats(self, interaction: discord.Interaction, action: str, user: Optional[discord.User]):
        if user is None:
            user = interaction.user
        if action not in self.COMMANDS:
            return await interaction.response.send_message(
                f"The valid choices to view stats for are {', '.join(f'`{c}`' for c in self.COMMANDS)}"
            )
        embed = await rstats_embed(self, interaction, action, user)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="performset", description="Settings for roleplay stats")
    @commands.is_owner()
    async def performset(self, interaction: discord.Interaction):
        pass

    @performset.command(name="footer", description="Toggle showing footers for roleplay stats")
    async def footer(self, interaction: discord.Interaction):
        value = await self.config.footer()
        await self.config.footer.set(not value)
        if value:
            await interaction.response.send_message("Footers will no longer be shown")
        else:
            await interaction.response.send_message("Footers will now be shown")

    def cog_unload(self):
        global hug
        if hug:
            try:
                self.bot.remove_command("hug")
            except Exception as e:
                log.info(e)
            self.bot.add_command(hug)


async def setup(bot: Red):
    global hug
    hug = bot.remove_command("hug")
    await bot.add_cog(PerformCog(bot))

    # Register the slash commands globally
    bot.tree.add_command(PerformCog.cuddle)
    bot.tree.add_command(PerformCog.poke)
    bot.tree.add_command(PerformCog.kiss)
    bot.tree.add_command(PerformCog.hug)
    bot.tree.add_command(PerformCog.pat)
    bot.tree.add_command(PerformCog.tickle)
    bot.tree.add_command(PerformCog.smug)
    bot.tree.add_command(PerformCog.lick)
    bot.tree.add_command(PerformCog.slap)
    bot.tree.add_command(PerformCog.cry)
    bot.tree.add_command(PerformCog.sleep)
    bot.tree.add_command(PerformCog.spank)
    bot.tree.add_command(PerformCog.pout)
    bot.tree.add_command(PerformCog.blush)
    bot.tree.add_command(PerformCog.feed)
    bot.tree.add_command(PerformCog.punch)
    bot.tree.add_command(PerformCog.confuse)
    bot.tree.add_command(PerformCog.amazed)
    bot.tree.add_command(PerformCog.highfive)
    bot.tree.add_command(PerformCog.plead)
    bot.tree.add_command(PerformCog.clap)
    bot.tree.add_command(PerformCog.facepalm)
    bot.tree.add_command(PerformCog.facedesk)
    bot.tree.add_command(PerformCog.kill)
    bot.tree.add_command(PerformCog.love)
    bot.tree.add_command(PerformCog.hide)
    bot.tree.add_command(PerformCog.laugh)
    bot.tree.add_command(PerformCog.lurk)
    bot.tree.add_command(PerformCog.bite)
    bot.tree.add_command(PerformCog.dance)
    bot.tree.add_command(PerformCog.yeet)
    bot.tree.add_command(PerformCog.dodge)
    bot.tree.add_command(PerformCog.happy)
    bot.tree.add_command(PerformCog.cute)
    bot.tree.add_command(PerformCog.lonely)
    bot.tree.add_command(PerformCog.mad)
    bot.tree.add_command(PerformCog.nosebleed)
    bot.tree.add_command(PerformCog.protect)
    bot.tree.add_command(PerformCog.run)
    bot.tree.add_command(PerformCog.scared)
    bot.tree.add_command(PerformCog.shrug)
    bot.tree.add_command(PerformCog.scream)
    bot.tree.add_command(PerformCog.stare)
    bot.tree.add_command(PerformCog.wave)
    bot.tree.add_command(PerformCog.kicknuts)
    bot.tree.add_command(PerformCog.performapi)
    bot.tree.add_command(PerformCog.performstats)
    bot.tree.add_command(PerformCog.performset)
        
