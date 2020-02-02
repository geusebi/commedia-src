from sys import argv

text = open(argv[1])

root = argv[2]
start = end = False
nversi = 0
lines = filter(None, map(str.strip, text))

for line in lines:
    if line == ".POEMA":
        start = True
        titolo = next(lines)

    if not start:
        continue

    if line == ".CANTICA":
        cantica = next(lines)
        fcantica = open(f"{root}/{cantica.lower()}.tex", "w")
        fcantica.write(f"\\chapter{{{cantica}}}\n\n")

    if line == ".FINE CANTICA":
        fcantica.close()

    if line == ".CANTO":
        canto = next(lines)
        _, numero = canto.split()
        fcantica.write(f"\\input{{{cantica.lower()}/{numero}.tex}}\n")
        fcanto = open(f"{root}/{cantica.lower()}/{numero}.tex", "w")
        fcanto.write(f"\\section{{{canto}}}\n\n")
        fcanto.write(f"\\begin{{verse}}\n")

    if line == ".FINE CANTO":
        fcanto.write(f"\\end{{verse}}\n")
        fcanto.close()

    if line == ".TERZINA":
        versi = next(lines), next(lines), next(lines)
        fcanto.write(f"{versi[0]}\\\\*\n")
        fcanto.write(f"{versi[1]}\\\\*\n")
        fcanto.write(f"{versi[2]}\\\\!\n\n")
        nversi += 3

    if line == ".VERSO":
        verso = next(lines)
        fcanto.write(f"{verso}\\\\\n")
        nversi += 1

    if line == ".FINE":
        end = True
        break

assert (nversi == 14233)
assert (start is True and end is True)
