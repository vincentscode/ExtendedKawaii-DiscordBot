import discord
import random

commands = ["pigcuddle", "cuddlepig", "kuschelschwein", "kuschelschweinchen"]
requires_mention = False
accepts_mention = False
description = "Ein Kuschelschweinchen! (´｡• ᵕ •｡`)"

picture_urls = [
    "https://cdn.pixabay.com/photo/2020/05/30/23/13/piglet-5240704_960_720.jpg",
    "https://cdn.pixabay.com/photo/2013/02/21/19/13/agriculture-84702_960_720.jpg",
    "https://cdn.pixabay.com/photo/2019/06/10/19/24/pot-bellied-pig-4265062_960_720.jpg",
    "https://cdn.pixabay.com/photo/2018/03/30/16/16/piglet-3275738_960_720.jpg",
    "https://cdn.pixabay.com/photo/2016/04/06/23/27/piglet-1313042_960_720.jpg",
    "https://cdn.pixabay.com/photo/2019/03/10/19/43/pig-4047086_960_720.jpg",
    "https://i.pinimg.com/564x/b2/69/56/b269568f3fd30038b640d96b9d4c207a.jpg",
    "https://i.pinimg.com/564x/48/52/5e/48525e01a66865467382a031d45a4081.jpg",
    "https://i.pinimg.com/564x/f1/42/38/f142387bc3f418da7f4ae56aa347422f.jpg",
    "https://i.pinimg.com/564x/17/3b/7a/173b7a85fdfee91953e2e00a1ad2950a.jpg",
    "https://i.pinimg.com/564x/27/a6/7b/27a67bcd2dfbe7d6a9c910fbb4ddbed0.jpg",
    "https://i.pinimg.com/564x/6d/9f/ce/6d9fcecca7155bc140db4136bf5a95ce.jpg",
    "https://i.pinimg.com/564x/e3/22/1d/e3221d40de5551d69d549d661c99267b.jpg",
    "https://i.pinimg.com/564x/28/09/e0/2809e062b5c659f4094bfa972ed22d7b.jpg",
    "https://i.pinimg.com/564x/77/4b/a1/774ba1ff1603b82d5214e03a0c52aefe.jpg",
    "https://i.pinimg.com/564x/5f/8f/47/5f8f471b896d9a5a59358fd3e025debb.jpg",
    "https://i.pinimg.com/564x/0f/b3/cd/0fb3cd6db9534c5f2c60c3588ec82410.jpg",
    "https://i.pinimg.com/564x/05/91/c3/0591c32ed7d8a864429ef2f323477cfd.jpg",
    "https://i.pinimg.com/564x/f6/31/d7/f631d7f57baad7ebdfefb7f645fa1887.jpg",
    "https://i.pinimg.com/564x/f2/d0/3b/f2d03be0df399702cf413ef3630c6c1b.jpg",
    "https://i.pinimg.com/564x/d3/7b/7e/d37b7eea4ffdcbd96384562a36b7d25a.jpg",
    "https://i.pinimg.com/564x/6b/53/92/6b539254d3f8344774f96dcf3bfe5047.jpg",
    "https://i.pinimg.com/564x/b6/ed/02/b6ed023be37b4dde5ac08296ae66ff15.jpg",
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Grunz! Schweinchen will Kuscheln! :pig_nose: :heart:"
    embed.set_footer(text="https://br.pinterest.com/MiiObst/pigs/")
    embed.set_image(url=random.choice(picture_urls))

    await message.channel.send(embed=embed)
