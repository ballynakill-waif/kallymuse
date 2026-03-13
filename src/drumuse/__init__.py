
from music21 import *
from music21 import chord, percussion

## Defining a drum kit

### Definitions for snare and kick drum
sn = note.Unpitched('C5')
sn.storedInstrument = instrument.SnareDrum()
sn.storedInstrument
bd = note.Unpitched('F4')
bd.storedInstrument = instrument.BassDrum()
# dm = stream.Measure()
# for x in [bd, sn]:
    # dm.append(x)

### Defining the cymbals
#### The high hat
hh = note.Unpitched('f5')
#hh.note = 'F'
#hh.octave = 4
hh.notehead = 'x'
hh.stemDirection = 'up'
#hh.beams = 'up'
#### The ride
ride = note.Unpitched('g5')
#hh.note = 'F'
#hh.octave = 4
ride.storedInstrument = instrument.RideCymbals()
ride.notehead = 'x'
ride.stemDirection = 'up'
# adding lilypond like variables
cymbr = ride

### Defining percussionary chords
tzh = percussion.PercussionChord([hh, sn] )


# Putting it all together by adding classes (factories) to have the functionarlity to create bars
class makeDrums():
    """ makeDrums is a factory for making drum bars in music21

        here is an example using the class to make a simple march beat bar:
            makeDrums().partsDrums( makeDrums().zipDrums([1, 1, 1, 1], [hh, p3, hh, p3], [1, 1, 1, 1], [bd, note.Rest(), bd, note.Rest()]), 1 ).show()
        if we want to save the bar and expand it over multiple bars here is an example of 4 bars:
            mbr = makeDrums().partsDrums( 
                        makeDrums().zipDrums([1, 1, 1, 1], [hh, p3, hh, p3], [1, 1, 1, 1], [bd, note.Rest(), bd, note.Rest()]),
                        4
                        ) # mbr = march beat riff
            mbr.show()


    """
    def __init__(self):
        pass
    def zipDrums(self, values1, objects1, values2=None, objects2=None, iterations=1):
        """ takes given number of list(values) and list(objects), where objects is a list of durations, 
            and turns them into a (polyphony) two part structure.

            this is meant to be used with drums, with the upper voice as(values1, objects1), and the lower as(values2, objects2).

            here is an example, with the drum riff from andy shauf's 'the long throw':
                makeDrums().zipDrums([1, .5, .5, 1, 1], [hh, hh, hh, hh, p3], [1, 3], [bd, note.Rest()], iterations=4).show()
        """
        assert isinstance(iterations, int), 'fatal: iterations parameter is not an integar'
        for x in [values1, values2, objects1, objects2]:
            assert isinstance(x, (type(None), list)), f'fatal: {x} is not a list or NoneType'
        m = stream.Measure()
        v1 = stream.Voice()
        if values2 and objects2:
            v2 = stream.Voice()
        for x in zip(objects1, values1):
            x[0].quarterLength = x[1]
            v1.repeatAppend(x[0], 1)
        m.insert(0, v1)
        if values2 and objects2:
            for x in zip(objects2, values2):
                x[0].quarterLength = x[1]
                v2.repeatAppend(x[0], 1)
            m.insert(0, v2)
        return m
    def partsDrums(self, bar, times):
        ''' takes bar and puts in `stream.Part` with percussion clef x times '''
        riff = stream.Part()
        riff.append(clef.PercussionClef())
        riff.repeatAppend(bar, times)
        return riff
