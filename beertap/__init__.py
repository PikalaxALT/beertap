import discord

__all__ = ('BeerTap',)


class BeerTap(discord.Client):
    def __init__(self, *, intents: discord.Intents, **options):
        super().__init__(intents=intents, **options)
        self._command_tree = discord.app_commands.CommandTree(self)
    
    async def setup_hook(self):
        await self.wait_until_ready()
        await self._command_tree.sync()

    def add_command(self, command: discord.app_commands.Command, **kwargs):
        self._command_tree.add_command(command, **kwargs)
