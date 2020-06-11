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
    "https://i.pinimg.com/564x/82/e7/eb/82e7eb2537e1cbcce20762ac0ff99b96.jpg",
    "https://i.pinimg.com/564x/90/f7/06/90f7062e0cce67581040a90d1458067f.jpg",
    "https://i.pinimg.com/564x/44/08/f4/4408f4144191cbcad8ff24aa10b88ffd.jpg",
    "https://i.pinimg.com/564x/38/6d/c8/386dc8cbd523bb6fbec5a53b7df805b9.jpg",
    "https://i.pinimg.com/564x/ad/82/89/ad82892a50318ddd71f5a01740251aeb.jpg",
    "https://i.pinimg.com/564x/66/2e/b2/662eb26c26986e35ac30d39b4433d931.jpg",
    "https://i.pinimg.com/564x/43/34/0f/43340f6ff1a50a3348eb7fd790e6eef5.jpg",
    "https://i.pinimg.com/564x/1e/97/97/1e979767102f5545f71a5adb8163d6d6.jpg",
    "https://i.pinimg.com/564x/92/e9/c8/92e9c85d7d9a6612945ba52f2716b556.jpg",
    "https://i.pinimg.com/564x/20/53/e9/2053e9a12d99b82c5e2bfa8ef4269fca.jpg",
    "https://i.pinimg.com/564x/2a/92/76/2a92768ce4123a5fcf66b08446ef35c4.jpg",
    "https://i.pinimg.com/564x/7d/7d/6c/7d7d6c262b30eea9963406bf41830398.jpg",
    "https://i.pinimg.com/564x/c9/0e/1c/c90e1cd9ca6ee313001b7ac88617aa07.jpg",
    "https://i.pinimg.com/564x/4a/cc/50/4acc504f78531fcc5864d20bb6b92181.jpg",
    "https://i.pinimg.com/564x/25/27/01/25270130a7821af421c5b9edd80f98c3.jpg",
    "https://i.pinimg.com/564x/85/60/1a/85601a0542825b070208672e46310b3f.jpg",
    "https://i.pinimg.com/564x/0e/a3/f8/0ea3f8ff27130ff6ea4cc9dffbce29ff.jpg",
    "https://i.pinimg.com/564x/b5/3c/63/b53c63afd059f29f62032cdfacf9ce0d.jpg",
    "https://i.pinimg.com/564x/0f/c5/3d/0fc53d13a24aecc6456f52c54178a654.jpg",
    "https://i.pinimg.com/564x/7c/62/69/7c6269ea84086c9d42938c8d4da4563c.jpg",
    "https://i.pinimg.com/564x/e7/35/1d/e7351d5386f982c335392d7dc7535620.jpg",
    "https://i.pinimg.com/564x/52/4d/65/524d65d13b777d4d1a8a350a77d23875.jpg",
    "https://i.pinimg.com/564x/b9/8c/cc/b98ccce62901cf1aa3bca94fa9a990c5.jpg",
    "https://i.pinimg.com/564x/e8/72/93/e872934204514a7034fabdbf8a4e3a41.jpg",
    "https://i.pinimg.com/236x/21/bf/99/21bf99310cf6f6484a6ba3899db03c22.jpg",
    "https://i.pinimg.com/564x/56/cd/a4/56cda4173af5da6f771dd92c13e1ab98.jpg",
    "https://i.pinimg.com/564x/b5/fd/f2/b5fdf288e169cdeb55d9a7fa94c499f9.jpg",
    "https://i.pinimg.com/564x/7d/50/40/7d50400aea50109ed4801e8cae238832.jpg",
    "https://i.pinimg.com/236x/19/63/35/196335abea460f6038049fe5a9baf7e6.jpg",
    "https://i.pinimg.com/564x/f7/2e/78/f72e78f4b962666225f78314fd7be455.jpg",
    "https://i.pinimg.com/564x/cc/86/8b/cc868b438770f98c3a4b025686ab2791.jpg",
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Grunz! Schweinchen will Kuscheln! :pig_nose: :heart:"
    embed.set_footer(text="https://br.pinterest.com/MiiObst/pigs/")
    embed.set_image(url=random.choice(picture_urls))

    await message.channel.send(embed=embed)
