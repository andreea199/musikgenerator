sheetDictionary = {}


def make_note_dictionary(mapper):
    with open(mapper, "r") as m:
        for line in m:
            line = line.replace('\n', '')
            data = iter(line.split(":"))

            while True :
                try :
                    nota = next(data)
                    pian = next(data)
                    sheetDictionary[nota] = pian
                except StopIteration:
                    break
    m.close()


def translate_notes(partituri, rezultat):
    with open(partituri, 'r') as f:
        with open(rezultat, 'w') as t:
            for line in f:
                if line == "\n":
                    t.write("\n")
                line = line.replace('\n', '')
                for word in line.split(" "):
                    # if mod == "chords":
                    t.write(sheetDictionary[word] + " ")
                    # elif mod == "notes":
                    #     t.write()

    f.close()
    t.close()
