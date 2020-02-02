from sys import argv

text = open(argv[1])

start = end = False
nversi = 0
lines = filter(None, map(str.strip, text))

for line in lines:
    if line == ".POEMA":
        start = True
        titolo = next(lines)
        print(f"  {titolo}\n\n")

    if not start:
        continue

    if line == ".CANTICA":
        cantica = next(lines)
        print(f"  {cantica}\n")

    if line == ".FINE CANTICA":
        print()

    if line == ".CANTO":
        canto = next(lines)
        print(f"  {canto}\n")

    if line == ".FINE CANTO":
        continue

    if line == ".TERZINA":
        versi = next(lines), next(lines), next(lines)
        nversi += 3
        print(f"    {versi[0]}")
        print(f"    {versi[1]}")
        print(f"    {versi[2]}\n")

    if line == ".VERSO":
        verso = next(lines)
        nversi += 1
        print(f"    {verso}\n")

    if line == ".FINE":
        end = True
        break

assert (nversi == 14233)
assert (start is True and end is True)
