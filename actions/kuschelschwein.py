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
    "https://i.pinimg.com/564x/41/f5/b7/41f5b7df7eb8cece68bc57ac8c9509f8.jpg",
    "https://i.pinimg.com/564x/60/3d/54/603d54d448457a23645275c655c0938b.jpg",
    "https://i.pinimg.com/564x/fc/df/69/fcdf694ef8d6b1481b5c0bd5236c9736.jpg",
    "https://i.pinimg.com/564x/ee/83/66/ee83663046199af8ebfcf98dd1339b86.jpg",
    "https://i.pinimg.com/564x/bf/94/c4/bf94c4fd12a9b81cc61f6bb948ef7865.jpg",
    "https://i.pinimg.com/564x/37/16/bd/3716bd0183f3609463564fa52b083194.jpg",
    "https://i.pinimg.com/564x/e4/74/ae/e474ae22b75d4fe3eb0a517a4b002037.jpg",
    "https://i.pinimg.com/564x/f0/fb/6f/f0fb6f386b7636e05e408c3ad315d287.jpg",
    "https://i.pinimg.com/564x/40/04/bf/4004bf0e1bacd60345267b9bfe39b22e.jpg",
    "https://i.pinimg.com/564x/75/2c/f4/752cf4052d2b34b25acf0196af5bffb5.jpg",
    "https://i.pinimg.com/564x/ae/06/8f/ae068f6aa8bf80d3eab0e6d8e9857086.jpg",
    "https://i.pinimg.com/564x/37/91/42/379142c384136e5d3f1a08806de5921d.jpg",
    "https://i.pinimg.com/564x/fe/d7/26/fed726ce474bd58709895a1ce49147c8.jpg",
    "https://i.pinimg.com/564x/22/18/3d/22183dff11648697e1376f108f25be85.jpg",
    "https://i.pinimg.com/564x/78/96/f3/7896f37b0172520716f4498b1ae8dccf.jpg",
    "https://i.pinimg.com/564x/8f/23/8f/8f238f5d08e50994c518bca3345eacaf.jpg",
    "https://i.pinimg.com/564x/48/5e/c0/485ec009860960317b1e57763a420bdd.jpg",
    "https://i.pinimg.com/564x/b3/ed/03/b3ed03e4c978ddd3f03bdccab5178201.jpg",
    "https://i.pinimg.com/564x/28/f9/3b/28f93bde0a421fd89a9ad4f45dc5e1b3.jpg",
    "https://i.pinimg.com/564x/4f/0c/e2/4f0ce2102618c5c4e025f885e0c96c87.jpg",
    "https://i.pinimg.com/564x/63/ae/ff/63aeffe0b226c8bc895e8334fb1c637e.jpg",
    "https://i.pinimg.com/564x/ce/90/93/ce9093d302c4bc43517bdc10986f71eb.jpg",
    "https://i.pinimg.com/564x/fe/69/a6/fe69a6424449f89bf8788a02d21ec0c0.jpg",
    "https://i.pinimg.com/564x/00/85/b5/0085b52cfc9622a7a1f71b5f8e3ebdbb.jpg",
    "https://i.pinimg.com/564x/48/db/bb/48dbbb8f896687970868f1e73eb21dee.jpg",
    "https://i.pinimg.com/564x/00/ec/cf/00eccfb97132079240bde1b51f761e90.jpg",
    "https://i.pinimg.com/564x/d6/ef/9f/d6ef9fa2234db0ad7e8c34b5dd3e41aa.jpg",
    "https://i.pinimg.com/564x/10/56/c2/1056c2b20469021e72907b51f6fb5980.jpg",
    "https://i.pinimg.com/564x/d3/b0/e2/d3b0e2b25146dacb717131455769a9fa.jpg",
    "https://i.pinimg.com/564x/65/8e/9d/658e9df4888064d7c109f2a7c1245239.jpg",
    "https://i.pinimg.com/564x/d6/0c/10/d60c10c05ab2e1d4cb1f136cad1fca35.jpg",
    "https://i.pinimg.com/564x/6e/93/b3/6e93b377c696a184196b1fc9460ec15a.jpg",
    "https://i.pinimg.com/564x/5c/f9/a0/5cf9a00381a940fb4406223b92981f48.jpg",
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Grunz! Schweinchen will Kuscheln! :pig_nose: :heart:"
    embed.set_footer(text="https://br.pinterest.com/MiiObst/pigs/")
    embed.set_image(url=random.choice(picture_urls))

    await message.channel.send(embed=embed)
