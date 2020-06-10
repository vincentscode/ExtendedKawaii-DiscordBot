import random

commands = ["pigfact", "pigfacts"]
requires_mention = False
accepts_mention = False
description = "Schweinchen Fakten!"


async def execute(message):
    pig_facts = [
        "Schweine schwitzen gar nicht, sie haben nur wenige Schweißdrüsen auf der Nase. ",
        "Schweine sulen sich im Schlamm um sich vor Insekten und Sonne zu schützen. Sie sind genauso anfällig auf Sonnenbrand wie wir.",
        "Die kleinste Schweinerasse ist das Göttinger Minischwein.",
        "Das Göttinger Minischwein wiegt ausgewachsen um die 35kg.",
        "Schweine sind sehr intelligent. Sie können Tricks lernen wie Hunde, kennen ihren Namen, bilden komplexe soziale Einheiten und lernen voneinander.",
        "Anders als es das Klischee sagt, sind Schweine saubere Tiere.",
        "Schweine träumen! Sie mögen es Nase an Nase zu schlafen und angekuschelt aneinander zu liegen.",
        "Das Grunzen und Quieken hat tatsächlich eine Bedeutung, mehr als 20 ihrer Laute wurde für verschiedene Sittuationen differenziert.",
        "Schweine werden intelligenter eingeschätzt als 3 jährige Menschenkinder oder Hunde.",
        "Ausgewachsene Schweine können Geschwindigkeiten von bis zu 16 Kilometern pro Stunde erreichen.",
        "Schweine essen am liebsten langsam und genussvoll, sie sind also Genießer. Wenn man wie ein Schwein isst, isst man also mit Genuss. ;)",
        "Schweine haben ein ausgezeichnetes Gedächtnis.",
        "Schweine haben einen ausgeprägten Orientierungssinn und finden ihren Weg nach Hause auch über große Distanzen.",
        "Schweine sind Optimisten. Sie sind sehr neugierig, aufgeschlossen und enthusiastisch. Wenige Tiere erkunden die Welt wie sie.",
        "Schweine können so tapfer sein, dass sie anderen das Leben retten würden, auch Menschenfreunden.",
        "Die Lebenserwartung für ein Hausschwein beträgt 15-20 Jahre.",
        "Schweine gehören zur Ordnung der Paarhufer.",
    ]

    response = random.choice(pig_facts)
    await message.channel.send(response)
