import sys
from translate import Translate
from muusic21 import Lib
from markovChains import Markov


def main():
    Translate.make_note_dictionary(sys.argv[1])
    Translate.translate_notes(sys.argv[2], sys.argv[3])

    Lib.play_midi(sys.argv[4])
    # Lib.create_histogram()
    # Lib.create_xml()
    # Lib.translate_german()

    Markov.markov_chains(sys.argv[5], sys.argv[6])


if __name__ == "__main__":
    main()


# python Main.py translate/map translate/partituri translate/rezultatTranslate muusic21/partituri
# markovChains/partituri markovChains/rezultat
