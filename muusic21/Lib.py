from music21 import *


def play_midi(partituri):
    x = stream.Stream()
    with open(partituri, 'r') as f:
        for line in f:
            for word in line.split(" "):
                nota = note.Note(word)
                x.append(nota)
    x.show('midi')


def read_midi():
     midi.MidiFile.read("D:\\AN3\\Licenta\\translate_partituri\\muusic21\\ColorsHalsey.mid")


def create_xml():
    s = corpus.parse('beethoven/opus18no1/movement1')
    s.show()  # deschide xml


def create_histogram():
    s = corpus.parse('beethoven/opus18no1/movement1')  # beethoven/opus18no1/movement1.mxl
    p = graph.plot.HistogramPitchSpace(s)
    p.run()


def translate_german():
    bach = corpus.parse('bach/bwv295')
    for thisNote in bach.recurse().notes:
        thisNote.addLyric(thisNote.pitch.german)  # traduce in germana
    bach.show()  # xml

