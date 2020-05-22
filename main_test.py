import discord
from config import token

client = discord.Client()


@client.event
async def on_member_join(member: discord.Member):
    for text_channel in member.guild.text_channels:
        if text_channel.id == 610905145953484802:
            embed = discord.Embed()
            embed.description = member.display_name + " joined."
            embed.set_image(url="https://i.ibb.co/rfzGVLs/du-lauch.png")
            await text_channel.send(embed=embed)

client.run(token)
