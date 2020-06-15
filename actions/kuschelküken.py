import discord
import random

commands = ["cuddlechick", "kuschelküken"]
requires_mention = False
accepts_mention = False
description = "Ein Kuschelküken! (´｡• ᵕ •｡`)"

picture_urls = [
    "https://media.tenor.com/images/d47a415586e26da144f95799434ddc59/tenor.gif",
    "https://media.tenor.com/images/45c63edfe068b320698f6aa8317abb06/tenor.gif",
    "https://media.tenor.com/images/786b81c44e33aaed52b94d5481351be2/tenor.gif",
    "https://media.tenor.com/images/bf81564ae058991178057dbf04e4a691/tenor.gif",
    "https://media.tenor.com/images/d0e9f6ccd57fbcaa99c1eafb2e83061d/tenor.gif",
    "https://media.tenor.com/images/fa97254d32837abb671d099394da7395/tenor.gif",
    "https://media.tenor.com/images/cbbe34e6ddc0c6fc523f461139b8daca/tenor.gif",
    "https://media.tenor.com/images/d39006b4093d755a9e0d777e7908274e/tenor.gif",
    "https://media.tenor.com/images/a272eb6bda70b2e76f5f75e3a10798b8/tenor.gif",
    "https://media.tenor.com/images/30accf0f006d16e472c4e49100165e8a/tenor.gif",
    "https://media.tenor.com/images/185933592fa3740cf7029713a30e8c57/tenor.gif",
    "https://media.tenor.com/images/709bf33c02a7f3ada1690386247d293b/tenor.gif",
    "https://media.tenor.com/images/5c4ef70120fecd4387325afff3cfcf05/tenor.gif",
    "https://media.tenor.com/images/30f5f9b6c9763f8ea531c5965444270a/tenor.gif",
    "https://media.tenor.com/images/68be80c9492e3d0bb8d8b14c93a71027/tenor.gif",
    "https://media.tenor.com/images/7d2f3ba98751945bd18fdae92952d4c6/tenor.gif",
    "https://media.tenor.com/images/803b558223b478fffe387760c0295434/tenor.gif",
    "https://media.tenor.com/images/76ca9a5f493f2dc5b154f7db32d4e43b/tenor.gif",
    "https://media.tenor.com/images/40e600535ee2af50e7342e68252697da/tenor.gif",
    "https://media.tenor.com/images/40e5e3d275081ccd7b2f4c9cb628e772/tenor.gif",
    "https://media.tenor.com/images/0eea15e0431eb004420b555315c4091a/tenor.gif",
    "https://media.tenor.com/images/cdf9f97895b5ee06ed450d318ab25124/tenor.gif",
    "https://media.tenor.com/images/30f5f9b6c9763f8ea531c5965444270a/tenor.gif",
    "https://media.tenor.com/images/a82a7145c8df2c767f821d0b88d6bdf2/tenor.gif",
    "https://cdn.discordapp.com/avatars/404431566031552512/b88420a6c6f5015ca6b2277f02787774.png?size=1024"
    "https://media.tenor.com/images/a24ec7fafd74950e7c7e15c1160eb339/tenor.gif",
    "https://media.tenor.com/images/ea3fd4bf65e9ce7e093d6cc987e74970/tenor.gif",
    "https://i.imgur.com/inxht6k.gif?noredirect",
    "https://media.tenor.com/images/e1620124a080032f4d65fe3779181a74/tenor.gif",
    "https://webstockreview.net/images/chick-clipart-animation-4.gif",
    "https://oslo-production.s3.amazonaws.com/uploads/medium/asset/397/baby_chick.gif",
    "https://i.imgur.com/nNF7aLD.gif",
    "https://media.tenor.com/images/8649b4b882dc9d90cefd39d81c2c9b3f/tenor.gif",
    "https://i.pinimg.com/originals/66/bb/8b/66bb8b898adf5c556fa3ae6b5bd5f038.gif",
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Miep! :hatching_chick: :heart:"
    url = random.choice(picture_urls)
    embed.set_footer(text=url)
    embed.set_image(url=url)

    await message.channel.send(embed=embed)
