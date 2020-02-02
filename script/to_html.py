from sys import argv
from jinja2 import Environment, FileSystemLoader


text = open(argv[1])

start = end = False
nversi = 0
lines = filter(None, map(str.strip, text))

poema = [
    # {
    #     "titolo": "",
    #     "canti": [
    #         {
    #             "titolo": "",
    #             "versi": []
    #         }
    #     ]
    # }
]

for line in lines:
    if line == ".POEMA":
        start = True
        titolo = next(lines)

    if not start:
        continue

    if line == ".CANTICA":
        cantica = next(lines)
        canti = []
        poema.append({"titolo": cantica, "canti": canti})

    if line == ".FINE CANTICA":
        pass

    if line == ".CANTO":
        canto = next(lines)
        versi = []
        canti.append({"titolo": canto, "versi": versi})

    if line == ".FINE CANTO":
        continue

    if line == ".TERZINA":
        linee = next(lines), next(lines), next(lines)
        nversi += 3
        versi.extend(linee)

    if line == ".VERSO":
        verso = next(lines)
        nversi += 1
        versi.append(verso)

    if line == ".FINE":
        end = True
        break

assert (nversi == 14233)
assert (start is True and end is True)

templates_dirs = ["html_templates"]
if len(argv) > 2:
    templates_dirs.append(argv[2])

loader = FileSystemLoader(templates_dirs)
env = Environment(loader=loader)

html_tpl = env.get_template("poema.html")
print(html_tpl.render(titolo=titolo, poema=poema))
