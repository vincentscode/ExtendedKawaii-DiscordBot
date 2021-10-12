import random

commands = ["pigfact", "pigfacts"]
requires_mention = False
accepts_mention = False
description = "Schweinchen Fakten!"


async def execute(message):
    e = discord.Embed()
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
        "Als Teacup Pig bezeichnet man Mini-Ferkel (Baby Schweinchen), die in eine Teetasse passen. Es stimmt *nicht*, dass diese Schweinchen so klein bleiben.",
        "Der Mensch und das Schwein haben physiologische und anatomische Ähnlichkeiten. Diese Ähnlichkeiten hat sich der Mensch schon im griechischen Altertum zu Nutze gemacht. Zum Beispiel bei der medizinischen Forschung.",
        "Eines der ersten kleinen Schweinchen Rassen ist das Minnesota-Minischwein, welches in den 1940er Jahren in den USA entwickelt wurde.",
        "Schweine sind Allesfresser und *immer* hungrig. (Sie würden auch Menschen essen.)",
        "Eine Sau kann kann bis zu 16 Nippel haben! Üblich sind 12-14. Stell dir vor du hast 12 Brüste, die an dir runter hängen.",
        "Schweine haben einen besseren Geruchssinn als Hunde. Trüffelschweine suchen Trüffel mit ihrer Nase. :pig_nose:.",
        "Schweinchen können nicht nach oben gucken (wegen der Anatomie ihrer Muskeln im Nacken). Sie können sich aber auf die Seite legen oder auf ihre Hinterbeine stellen, um nach oben zu sehen.", 
        "Wusstest du, dass Metalpig total in Schweinchen vernarrt ist? Sie würde am liebsten Schwweinchen mit Drachen kreuzen und eine Armee aufstellen.",
        "Schweine können sich gegenseitig austricken. So folgen sie gerne ihren Artgenossen, wenn diese auf der Suche nach Nahrung sind, und schnappen ihnen diese dann vor der Nase weg. Diejenigen, die überlistet werden, lernen jedoch, ihr Verhalten zu ändern, damit sie nicht mehr so häufig das Nachsehen haben.",
        "Schweine fühlen wie wir Schmerz, Leid, Freude und Trauer. Sie können auch Mitgefühl mit anderen Schweinen haben, die leiden.",
        "Das Kunekune Schwein ist sehr flauschig. Google es! Los! Überzeuge dich von der Flauschigkeit!",
        
    ]

    response = random.choice(pig_facts)
    e.description = response
    await message.channel.send(embed=e)
