import random

commands = ["pigjoke", "pigjokes"]
requires_mention = False
accepts_mention = False
description = "Schweinchen Witze!"


async def execute(message):
    pig_jokes = [
        "I like pig butts and I cannot lie.",
        "Ein Leben ohne Schwein ist möglich, aber sinnlos",
        "Wie heißt ein kleines schwäbisches Schwein, das um Hilfe ruft? ....... Notrufsäule",
        "Ich brauche keine Therapie, ich muss nur zu meinem Schweinchen.",
        "Es wackelt spät durch Nacht und Wind, ein Schweinchen, das lacht und singt. Es wünscht nur eines, das ist klar: Alles Gute im neuen Jahr!",
        "Zwei Schweinchen sitzen frustriert nebeneinander, sagt das eine: Ist doch eh Wurst was aus uns wird...",
        "Kommt ein kleines Schweinchen zu einer Steckdose und sagt: Wer hat dich denn da eingemauert? :(",
        "Kun Grunzius sprach: Grunz grunz grunz grunz grunz!",
        "Keep Calm and Grunz on.",
        "Da guckt ein Schwein ganz überzeugt: Das ist wahrschweinlich!",
        "Ich will keine Meerjungfrau sein, sondern ein Meerjungschweinchen.",
        "Man gebe mir ein Schwein.",
        "Ich denke nicht schmutzig, mein Name ist einfach Ferkel.",
        "Ein Leben ist nichts ohne Schweinchen."
        "Grunz grunz grunz grunz grunz.",
        "Das passt wie Schwein auf Eimer.",
        "Unter aller Sau ist nichts schlechtes, denn Schweinchen legen die Messlatte ganz schön hoch.",

    ]

    response = random.choice(pig_jokes)
    await message.channel.send(response)
