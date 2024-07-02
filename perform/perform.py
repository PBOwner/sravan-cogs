import logging
from random import randint
from typing import Optional, Union

import discord
from redbot.core import Config, commands, app_commands
from redbot.core.bot import Red

from .utils import add_footer, kawaiiembed, rstats_embed, send_embed

log = logging.getLogger("red.sravan.perform")

class Perform(commands.Cog):
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

    async def do_action(self, ctx_or_interaction: Union[commands.Context, discord.Interaction], user: Optional[discord.Member], action: str):
        if isinstance(ctx_or_interaction, commands.Context):
            author = ctx_or_interaction.author
        else:
            author = ctx_or_interaction.user

        embed = await kawaiiembed(self, ctx_or_interaction, f"{action}ed", action, user)
        if not isinstance(embed, discord.Embed):
            return await ctx_or_interaction.send(embed)

        if user:
            target = await self.config.custom("Target", author.id, user.id)[f"{action}_r"]()
            used = await self.config.user(author)[f"{action}_s"]()
            await add_footer(self, ctx_or_interaction, embed, used, f"{action}s", target=target, word2=f"{action}ed", user=user)
            await send_embed(self, ctx_or_interaction, embed, user)
            await self.config.user(author)[f"{action}_s"].set(used + 1)
            await self.config.custom("Target", author.id, user.id)[f"{action}_r"].set(target + 1)
        else:
            used = await self.config.user(author)[f"{action}_s"]()
            await add_footer(self, ctx_or_interaction, embed, used, f"{action}s")
            await send_embed(self, ctx_or_interaction, embed)
            await self.config.user(author)[f"{action}_s"].set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def cuddle(self, ctx: commands.Context, user: discord.Member):
        """
        Cuddle a user!
        """
        await self.do_action(ctx, user, "cuddle")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="poke")
    async def poke(self, ctx: commands.Context, user: discord.Member):
        """
        Poke a user!
        """
        await self.do_action(ctx, user, "poke")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="kiss")
    async def kiss(self, ctx: commands.Context, user: discord.Member):
        """
        Kiss a user!
        """
        await self.do_action(ctx, user, "kiss")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="hug")
    async def hug(self, ctx: commands.Context, user: discord.Member):
        """
        Hugs a user!
        """
        await self.do_action(ctx, user, "hug")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="pat")
    async def pat(self, ctx: commands.Context, user: discord.Member):
        """
        Pats a user!
        """
        await self.do_action(ctx, user, "pat")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="tickle")
    async def tickle(self, ctx: commands.Context, user: discord.Member):
        """
        Tickles a user!
        """
        await self.do_action(ctx, user, "tickle")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="smug")
    async def smug(self, ctx: commands.Context):
        """
        Be smug towards someone!
        """
        await self.do_action(ctx, None, "smug")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="lick")
    async def lick(self, ctx: commands.Context, user: discord.Member):
        """
        Licks a user!
        """
        await self.do_action(ctx, user, "lick")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="slap")
    async def slap(self, ctx: commands.Context, user: discord.Member):
        """
        Slaps a user!
        """
        await self.do_action(ctx, user, "slap")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="cry")
    async def cry(self, ctx: commands.Context):
        """
        Start crying!
        """
        await self.do_action(ctx, None, "cry")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="sleep")
    async def sleep(self, ctx: commands.Context):
        """
        Act sleepy!
        """
        await self.do_action(ctx, None, "sleep")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="spank")
    async def spank(self, ctx: commands.Context, user: discord.Member):
        """
        Spanks a user!
        """
        await self.do_action(ctx, user, "spank")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="pout")
    async def pout(self, ctx: commands.Context):
        """
        Act pout!
        """
        await self.do_action(ctx, None, "pout")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="blush")
    async def blush(self, ctx: commands.Context):
        """
        Act blush!
        """
        await self.do_action(ctx, None, "blush")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="feed")
    async def feed(self, ctx: commands.Context, user: discord.Member):
        """
        Feeds a user!
        """
        await self.do_action(ctx, user, "feed")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="punch")
    async def punch(self, ctx: commands.Context, user: discord.Member):
        """
        Punch a user!
        """
        await self.do_action(ctx, user, "punch")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="confuse", aliases=["confused"])
    async def confuse(self, ctx: commands.Context):
        """
        Act confused!
        """
        await self.do_action(ctx, None, "confuse")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="amazed", aliases=["amazing"])
    async def amazed(self, ctx: commands.Context):
        """
        Act amazed!
        """
        await self.do_action(ctx, None, "amazed")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def highfive(self, ctx: commands.Context, user: discord.Member):
        """
        Highfive a user!
        """
        await self.do_action(ctx, user, "highfive")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="plead")
    async def plead(self, ctx: commands.Context, user: discord.Member):
        """
        Asks a user!
        """
        await self.do_action(ctx, user, "plead")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="clap")
    async def clap(self, ctx: commands.Context):
        """
        Clap for someone!
        """
        await self.do_action(ctx, None, "clap")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="facepalm")
    async def facepalm(self, ctx: commands.Context):
        """
        Do a facepalm!
        """
        await self.do_action(ctx, None, "facepalm")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="headdesk", aliases=["facedesk"])
    async def facedesk(self, ctx: commands.Context):
        """
        Do a facedesk!
        """
        await self.do_action(ctx, None, "facedesk")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def kill(self, ctx: commands.Context, user: discord.Member):
        """
        Kill a user!
        """
        await self.do_action(ctx, user, "kill")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def love(self, ctx: commands.Context, user: discord.Member):
        """
        Love a user!
        """
        await self.do_action(ctx, user, "love")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="hide")
    async def hide(self, ctx: commands.Context):
        """
        Hide yourself!
        """
        await self.do_action(ctx, None, "hide")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="laugh")
    async def laugh(self, ctx: commands.Context):
        """
        Start laughing!
        """
        await self.do_action(ctx, None, "laugh")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="laugh")
    async def laugh(self, ctx: commands.Context):
        """
        Start laughing!
        """
        await self.do_action(ctx, None, "laugh")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="peek", aliases=["lurk"])
    async def lurk(self, ctx: commands.Context):
        """
        Start lurking!
        """
        await self.do_action(ctx, None, "lurk")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def bite(self, ctx: commands.Context, user: discord.Member):
        """
        Bite a user!
        """
        await self.do_action(ctx, user, "bite")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="dance")
    async def dance(self, ctx: commands.Context):
        """
        Start dancing!
        """
        await self.do_action(ctx, None, "dance")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def yeet(self, ctx: commands.Context, user: discord.Member):
        """
        Yeet someone!
        """
        await self.do_action(ctx, user, "yeet")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="dodge")
    async def dodge(self, ctx: commands.Context):
        """
        Dodge something!
        """
        await self.do_action(ctx, None, "dodge")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="happy")
    async def happy(self, ctx: commands.Context):
        """
        Act happy!
        """
        await self.do_action(ctx, None, "happy")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="cute")
    async def cute(self, ctx: commands.Context):
        """
        Act cute!
        """
        await self.do_action(ctx, None, "cute")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="lonely", aliases=["alone"])
    async def lonely(self, ctx: commands.Context):
        """
        Act lonely!
        """
        await self.do_action(ctx, None, "lonely")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="mad", aliases=["angry"])
    async def mad(self, ctx: commands.Context):
        """
        Act angry!
        """
        await self.do_action(ctx, None, "mad")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="nosebleed")
    async def nosebleed(self, ctx: commands.Context):
        """
        Start bleeding from nose!
        """
        await self.do_action(ctx, None, "nosebleed")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def protect(self, ctx: commands.Context, user: discord.Member):
        """
        Protech someone!
        """
        await self.do_action(ctx, user, "protect")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="run")
    async def run(self, ctx: commands.Context):
        """
        Start running!
        """
        await self.do_action(ctx, None, "run")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="scared")
    async def scared(self, ctx: commands.Context):
        """
        Act scared!
        """
        await self.do_action(ctx, None, "scared")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="shrug")
    async def shrug(self, ctx: commands.Context):
        """
        Start shrugging!
        """
        await self.do_action(ctx, None, "shrug")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="scream")
    async def scream(self, ctx: commands.Context):
        """
        Start screaming!
        """
        await self.do_action(ctx, None, "scream")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="stare")
    async def stare(self, ctx: commands.Context):
        """
        Stare someone!
        """
        await self.do_action(ctx, None, "stare")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(aliases=["welcome"])
    async def wave(self, ctx: commands.Context, user: discord.Member):
        """
        Wave to someone!
        """
        await self.do_action(ctx, user, "wave")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="nutkick", aliases=["kicknuts"])
    async def kicknuts(self, ctx: commands.Context, user: discord.Member):
        """
        Kick a user on the nuts!
        """
        await self.do_action(ctx, user, "nut")

    @commands.is_owner()
    @commands.command()
    async def performapi(self, ctx: commands.Context):
        """
        Steps to get the API token needed for few commands.
        """
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
        await ctx.send(embed=embed)

    @commands.command(aliases=["rstats", "pstats", "roleplaystats"])
    @commands.guild_only()
    async def performstats(
        self, ctx: commands.Context, action: str, user: Optional[discord.User]
    ):
        """View your roleplay stats"""
        if user is None:
            user = ctx.author
        if action not in self.COMMANDS:
            return await ctx.send(
                f"The valid choices to view stats for are {', '.join(f'`{c}`' for c in self.COMMANDS)}"
            )
        embed = await rstats_embed(self, ctx, action, user)
        await ctx.send(embed=embed)

    @commands.group(aliases=["pset", "rset", "roleplayset"])
    @commands.is_owner()
    async def performset(self, ctx: commands.Context):
        """Settings for roleplay stats"""

    @performset.command()
    async def footer(self, ctx: commands.Context):
        """Toggle showing footers for roleplay stats"""
        value = await self.config.footer()
        await self.config.footer.set(not value)
        if value:
            await ctx.send("Footers will no longer be shown")
        else:
            await ctx.send("Footers will now be shown")

    def cog_unload(self):
        global hug
        if hug:
            try:
                self.bot.remove_command("hug")
            except Exception as e:
                log.info(e)
            self.bot.add_command(hug)

    @app_commands.command()
    async def slash_cuddle(self, interaction: discord.Interaction, user: discord.Member):
        """Cuddle a user!"""
        await self.do_action(interaction, user, "cuddle")

    @app_commands.command()
    async def slash_poke(self, interaction: discord.Interaction, user: discord.Member):
        """Poke a user!"""
        await self.do_action(interaction, user, "poke")

    @app_commands.command()
    async def slash_kiss(self, interaction: discord.Interaction, user: discord.Member):
        """Kiss a user!"""
        await self.do_action(interaction, user, "kiss")

    @app_commands.command()
    async def slash_hug(self, interaction: discord.Interaction, user: discord.Member):
        """Hug a user!"""
        await self.do_action(interaction, user, "hug")

    @app_commands.command()
    async def slash_pat(self, interaction: discord.Interaction, user: discord.Member):
        """Pat a user!"""
        await self.do_action(interaction, user, "pat")

    @app_commands.command()
    async def slash_tickle(self, interaction: discord.Interaction, user: discord.Member):
        """Tickle a user!"""
        await self.do_action(interaction, user, "tickle")

    @app_commands.command()
    async def slash_smug(self, interaction: discord.Interaction):
        """Be smug towards someone!"""
        await self.do_action(interaction, None, "smug")

    @app_commands.command()
    async def slash_lick(self, interaction: discord.Interaction, user: discord.Member):
        """Lick a user!"""
        await self.do_action(interaction, user, "lick")

    @app_commands.command()
    async def slash_slap(self, interaction: discord.Interaction, user: discord.Member):
        """Slap a user!"""
        await self.do_action(interaction, user, "slap")

    @app_commands.command()
    async def slash_cry(self, interaction: discord.Interaction):
        """Start crying!"""
        await self.do_action(interaction, None, "cry")

    @app_commands.command()
    async def slash_sleep(self, interaction: discord.Interaction):
        """Act sleepy!"""
        await self.do_action(interaction, None, "sleep")

    @app_commands.command()
    async def slash_spank(self, interaction: discord.Interaction, user: discord.Member):
        """Spank a user!"""
        await self.do_action(interaction, user, "spank")

    @app_commands.command()
    async def slash_pout(self, interaction: discord.Interaction):
        """Act pout!"""
        await self.do_action(interaction, None, "pout")

    @app_commands.command()
    async def slash_blush(self, interaction: discord.Interaction):
        """Act blush!"""
        await self.do_action(interaction, None, "blush")

    @app_commands.command()
    async def slash_feed(self, interaction: discord.Interaction, user: discord.Member):
        """Feed a user!"""
        await self.do_action(interaction, user, "feed")

    @app_commands.command()
    async def slash_punch(self, interaction: discord.Interaction, user: discord.Member):
        """Punch a user!"""
        await self.do_action(interaction, user, "punch")

    @app_commands.command()
    async def slash_confuse(self, interaction: discord.Interaction):
        """Act confused!"""
        await self.do_action(interaction, None, "confuse")

    @app_commands.command()
    async def slash_amazed(self, interaction: discord.Interaction):
        """Act amazed!"""
        await self.do_action(interaction, None, "amazed")

    @app_commands.command()
    async def slash_highfive(self, interaction: discord.Interaction, user: discord.Member):
        """Highfive a user!"""
        await self.do_action(interaction, user, "highfive")

    @app_commands.command()
    async def slash_plead(self, interaction: discord.Interaction, user: discord.Member):
        """Ask a user!"""
        await self.do_action(interaction, user, "plead")

    @app_commands.command()
    async def slash_clap(self, interaction: discord.Interaction):
        """Clap for someone!"""
        await self.do_action(interaction, None, "clap")

    @app_commands.command()
    async def slash_facepalm(self, interaction: discord.Interaction):
        """Do a facepalm!"""
        await self.do_action(interaction, None, "facepalm")

    @app_commands.command()
    async def slash_facedesk(self, interaction: discord.Interaction):
        """Do a facedesk!"""
        await self.do_action(interaction, None, "facedesk")

    @app_commands.command()
    async def slash_kill(self, interaction: discord.Interaction, user: discord.Member):
        """Kill a user!"""
        await self.do_action(interaction, user, "kill")

    @app_commands.command()
    async def slash_love(self, interaction: discord.Interaction, user: discord.Member):
        """Love a user!"""
        await self.do_action(interaction, user, "love")

    @app_commands.command()
    async def slash_hide(self, interaction: discord.Interaction):
        """Hide yourself!"""
        await self.do_action(interaction, None, "hide")

    @app_commands.command()
    async def slash_laugh(self, interaction: discord.Interaction):
        """Start laughing!"""
        await self.do_action(interaction, None, "laugh")

    @app_commands.command()
    async def slash_lurk(self, interaction: discord.Interaction):
        """Start lurking!"""
        await self.do_action(interaction, None, "lurk")

    @app_commands.command()
    async def slash_bite(self, interaction: discord.Interaction, user: discord.Member):
        """Bite a user!"""
        await self.do_action(interaction, user, "bite")

    @app_commands.command()
    async def slash_dance(self, interaction: discord.Interaction):
        """Start dancing!"""
        await self.do_action(interaction, None, "dance")

    @app_commands.command()
    async def slash_yeet(self, interaction: discord.Interaction, user: discord.Member):
        """Yeet someone!"""
        await self.do_action(interaction, user, "yeet")

    @app_commands.command()
    async def slash_dodge(self, interaction: discord.Interaction):
        """Dodge something!"""
        await self.do_action(interaction, None, "dodge")

    @app_commands.command()
    async def slash_happy(self, interaction: discord.Interaction):
        """Act happy!"""
        await self.do_action(interaction, None, "happy")

    @app_commands.command()
    async def slash_cute(self, interaction: discord.Interaction):
        """Act cute!"""
        await self.do_action(interaction, None, "cute")

    @app_commands.command()
    async def slash_lonely(self, interaction: discord.Interaction):
        """Act lonely!"""
        await self.do_action(interaction, None, "lonely")

    @app_commands.command()
    async def slash_mad(self, interaction: discord.Interaction):
        """Act angry!"""
        await self.do_action(interaction, None, "mad")

    @app_commands.command()
    async def slash_nosebleed(self, interaction: discord.Interaction):
        """Start bleeding from nose!"""
        await self.do_action(interaction, None, "nosebleed")

    @app_commands.command()
    async def slash_protect(self, interaction: discord.Interaction, user: discord.Member):
        """Protect someone!"""
        await self.do_action(interaction, user, "protect")

    @app_commands.command()
    async def slash_run(self, interaction: discord.Interaction):
        """Start running!"""
        await self.do_action(interaction, None, "run")

    @app_commands.command()
    async def slash_scared(self, interaction: discord.Interaction):
        """Act scared!"""
        await self.do_action(interaction, None, "scared")

    @app_commands.command()
    async def slash_shrug(self, interaction: discord.Interaction):
        """Start shrugging!"""
        await self.do_action(interaction, None, "shrug")

    @app_commands.command()
    async def slash_scream(self, interaction: discord.Interaction):
        """Start screaming!"""
        await self.do_action(interaction, None, "scream")

    @app_commands.command()
    async def slash_stare(self, interaction: discord.Interaction):
        """Stare someone!"""
        await self.do_action(interaction, None, "stare")

    @app_commands.command()
    async def slash_wave(self, interaction: discord.Interaction, user: discord.Member):
        """Wave to someone!"""
        await self.do_action(interaction, user, "wave")

    @app_commands.command()
    async def slash_kicknuts(self, interaction: discord.Interaction, user: discord.Member):
        """Kick a user on the nuts!"""
        await self.do_action(interaction, user, "nut")

async def setup(bot: Red):
    global hug
    hug = bot.remove_command("hug")
    await bot.add_cog(Perform(bot))
