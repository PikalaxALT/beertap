import discord

__all__ = ('echo',)


@discord.app_commands.command()
async def echo(interaction: discord.Interaction, *, message: str):
    await interaction.response.send_message(f'Your message: {message}')
