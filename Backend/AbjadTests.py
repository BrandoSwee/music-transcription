import abjad
from CreateFreqArray2 import createFreqArray2
from FreqProcess import analyzeFrequencies
import re
import os

def createSheet(wavFile, Title = "No Title",  bpm=65, peg=4):
    actualWav = 'Backend/Recordings/' + wavFile
    out = createFreqArray2(actualWav, bpm, peg)
    stringO, secondOutFromAF = analyzeFrequencies(out, peg)
    #print(secondOutFromAF)
    #stringO = "<f'>16 g' a' b' c'' d'' e'' f''"
    #secondOutFromAF = "r4 g,,8 g,8"
    #secondOutFromAF = "c'8 f' <g'' c'' f'' e''> d' g' a' b' e'2 a' b' c'' f' b' c''8 c' c'"
                                #"c'16 f' g' a' d' g' a' b' e' a' b' c'' f' b' c'' c' "
    ### 
    voice = abjad.Voice(stringO, name="R_Voice")
    r_staff = abjad.Staff([voice], name="R_Staff")
    lh_voice = abjad.Voice(secondOutFromAF,name="LH_Voice")
    lh_staff = abjad.Staff([lh_voice], name="LH_Staff")
    staff_group = abjad.StaffGroup(
        [r_staff, lh_staff],
        lilypond_type="PianoStaff",
        name="Piano_Staff",
    )
    leaf = abjad.select(staff_group["LH_Voice"]).leaf(0)
    clef = abjad.Clef("bass")
    abjad.attach(clef, leaf)
    score = abjad.Score([staff_group], name="Score")
    string = abjad.lilypond(score)
    #print(string)
    #print(len(string))
    #print(string[118:120])
    ##print(string)
    titleString = " title = \markup {" + Title + "}"
    testString1 = """#(set-global-staff-size 14)

    \header {
        composer = \markup { Me }
        subtitle = \markup { You }
    """
    testString2 = """
    }
    \layout {
        indent = 0
    }

    """
    testString = testString1 + titleString + testString2
    m = re.sub(r's', 'is', string)
    mstring = m
    mstring = re.sub(r"baisis","bass", mstring)
    File = abjad.LilyPondFile([testString, mstring])
    #out = abjad.lilypond(File)
    #print(out)
    title = re.sub(r'\s+', '', Title)
    returnTitle = '/' + title + '.pdf'
    abjad.persist.as_pdf(File, os.path.join(os.getcwd(), 'Backend\\pdfFiles\\' + title))
    return returnTitle


if __name__ == "__main__":
    createSheet("SP","TestRecording/SongFiles/SP140.wav", 140, 16)