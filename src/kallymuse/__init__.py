"""
# kallymuse

kallymuse is a collection of classes, functions, and objects envisioned to aid a composer in conveying ideas quickly in
jupyter notebooks using music21.

## Chord Objects

To accomplish this chord objects for standard guitar chords are available for all 12 tones (A, A#, Bb, B, B#, C, C#, D, D#, E, E#, F, F#, G, G#)
as variables or attributes of the module. Of course the hash character is a special character in python so in naming
sharp chords, such as G#Maj, we replace the '#' with 'h'.

GhMaj.show('text') should return:
    <music21.chord.Chord G#2 D#3 G#3 B#3 D#4>

The lowest chord available as such is Emaj.
Using Emaj.show('text') should give:







## Systemized diminished chords

There are many types of diminished chords, and ways of playing them, and their voicing are consisently different
depending on how what instruments they are voiced with. However there are three ways that I use consisently enough
to have a way to reference them.

### Diminished with Capital Letter

These are for the diminished chords with this shape:
This would be a diminished chord in the E shape of CAGED.


```Fdim56, or dimF
e|-1
B|-3
G|-4
D|-3
A|-x
E|-1
```
"""

from music21 import *

# Standard Guitar Chords of the Major Quality (Great Octave)
Emaj, Ehmaj = chord.Chord("E2 b2 e3 g#3 b3 e4"), chord.Chord("E#2 b#2 e#3 g##3 b#3 e#4") 
Fbmaj, Fmaj, Fhmaj = chord.Chord("F-2 C-3 f-3 a-3 c-4 f-4"), chord.Chord("F2 c3 f3 a3 c4 f4"), chord.Chord("F#2 c#3 f#3 a#3 c#4 f#4")
## G Major, G# Major, and A Major
Gmaj, Ghmaj, Amaj = chord.Chord('G2 D3 G3 b3 d4 g4'), chord.Chord('G#2 D#3 G#3 b#3 d#4 g#4'), chord.Chord('A2 e3 a3 c#4 e4')
Gbmaj = chord.Chord('G-2 D-3 G-3 b-3 d-4 g-4')
Abmaj = chord.Chord('A-2 e-3 a-3 c4 e-4')

## Bb Major, and B major
Bbmaj = chord.Chord('B-2 f3 b-3 d4 f4')
Bmaj = chord.Chord("B2 f#3 b3 d#4 f#4")
## C through to D# <- which goes to E
Cmaj, Chmaj, Dmaj, Dhmaj = chord.Chord("C3 G3 c4 e4 g4 c5"), chord.Chord("C#3 g#3 c#4 e4 g#4 c#5"), chord.Chord("D3 A3 d4 f#4 a4 d5"), chord.Chord("D#3 A#3 d#4 f##4 a#4 d#5")
Cbmaj, Dbmaj, Ebmaj = chord.Chord("C-3 g-3 c-4 e4 g-4 c-5"), chord.Chord("D-3 A-3 d-4 f--4 a-4 d-5"), chord.Chord("E-3 B-3 E-4 g4 B-4 E-5")

# Suspended Great Octave
Emajadd6, Fmajadd6 = chord.Chord(" E2 B2 G#3 C#4 "), chord.Chord("F2 C3 A3 D4") 
Fhmajadd6, Gmajadd6 = chord.Chord("F#2 C#3 A#3 D#4"), chord.Chord("G2 D3 B3 E4")


# Standard Guitar Chords of the Minor Quality
Emin, Ehmin = chord.Chord("E2 b2 e3 g3 b3 e4"), chord.Chord("E#2 b#2 e#3 g#3 b#3 e#4") 
Fbmin, Fmin, Fhmin = chord.Chord("F-2 C-3 f-3 a3 c-4 f-4"), chord.Chord("F2 c3 f3 a-3 c4 f4"), chord.Chord("F#2 c#3 f#3 a3 c#4 f#4")
## G Minor, G# Minor, and A Minor
Gmin, Ghmin, Amin = chord.Chord('G2 D3 G3 b-3 d4 g4'), chord.Chord('G#2 D#3 G#3 b3 d#4 g#4'), chord.Chord('A2 e3 a3 c4 e4')
## Bb Minor, and B minor
Bbmin = chord.Chord('B-2 f3 b-3 d-4 f4')
Bmin = chord.Chord("B2 f#3 b3 d4 f#4")
## C through to D# <- which goes to E
Cmin, Chmin, Dmin, Dhmin = chord.Chord("C3 G3 c4 e-4 g4 c5"), chord.Chord("C#3 g#3 c#4 e4 g#4 c#5"), chord.Chord("D3 A3 d4 f4 a4 d5"), chord.Chord("D#3 A#3 d#4 f#4 a#4 d#5")

# Standard Guitar Chords of the diminished Quality (Great~ Octave)
# E to G
dimE, dimF, dimFh, dimG = chord.Chord("E2 e3 a#3 c#4 e4"), chord.Chord("F2 f3 b3 d4 f4"),chord.Chord("F#2 f#3 b#3 d#4 f#4"), chord.Chord('G2 g3 c#3 e4 g4')
# G# to A#
dimGh, dimA, dimAh = chord.Chord('G#2 g#3 d4 f4 g#4'), chord.Chord("A2 a3 d#4 f#4 a4"), chord.Chord("A#2 a#3 d##4 f##4 a#4")
dimBb = chord.Chord("B-2 B-3 e4 g4 b-4")
# B to D sharp (Dh)
dimB, dimC, dimCh, dimD, dimDh = chord.Chord("B2 b3 e#4 g#4 b4"), chord.Chord("C3 c4 f#4 a4 c5"), chord.Chord("C#3 c#4 f##4 a#4 c#5"), chord.Chord("D3 d4 g#4 b4 d5"), chord.Chord("D#3 d#4 g##4 b#4 d#5")

# Standard Guitar Chord of the major quality (small~ octave)
#
# cipher <name><quality><inversion>: inversion 35 refers to C in CAGED
#
# A to B
amaj, ahmaj, bmaj, bhmaj = chord.Chord('A2 E3 A3 C#4'), chord.Chord('A#2 E#3 A#3 C##4'), chord.Chord('B2 F#3 B3 D#4'), chord.Chord('B#2 F##3 B#3 D##4')
abmaj, bbmaj = None, None
# C to D
cmaj35, cmaj, chmaj, dmaj, dhmaj = chord.Chord('C3 E3 G3 C4 E4'), chord.Chord('C3 G3 C4 E4 G4'), chord.Chord('C#3 G#3 C#4 E#4'), chord.Chord('D3 A3 D4 F#4'), chord.Chord('D#3 A#3 D#4 F##4')
# E to F
ebmaj, emaj, ehmaj, fmaj, fhmaj = chord.Chord('E-3 B-3 E-4 G4'), chord.Chord('E3 B3 E4 G#4'), chord.Chord('E#3 B#3 E#4 G##4'), chord.Chord('F3 C4 F4 A4'), chord.Chord('F#3 C#4 F#4 A#4')
# G
gbmaj, gmaj, ghmaj = chord.Chord('G-3 D-4 G-4 B-4'), chord.Chord('G3 D4 G4 B4'), chord.Chord('G#3 D#4 G#4 B#4')

# Half diminished A in CAGED voicing
# A to B
ahalfdim, bbhalfdim, bhalfdim = chord.Chord(' A2 E-3 G3 C4 '), chord.Chord('B-2 E3 G#3 C#4'), chord.Chord('B2 F3 A3 D4')
# C to D
chalfdim, chhalfdim, dhalfdim = chord.Chord(' C3 F#3 B-3 E-4'), chord.Chord('C#3 G3 B3 E4'), chord.Chord('D3 G#3 C4 F4')
# E to F
ebhalfdim, ehalfdim, fhalfdim, fhhalfdim = chord.Chord('E-3 A3 C#4 F#4'), chord.Chord(' E3 B-3 D4 G4'), chord.Chord('F3 B3 E-4 G#4'), chord.Chord('F#3 C4 E4 A4')
# G
ghalfdim, ghhalfdim, _ahalfdim = chord.Chord('G3 C#4 F4 B-4'), chord.Chord('G#3 D4 F#4 B4'), chord.Chord('A3 E-4 G4 C5')

# Add 9 chords
# B
b46add9 = chord.Chord('F#2 D#3 A3 C#4')
# C to D
c46add9, ch46add9, d46add9, dh46add9 = chord.Chord('G2 E3 B-3 D4'), chord.Chord(' G#2 F3 B3 E-4'), chord.Chord('A2 F#3 C4 E4'), chord.Chord('B-2 G3 C#4 F4')
# E to F
e46add9, f46add9 = chord.Chord('B2 G#3 D4 F#4'), chord.Chord('C3 A3 E-4 G4')
# G to A
fh46add9, g46add9, gh46add9, a46add9, bb46add9 = chord.Chord('C#3 B-3 E4 G#4'), chord.Chord('D3 B3 F4 A4'), chord.Chord('D#3 B#4 F#4 A#4'), None, chord.Chord('F3 D4 A-4 C5') 

# Suspended chords (add6)
# A to B
amajadd6 = chord.Chord( 'A2 E3 C#4 F#4' )
bmajadd6, bbmajadd6 = chord.Chord("B2 F#3 E-4 G#4"), chord.Chord( "B-2 F3 D4 G4")
# C to D
cmajadd6 = chord.Chord('C3 G3 E4 A4')
chmajadd6 = chord.Chord('C#3 G#3 F4 B-4')
dmajadd6 = chord.Chord('D3 A3 F#4 B4')
# E to F
#
# G
ebmajadd6 = chord.Chord('E-3 B-3 G4 C5')



# Standard Guitar Chords of the diminished Quality (Small~ Octave)
adim, bdim, bbdim, cdim, chdim = chord.Chord('A2 E-2 A3 C3'), chord.Chord('B2 F2 B3 D3'), chord.Chord('B-2 F-3 B-3 D-4'), chord.Chord('C3 G-3 C4 E-4'), chord.Chord('C#3 G3 C#4 E4')


# Next I will add a class containing classes of chords where chord fingerings are stored attributes
# This gives the user the ability to call common chords from methods `Emaj.Cshape` for `x 7 6 4 5 4 x` for instance.
class GuitarChords():

    """ 
    # GuitarChords contains classes that sort guitar chords by common fingerings or shapes
    # This gives the user the ability to call common chords from methods `Emaj.Cshape` for `x 7 6 4 5 4 x` for instance. 
    """

    def __init__(self):
        """TODO: to be defined. """
        pass
    # maj
    class Ebmaj():
        def __init__(self):
            pass
    class Emaj():
        def __init__(self):
            self.Cshape = chord.Chord('E2 E3 G#3 B3 E4 G#4', tab='0 7 6 4 5 4')
            self.Eshape = chord.Chord("E2 b2 e3 g#3 b3 e4", tab='0 2 2 1 0 0')
    class Ehmaj():
        def __init__(self):
            self.Eshape = chord.Chord("E#2 b#2 e#3 g##3 b#3 e#4", tab='1 3 3 2 1 1')
    class Fbmaj():
        def __init__(self):
            self.Eshape = chord.Chord("F-2 C-3 f-3 a-3 c-4 f-4", tab='0 2 2 1 0 0')
    class Fmaj():
        def __init__(self):
            self.Eshape = chord.Chord("F2 c3 f3 a3 c4 f4", tab='1 3 3 2 1 1')
    class Fhmaj():
        def __init__(self):
            self.Eshape =  chord.Chord("F#2 c#3 f#3 a#3 c#4 f#4", tab='2 4 4 3 2 2')
    class Gbmaj():
        def __init__(self):
            pass
    class Gmaj():
        def __init__(self):
            self.Eshape = chord.Chord('G2 D3 G3 b3 d4 g4', tab='3 5 5 4 3 3')
    class Ghmaj():
        def __init__(self):
            self.Eshape = chord.Chord('G#2 D#3 G#3 b#3 d#4 g#4', tab='4 6 6 5 4 4')
    class Abmaj():
        def __init__(self):
            self.Eshape = chord.Chord('A-2 e-3 a-3 c4 e-4 a-5', tab='4 6 6 5 4 4')
    class Amaj():
        def __init__(self):
            self.Eshape = chord.Chord('A2 e3 a3 c#4 e4 a5', tab='5 7 7 6 5 5')
    class Ahmaj():
        def __init__(self):
            self.Eshape = None
    class Bbmaj():
        def __init__(self):
            self.Ashape = chord.Chord('B-2 f3 b-3 d4 f4', tab='x 1 3 3 3 1')
            self.Eshape = chord.Chord('B-2 f3 b-3 d4 f4 B-4', tab='6 8 8 7 6 6')
    class Bmaj():
        def __init__(self):
            self.Ashape = chord.Chord("B2 f#3 b3 d#4 f#4", tab='x 2 4 4 4 2')
            self.Eshape = chord.Chord("B2 f#3 b3 d#4 f#4 B5", tab='7 9 9 8 7 7')
    class Cbmaj():
        def __init__(self):
            self.Eshape = chord.Chord("C-3 G-3 c-4 e-4 g-4 c-5", tab='7 9 9 8 7 7')
    class Cmaj():
        def __init__(self):
            self.Cshape = chord.Chord('C3 E3 G3 c4 e4', tab='x 3 2 0 1 0')
            self.Ashape = chord.Chord("C3 G3 c4 e4 g4", tab='x 3 5 5 5 3')
            self.Eshape = chord.Chord("C3 G3 c4 e4 g4 c5", tab='8 10 10 9 8 8')
    class Chmaj():
        def __init__(self):
            self.Eshape = chord.Chord("C#3 g#3 c#4 e4 g#4 c#5", tab='9 11 11 10 9 9')
    class Dbmaj():
        def __init__(self):
            self.Eshape = chord.Chord("D-3 A-3 d-4 f4 a-4 d-5", tab='9 11 11 10 9 9')
    class Dmaj():
        def __init__(self):
            self.Eshape = chord.Chord("D3 A3 d4 f#4 a4 d5", tab='10 12 12 11 10 10')
    class Dhmaj():
        def __init__(self):
            self.Eshape = chord.Chord("D#3 A#3 d#4 f##4 a#4 d#5", tab='11 13 13 12 11 11')

    # min
    class Ebmin():
        def __init__(self):
            self.Eshape = None
    class Emin():
        def __init__(self):
            self.Eshape = None
    class Fbmin():
        def __init__(self):
            self.Eshape = None
    class Fmin():
        def __init__(self):
            self.Eshape = None
    class Fhmin():
        def __init__(self):
            self.Eshape = None
    class Gbmin():
        def __init__(self):
            self.Eshape = chord.Chord('G#2 D#3 G#3 b3 d#4 g#4')
    class Gmin():
        def __init__(self):
            self.Ashape = chord.Chord('D3 G3 D4 G4 B-4 D5', tab='10 10 12 12 11 10')
            self.Gshape = chord.Chord('G2 B-2 D3 B-3 D4', tab='3 1 0 3 3 x')
            self.Eshape = chord.Chord('G2 D3 G3 b-3 d4 g4', tab='3 5 5 3 3 3')
            self.Dshape = chord.Chord('G3 d4 g4 b-4', tab='x x 5 7 8 6')
    class Ghmin():
        def __init__(self):
            pass
    class Abmin():
        def __init__(self):
            pass
    class Amin():
        def __init__(self):
            self.Ashape = chord.Chord('A2 e3 a3 c4 e4', tab='x 0 2 2 1 0')
            self.Eshape = chord.Chord('A2 e3 a3 c4 e4 a4', tab='5 7 7 5 5 5')
            self.Dshape = chord.Chord('a3 e4 a4 c5', tab='x x 5 7 10 8')
            self.Dshape6 = chord.Chord('c4 e4 a4 c5', tab='x x 5 7 10 8')
    class Ahmin():
        def __init__(self):
            pass
    class Bbmin():
        def __init__(self):
            self.Ashape = chord.Chord('B-2 f3 b-3 d-4 f4')
    class Bmin():
        def __init__(self):
            self.Ashape = chord.Chord("B2 f#3 b3 d4 f#4")
    class Cbmin():
        def __init__(self):
            pass
    class Cmin():
        def __init__(self):
            self.Eshape = chord.Chord("C3 G3 c4 e-4 g4 c5", tab='8 10 10 8 8 8')
    class Chmin():
        def __init__(self):
            self.Eshape = chord.Chord("C#3 g#3 c#4 e4 g#4 c#5", tab='9 11 11 9 9 9')
    class Dbmin():
        def __init__(self):
            pass
    class Dmin():
        def __init__(self):
            self.Eshape = chord.Chord("D3 A3 d4 f4 a4 d5", tab='10 12 12 10 10 10')
    class Dhmin():
        def __init__(self):
            self.Eshape = chord.Chord("D#3 A#3 d#4 f#4 a#4 d#5", tab='11 13 13 11 11 11')
            self.Ashape = chord.Chord("D#3 A#3 d#4 f#4 a#4", tab='x 6 8 8 7 6')
    # dim
    class Ebdim():
        def __init__(self):
            pass
    class Edim():
        def __init__(self):
            pass
    class Fbdim():
        def __init__(self):
            pass
    class Fdim():
        def __init__(self):
            pass
    class Fhdim():
        def __init__(self):
            pass
    class Gbdim():
        def __init__(self):
            pass
    class Gdim():
        def __init__(self):
            self.Cshape = chord.Chord('d-3 g3 b-3 d-4', tab='9 10 8 6 x x'  )
            self.Ashape = chord.Chord('d-3 d-4 g4 b-4 d-5', tab='9 x 11 12 11 9' )
            self.Gshape = None
            self.Eshape = chord.Chord('G2 D-2 G3 B-3', tab='3 4 5 3 x x')
            self.Dshape = None
    class dimG():
        def __init__(self):
            self.Ashape = chord.Chord('G2 g3 c#3 e4 g4', tab='3 x 5 6 5 3')
            self.Gshape = chord.Chord('G2 e3 b-3 d-4', tab='3 x 2 3 2 x')
            self.Eshape = chord.Chord('d-3 g3 d-4 f-4', tab='9 10 11 12 x x')
    class Ghdim():
        def __init__(self):
            pass
    class Abdim():
        def __init__(self):
            pass
    class Adim():
        def __init__(self):
            pass
    class Ahdim():
        def __init__(self):
            pass
    class Bbdim():
        def __init__(self):
            pass
    class Bdim():
        def __init__(self):
            pass
    class Cbdim():
        def __init__(self):
            pass
    class Cdim():
        def __init__(self):
            pass
    class Chdim():
        def __init__(self):
            pass
    class Dbdim():
        def __init__(self):
            pass
    class Ddim():
        def __init__(self):
            pass
    class Dhdim():
        def __init__(self):
            pass
    # aug
    class Ebaug():
        def __init__(self):
            pass
    class Eaug():
        def __init__(self):
            pass
    class Fbaug():
        def __init__(self):
            pass
    class Faug():
        def __init__(self):
            pass
    class Fhaug():
        def __init__(self):
            pass
    class Gbaug():
        def __init__(self):
            pass
    class Gaug():
        def __init__(self):
            pass
    class Ghaug():
        def __init__(self):
            pass
    class Abaug():
        def __init__(self):
            pass
    class Aaug():
        def __init__(self):
            pass
    class Ahaug():
        def __init__(self):
            pass
    class Bbaug():
        def __init__(self):
            pass
    class Baug():
        def __init__(self):
            pass
    class Cbaug():
        def __init__(self):
            pass
    class Caug():
        def __init__(self):
            pass
    class Chaug():
        def __init__(self):
            pass
    class Dbaug():
        def __init__(self):
            pass
    class Daug():
        def __init__(self):
            pass
    class Dhaug():
        def __init__(self):
            pass
    # 5
    class Eb5():
        def __init__(self):
            pass
    class E5():
        def __init__(self):
            pass
    class Fb5():
        def __init__(self):
            pass
    class F5():
        def __init__(self):
            pass
    class Fh5():
        def __init__(self):
            pass
    class Gb5():
        def __init__(self):
            pass
    class G5():
        def __init__(self):
            pass
    class Gh5():
        def __init__(self):
            pass
    class Ab5():
        def __init__(self):
            pass
    class A5():
        def __init__(self):
            self.Eshape = chord.Chord('A2 E2')
    class Ah5():
        def __init__(self):
            pass
    class Bb5():
        def __init__(self):
            pass
    class B5():
        def __init__(self):
            pass
    class Cb5():
        def __init__(self):
            pass
    class C5():
        def __init__(self):
            pass
    class Ch5():
        def __init__(self):
            pass
    class Db5():
        def __init__(self):
            pass
    class D5():
        def __init__(self):
            pass
    class Dh5():
        def __init__(self):
            pass
    # 7
    class Eb7():
        def __init__(self):
            pass
    class E7():
        def __init__(self):
            pass
    class Fb7():
        def __init__(self):
            pass
    class F7():
        def __init__(self):
            pass
    class Fh7():
        def __init__(self):
            pass
    class Gb7():
        def __init__(self):
            pass
    class G7():
        def __init__(self):
            self.Ashape = chord.Chord('D3 G3 D4 F4 B4 D5', tab='10 10 12 10 12 10')
            self.Gshape = chord.Chord('G2 B2 F3 G3 B3 F4', tab='3 2 3 0 0 1')
            self.Eshape = chord.Chord('G2 D3 G3 b-3 d4 g4', tab='3 5 5 3 3 3')
            self.Dshape = chord.Chord('G3 d4 g4 b-4', tab='x x 5 7 8 6')
    class Gh7():
        def __init__(self):
            pass
    class Ab7():
        def __init__(self):
            pass
    class A7():
        def __init__(self):
            pass
    class Ah7():
        def __init__(self):
            pass
    class Bb7():
        def __init__(self):
            pass
    class B7():
        def __init__(self):
            pass
    class Cb7():
        def __init__(self):
            pass
    class C7():
        def __init__(self):
            pass
    class Ch7():
        def __init__(self):
            pass
    class Db7():
        def __init__(self):
            pass
    class D7():
        def __init__(self):
            pass
    class Dh7():
        def __init__(self):
            pass
    # maj7
    class Ebmaj7():
        def __init__(self):
            pass
    class Emaj7():
        def __init__(self):
            pass
    class Fbmaj7():
        def __init__(self):
            pass
    class Fmaj7():
        def __init__(self):
            pass
    class Fhmaj7():
        def __init__(self):
            pass
    class Gbmaj7():
        def __init__(self):
            pass
    class Gmaj7():
        def __init__(self):
            pass
    class Ghmaj7():
        def __init__(self):
            pass
    class Abmaj7():
        def __init__(self):
            pass
    class Amaj7():
        def __init__(self):
            pass
    class Ahmaj7():
        def __init__(self):
            pass
    class Bbmaj7():
        def __init__(self):
            pass
    class Bmaj7():
        def __init__(self):
            pass
    class Cbmaj7():
        def __init__(self):
            pass
    class Cmaj7():
        def __init__(self):
            pass
    class Chmaj7():
        def __init__(self):
            pass
    class Dbmaj7():
        def __init__(self):
            pass
    class Dmaj7():
        def __init__(self):
            pass
    class Dhmaj7():
        def __init__(self):
            pass
    # min7
    class Ebmin7():
        def __init__(self):
            pass
    class Emin7():
        def __init__(self):
            pass
    class Fbmin7():
        def __init__(self):
            pass
    class Fmin7():
        def __init__(self):
            pass
    class Fhmin7():
        def __init__(self):
            pass
    class Gbmin7():
        def __init__(self):
            pass
    class Gmin7():
        def __init__(self):
            pass
    class Ghmin7():
        def __init__(self):
            pass
    class Abmin7():
        def __init__(self):
            pass
    class Amin7():
        def __init__(self):
            pass
    class Ahmin7():
        def __init__(self):
            pass
    class Bbmin7():
        def __init__(self):
            pass
    class Bmin7():
        def __init__(self):
            pass
    class Cbmin7():
        def __init__(self):
            pass
    class Cmin7():
        def __init__(self):
            pass
    class Chmin7():
        def __init__(self):
            pass
    class Dbmin7():
        def __init__(self):
            pass
    class Dmin7():
        def __init__(self):
            pass
    class Dhmin7():
        def __init__(self):
            pass
    # minmaj7
    class Ebminmaj7():
        def __init__(self):
            pass
    class Eminmaj7():
        def __init__(self):
            pass
    class Fbminmaj7():
        def __init__(self):
            pass
    class Fminmaj7():
        def __init__(self):
            pass
    class Fhminmaj7():
        def __init__(self):
            pass
    class Gbminmaj7():
        def __init__(self):
            pass
    class Gminmaj7():
        def __init__(self):
            pass
    class Ghminmaj7():
        def __init__(self):
            pass
    class Abminmaj7():
        def __init__(self):
            pass
    class Aminmaj7():
        def __init__(self):
            pass
    class Ahminmaj7():
        def __init__(self):
            pass
    class Bbminmaj7():
        def __init__(self):
            pass
    class Bminmaj7():
        def __init__(self):
            pass
    class Cbminmaj7():
        def __init__(self):
            pass
    class Cminmaj7():
        def __init__(self):
            pass
    class Chminmaj7():
        def __init__(self):
            pass
    class Dbminmaj7():
        def __init__(self):
            pass
    class Dminmaj7():
        def __init__(self):
            pass
    class Dhminmaj7():
        def __init__(self):
            pass
    # halfdim
    class Ebhalfdim():
        def __init__(self):
            pass
    class Ehalfdim():
        def __init__(self):
            pass
    class Fbhalfdim():
        def __init__(self):
            pass
    class Fhalfdim():
        def __init__(self):
            pass
    class Fhhalfdim():
        def __init__(self):
            pass
    class Gbhalfdim():
        def __init__(self):
            pass
    class Ghalfdim():
        def __init__(self):
            pass
    class Ghhalfdim():
        def __init__(self):
            pass
    class Abhalfdim():
        def __init__(self):
            pass
    class Ahalfdim():
        def __init__(self):
            pass
    class Ahhalfdim():
        def __init__(self):
            pass
    class Bbhalfdim():
        def __init__(self):
            pass
    class Bhalfdim():
        def __init__(self):
            self.Ashape = chord.Chord('B2 F3 A3 D4', tab='x 2 3 2 3 x')
            # CAGED doesn't cover all the voicings of the guitar and for each shape
            # there are several voicings. I think that it could be beneficial to cover
            # them via function but have no concret idea ATM.
    class Cbhalfdim():
        def __init__(self):
            pass
    class Chalfdim():
        def __init__(self):
            pass
    class Chhalfdim():
        def __init__(self):
            pass
    class Dbhalfdim():
        def __init__(self):
            pass
    class Dhalfdim():
        def __init__(self):
            pass
    class Dhhalfdim():
        def __init__(self):
            pass
    # dim5
    class Ebdim5():
        def __init__(self):
            pass
    class Edim5():
        def __init__(self):
            pass
    class Fbdim5():
        def __init__(self):
            pass
    class Fdim5():
        def __init__(self):
            pass
    class Fhdim5():
        def __init__(self):
            pass
    class Gbdim5():
        def __init__(self):
            pass
    class Gdim5():
        def __init__(self):
            self.Gshape = chord.Chord('G2 G3 d-4 g4', tab='3xx023')
    class Ghdim5():
        def __init__(self):
            pass
    class Abdim5():
        def __init__(self):
            pass
    class Adim5():
        def __init__(self):
            pass
    class Ahdim5():
        def __init__(self):
            pass
    class Bbdim5():
        def __init__(self):
            pass
    class Bdim5():
        def __init__(self):
            pass
    class Cbdim5():
        def __init__(self):
            pass
    class Cdim5():
        def __init__(self):
            pass
    class Chdim5():
        def __init__(self):
            pass
    class Dbdim5():
        def __init__(self):
            pass
    class Ddim5():
        def __init__(self):
            pass
    class Dhdim5():
        def __init__(self):
            pass
    # dim7
    class Ebdim7():
        def __init__(self):
            pass
    class Edim7():
        def __init__(self):
            pass
    class Fbdim7():
        def __init__(self):
            pass
    class Fdim7():
        def __init__(self):
            pass
    class Fhdim7():
        def __init__(self):
            pass
    class Gbdim7():
        def __init__(self):
            pass
    class Gdim7():
        def __init__(self):
            pass
    class Ghdim7():
        def __init__(self):
            pass
    class Abdim7():
        def __init__(self):
            pass
    class Adim7():
        def __init__(self):
            pass
    class Ahdim7():
        def __init__(self):
            pass
    class Bbdim7():
        def __init__(self):
            pass
    class Bdim7():
        def __init__(self):
            pass
    class Cbdim7():
        def __init__(self):
            pass
    class Cdim7():
        def __init__(self):
            pass
    class Chdim7():
        def __init__(self):
            pass
    class Dbdim7():
        def __init__(self):
            pass
    class Ddim7():
        def __init__(self):
            pass
    class Dhdim7():
        def __init__(self):
            pass
    # sus4
    class Ebsus4():
        def __init__(self):
            pass
    class Esus4():
        def __init__(self):
            pass
    class Fbsus4():
        def __init__(self):
            pass
    class Fsus4():
        def __init__(self):
            pass
    class Fhsus4():
        def __init__(self):
            pass
    class Gbsus4():
        def __init__(self):
            pass
    class Gsus4():
        def __init__(self):
            pass
    class Ghsus4():
        def __init__(self):
            pass
    class Absus4():
        def __init__(self):
            pass
    class Asus4():
        def __init__(self):
            pass
    class Ahsus4():
        def __init__(self):
            pass
    class Bbsus4():
        def __init__(self):
            pass
    class Bsus4():
        def __init__(self):
            pass
    class Cbsus4():
        def __init__(self):
            pass
    class Csus4():
        def __init__(self):
            pass
    class Chsus4():
        def __init__(self):
            pass
    class Dbsus4():
        def __init__(self):
            pass
    class Dsus4():
        def __init__(self):
            pass
    class Dhsus4():
        def __init__(self):
            pass
    # susb4
    class Ebsusb4():
        def __init__(self):
            pass
    class Esusb4():
        def __init__(self):
            pass
    class Fbsusb4():
        def __init__(self):
            pass
    class Fsusb4():
        def __init__(self):
            pass
    class Fhsusb4():
        def __init__(self):
            pass
    class Gbsusb4():
        def __init__(self):
            pass
    class Gsusb4():
        def __init__(self):
            pass
    class Ghsusb4():
        def __init__(self):
            pass
    class Absusb4():
        def __init__(self):
            pass
    class Asusb4():
        def __init__(self):
            pass
    class Ahsusb4():
        def __init__(self):
            pass
    class Bbsusb4():
        def __init__(self):
            pass
    class Bsusb4():
        def __init__(self):
            pass
    class Cbsusb4():
        def __init__(self):
            pass
    class Csusb4():
        def __init__(self):
            pass
    class Chsusb4():
        def __init__(self):
            pass
    class Dbsusb4():
        def __init__(self):
            pass
    class Dsusb4():
        def __init__(self):
            pass
    class Dhsusb4():
        def __init__(self):
            pass
    # sus6
    class Ebsus6():
        def __init__(self):
            pass
    class Esus6():
        def __init__(self):
            pass
    class Fbsus6():
        def __init__(self):
            pass
    class Fsus6():
        def __init__(self):
            pass
    class Fhsus6():
        def __init__(self):
            pass
    class Gbsus6():
        def __init__(self):
            pass
    class Gsus6():
        def __init__(self):
            pass
    class Ghsus6():
        def __init__(self):
            pass
    class Absus6():
        def __init__(self):
            pass
    class Asus6():
        def __init__(self):
            pass
    class Ahsus6():
        def __init__(self):
            pass
    class Bbsus6():
        def __init__(self):
            pass
    class Bsus6():
        def __init__(self):
            pass
    class Cbsus6():
        def __init__(self):
            pass
    class Csus6():
        def __init__(self):
            pass
    class Chsus6():
        def __init__(self):
            pass
    class Dbsus6():
        def __init__(self):
            pass
    class Dsus6():
        def __init__(self):
            pass
    class Dhsus6():
        def __init__(self):
            pass
    # susb6
    class Ebsusb6():
        def __init__(self):
            pass
    class Esusb6():
        def __init__(self):
            pass
    class Fbsusb6():
        def __init__(self):
            pass
    class Fsusb6():
        def __init__(self):
            pass
    class Fhsusb6():
        def __init__(self):
            pass
    class Gbsusb6():
        def __init__(self):
            pass
    class Gsusb6():
        def __init__(self):
            pass
    class Ghsusb6():
        def __init__(self):
            pass
    class Absusb6():
        def __init__(self):
            pass
    class Asusb6():
        def __init__(self):
            pass
    class Ahsusb6():
        def __init__(self):
            pass
    class Bbsusb6():
        def __init__(self):
            pass
    class Bsusb6():
        def __init__(self):
            pass
    class Cbsusb6():
        def __init__(self):
            pass
    class Csusb6():
        def __init__(self):
            pass
    class Chsusb6():
        def __init__(self):
            pass
    class Dbsusb6():
        def __init__(self):
            pass
    class Dsusb6():
        def __init__(self):
            pass
    class Dhsusb6():
        def __init__(self):
            pass
    # sus9
    class Ebsus9():
        def __init__(self):
            pass
    class Esus9():
        def __init__(self):
            pass
    class Fbsus9():
        def __init__(self):
            pass
    class Fsus9():
        def __init__(self):
            pass
    class Fhsus9():
        def __init__(self):
            pass
    class Gbsus9():
        def __init__(self):
            pass
    class Gsus9():
        def __init__(self):
            pass
    class Ghsus9():
        def __init__(self):
            pass
    class Absus9():
        def __init__(self):
            pass
    class Asus9():
        def __init__(self):
            pass
    class Ahsus9():
        def __init__(self):
            pass
    class Bbsus9():
        def __init__(self):
            pass
    class Bsus9():
        def __init__(self):
            pass
    class Cbsus9():
        def __init__(self):
            pass
    class Csus9():
        def __init__(self):
            pass
    class Chsus9():
        def __init__(self):
            pass
    class Dbsus9():
        def __init__(self):
            pass
    class Dsus9():
        def __init__(self):
            pass
    class Dhsus9():
        def __init__(self):
            pass
    # susb9
    class Ebsusb9():
        def __init__(self):
            pass
    class Esusb9():
        def __init__(self):
            pass
    class Fbsusb9():
        def __init__(self):
            pass
    class Fsusb9():
        def __init__(self):
            pass
    class Fhsusb9():
        def __init__(self):
            pass
    class Gbsusb9():
        def __init__(self):
            pass
    class Gsusb9():
        def __init__(self):
            pass
    class Ghsusb9():
        def __init__(self):
            pass
    class Absusb9():
        def __init__(self):
            pass
    class Asusb9():
        def __init__(self):
            pass
    class Ahsusb9():
        def __init__(self):
            pass
    class Bbsusb9():
        def __init__(self):
            pass
    class Bsusb9():
        def __init__(self):
            pass
    class Cbsusb9():
        def __init__(self):
            pass
    class Csusb9():
        def __init__(self):
            pass
    class Chsusb9():
        def __init__(self):
            pass
    class Dbsusb9():
        def __init__(self):
            pass
    class Dsusb9():
        def __init__(self):
            pass
    class Dhsusb9():
        def __init__(self):
            pass
    class Emaj():
        def __init__(self):
            self.Cshape = chord.Chord('E3 G#3 B3 E4 B4 G#4')
    class Fmaj():
        def __init__(self):
            pass
    class Gmaj():
        def __init__(self):
            pass

        


class snippet_maker():
    """ snippet_maker is a class from kallymuse module that can be used to make music21 music objects.
        music21 stream object is kept as a class attribute(self.stream) while setter functions
        engrave music to it.


        Here is a working example:

        Below are some examples:
        Example 1: Instanbul

            import kallymuse
            from music21 import *

            snip = kallymuse.snippet_maker()
            string = 'e4 f#4' 
            main = 'g4 f#4 e4 f#4 g4 b4 f#4 a4 e4'
            lstring = string.split()
            lmain = main.split()
            ds = [.5, .5, 1, 1, 1.5, .5, .5, .5, .5, .5, 2]
            wrds = 'e ven old new york was once new amb ser dam'
            lwrds = wrds.split()
            n1 = snip.make_measure(lstring, ds[:2], lwrds[:2])
            n2 = snip.make_measure(lmain, ds[2:6], lwrds[2:6])
            n3 = snip.make_measure(lmain[4:], ds[6:], lwrds[6:])
            for x in [n1, n2, n3]:
                snip.append(x)
            snip.stream.show()

        Example 2: No Name No. 5
            string = 'r r g4 g4 g4 g4 g4 e4 g4'
            list_string = string.split()
            _durations = [1, 1, .5, .5, 1, 1.75, .25, .5, 1.5]
            lyrics = "don't get up set a bout it - - "
            lyrics_list = lyrics.split()
            either_or = snip.make_stream(list_string, _durations, lyrics_list)
    """
    def __init__(self, string=""):
        self.string = string
        self.stream = stream.Stream()

    def make_stream(self, notecontainer, durations, lyrics_list=None, compare=False):
        '''makes a music21 stream given a list of notes (notecontainer), and their durations
        notecontainer:
            listtype of notes
        durations:
            listtype of values
        lyrics_list:
            listtype of lyrics
        '''
        # first rewrite the stream
        notes_stream = stream.Stream()
        # next the durations
        durations = durations

        for n, m in zip(notecontainer, durations):
            if n in ['rest', 'r', 'R']:
                new_rest = note.Rest()
                new_rest.duration.quarterLength = m
                notes_stream.append(new_rest)
            else:
                new_note = note.Note(n)
                new_note.duration.quarterLength = m
                notes_stream.append(new_note)


        if lyrics_list is not None:
            # lastily adding the lyrics
            if compare:
                assert len(lyrics_list) == len(notes_stream), f"lyrics list contains {len(lyrics_list)} while duration contains {len(durations)}"

            try:
                for idx, n in enumerate(notes_stream.notes):
                    n.lyric = lyrics_list[idx]
            except Exception as e:
                print(e)
        return notes_stream

    def make_measure(self, stringobj, durations, lyrics_list, sig=None, anacrusis=False, compare=False):
        '''makes a music21 stream given a string of notes, and their durations'''
        # first rewrite the stream
        notes_stream = stream.Measure()
        if sig:
            notes_stream.timeSignature = meter.TimeSignature(sig)
        if anacrusis:
            notes_stream.padAsAnacrusis()

        # next the durations
        durations = durations

        for n, m in zip(stringobj, durations):
            if n in ['rest', 'r', 'R']:
                new_rest = note.Rest()
                new_rest.duration.quarterLength = m
                notes_stream.append(new_rest)
            else:
                new_note = note.Note(n)
                new_note.duration.quarterLength = m
                notes_stream.append(new_note)


        # lastily adding the lyrics
        # assert len(lyrics_list) == len(notes_stream), f"lyrics list contains {len(lyrics_list)} while notes stream contains {len(notes_stream)}"
        if compare:
            assert len(lyrics_list) == len(durations), f"lyrics list contains {len(lyrics_list)} while notes stream contains {len(durations)}"

        try:
            for idx, n in enumerate(notes_stream.notes):
                n.lyric = lyrics_list[idx]
        except Exception as e:
            print(e)
        return notes_stream


    def append(self, obj):
        """ appends object to class attribute self.stream

        :obj: TODO
        :returns: TODO

        """
        self.stream.append(obj)

# A modified chordPattern function
# this version attempts to put notes into measures before placeing them into stream.Part classes (factories)
from typing import Union, Literal
def chordPattern(ordered_list_of_chords, rvalue, strums, isThreeFour=None, xdiv: Union[tuple, None] = None, voice_cipher: Union[Literal['a b'], None] = None) -> None:
    ''' returns a music21 score part by returning measures made from rvalue(quaterLength value in music21) and
        strums where each strum is given the value of rvalue (rhythm value). If rvalue is None and strums is a
        list, each element of the list will be conveyed to a strum.

        Further options include spliting the strums into separate voices using xdiv ( x division point ) which sets the point in each chord
        to split into either the upper or lower voice and voice_cipher which is the pattern to divide the strum values among the two
        voices. TODO: give examples.

        
    ordered_list_of_chords:
        a list of chord.Chord 
    rvalue:
        quarterLength to set for each strum
    strums:
        strums per element in ordered_list_of_chords
    isThreeFour:
        sets stream as 3/4
    xdiv:
        sets points in tuple(int(lower), int(upper) in chords to divide when using voice_cipher
    voice_cipher:
        sets pattern to divide strums into voices, defaults to None which gives a single voice, 'a b' gives each strum to alterate
        voice. 'a a b' would give the first two the first voice and third to second, and cycle the pattern.
    '''
    assert isinstance(rvalue, (int, type(None))), 'rvalue is not an int'
    assert isinstance(xdiv, (tuple, type(None))), 'xdiv: value error'
    assert isinstance(strums, (int, list)), 'strums is not an int: must be an int'
    assert isinstance(ordered_list_of_chords, list), 'ordered_list_of_chords must be a list' 
    fpart = stream.Part()
    if isThreeFour:
        fpart.append(tsThreeFour)
    # next code block is for standard function functionality, i.e., block chords with static rhythm
    # ex: chordsSectionOne = chordPattern([Cmaj, Bbmaj, Fmaj, Bbmaj], 1, 4)
    if isinstance(rvalue, int) and isinstance(strums, int) and isinstance(voice_cipher, type(None)):
        for x in ordered_list_of_chords:
            m = stream.Measure()
            x.duration.quarterLength = rvalue
            m.repeatAppend(x, strums)
            fpart.append(m)
    # next code block is for another standard application where chords inside a bar can be given rhythm
    # chordsSectionOne = chordPattern([Cmaj, Bbmaj, Fmaj, Bbmaj], None, [1.5, .5, 1, 1])
    elif not rvalue and isinstance(strums, list) and isinstance(voice_cipher, type(None)):
        for o in ordered_list_of_chords:
            m = stream.Measure()
            bar_parts = []
            for x in strums:
                # Create a chord from the current chord name and assign its duration
                o.duration.quarterLength=x
                m.repeatAppend(o, 1)
            fpart.append(m)
    elif not rvalue and isinstance(strums, list) and isinstance(voice_cipher, str) and voice_cipher == 'a b':
        # Initialize the two voices
        upper_rhythm = [x if i % 2 != 0 else note.Rest(quarterLength=x) for i, x in enumerate(strums)]
        lower_rhythm = [x if i % 2 == 0 else note.Rest(quarterLength=x) for i, x in enumerate(strums)]
        
        for o in ordered_list_of_chords:
            voice1 = stream.Voice()
            voice2 = stream.Voice()
            m = stream.Measure()
            bar_parts = []
            for x in lower_rhythm:
                # Create a chord from the current chord name and assign its duration
                #o.duration.quarterLength=x
                #voice1.repeatAppend(o, 1)
                if not isinstance(x, note.Rest):
                    subchord = chord.Chord(o.notes[:xdiv[0]]) if xdiv is not None else chord.Chord(o.notes[:2])
                    subchord.duration.quarterLength=x
                    voice1.repeatAppend(subchord, 1)
                elif isinstance(x, note.Rest):
                    x.style.AbsoluteX = 'above'
                    x.style.AbsoluteY = 'above'
                    voice1.repeatAppend(x, 1)
            for x in upper_rhythm:
                # Create upper chords
                if not isinstance(x, note.Rest):
                    subchord = chord.Chord(o.notes[xdiv[1]:]) if xdiv is not None else chord.Chord(o.notes[1:])
                    subchord.duration.quarterLength=x
                    voice2.repeatAppend(subchord, 1)
                elif isinstance(x, note.Rest):
                    voice2.repeatAppend(x, 1)
            m.insert(0, voice1)
            m.insert(1, voice2)
            fpart.append(m)
        
        
        
        # Combine both voices into one stream (score)                

    return fpart

def chordMelodyCombo(part1, part2, namePart=True):
    '''Make a chord melody combo with two parts
        part1:
            for voice
        part2:
            for guitar
        :namePart:
            (bool) labels the parts using music21 stream attribute partName with ['vocal', 'guitar'] respectatively.
    '''
    scoreStream = stream.Stream()
    part1.id, part2.id = "voice", 'guitar'
    if namePart:
        part1.partName, part2.partName = "vocal", "guitar"
    scoreStream.append(part1)
    scoreStream.append(part2)
    return scoreStream


def extendSegment(segment, extension, **args):
    """ function extends each stream.Part in a list(segment) with the measures 
        found in the list(extension) if they have a matching partName of either (['guitar', 'vocal'])


    :segment: 
        a list of stream.Part
    :extension: 
        a list of stream.Part
    :**args:
        pass
    :returns:
        returns extended list with same len of stream.Part elements

    """
    extensiond = {obj.partName: idx for idx, obj in enumerate(extension)}
    for x in segment:
        if x.partName == 'guitar':
            print(x)
            for m in extension[extensiond.get('guitar')]:
                x.append(m)
        elif x.partName == 'vocal':
            print(x)
            for m in extension[extensiond.get('vocal')]:
                x.append(m)
    return segment

def popBarline(seg, idx, partName):
    """ searches for and pops barline from first, segment[0], if present

    :segment: TODO
    :returns: TODO

    """
    if seg[idx].partName == partName:
        for I, x in enumerate(seg[idx]):
            for i, m in enumerate(x):
                if isinstance(m, bar.Barline):
                    print(I, i, m)
        seg[idx][I].pop(i)

# Modified convertor
#
from music21 import converter

class KeyToken(tinyNotation.Token):
    def parse(self, parent):
        keyName = self.token
        return key.Key(keyName)
kparser = tinyNotation.Converter()
keyMapping = (r'k(.*)', KeyToken)
kparser.tokenMap.append(keyMapping)

# Section concerning drums
#

