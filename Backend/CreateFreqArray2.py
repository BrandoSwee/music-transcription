import sys
import aubio 
import numpy as np
import copy
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpack
import numpy as np
import copy

# I will just put a slight expansion on this.
# Purely because I see the switch over to midi
# so I will attempt to use scipy with freq.

def getMidiVal(val):
    if(val < frequencyStrings[0][0]):
        return 0
        ## Or return it "12"
    elif(val > frequencyStrings[-1][0]):
        ## Section to add checks for a value greater than our highest frequency.
        return 0
    else:
        ### CHANGE THIS PART TO BETTER SEARCH ALGORITHM SOON
        for j in range(len(frequencyStrings) - 1):
            if(val < frequencyStrings[j + 1][0]):
                if(abs(val - frequencyStrings[j][0]) < abs(val - frequencyStrings[j + 1][0])):
                    return 24 + j
                else:
                    return 25 + j
    return 0
    #i = 1
    #while True:
    #    if(val < frequencyStrings[i*12][0]):
    #        i = i - 1
    #        break
    #    i = i + 1
    #    if(i > 7):
    #        return 0
    #i = i * 12
    #for j in range(12):
    #    if(val < frequencyStrings[i + j][0]):
    #        if(abs(val - frequencyStrings[i + j][0]) < abs(val - frequencyStrings[i + j - 1][0])):
    #            return 24 + i + j
    #        else:
    #            
    #        break
    #return 0
frequencyStrings = [[32.70320, "c,,"],[34.64783, "cs,,"],[36.70810, "d,,"],[38.89087, "ds,,"],[41.20344, "e,,"],
                    [43.65353, "f,,"],[46.24930, "fs,,"],[48.99943, "g,,"],[51.91309, "gs,,"],[55.00000, "a,,"],
                    [58.27047, "as,,"],[61.73541, "b,,"],
                    [65.40639, "c,"],[69.29566, "cs,"],[73.41619, "d,"],[77.78175, "ds,"],[82.40689, "e,"],
                    [87.30706, "f,"],[92.49861, "fs,"],[97.99886, "g,"],[103.8262, "gs,"],[110.0000, "a,"],
                    [116.5409, "as,"],[123.4708, "b,"],
                    [130.8128, "c "],[138.5913, "cs "],[146.8324, "d "],[155.5635, "ds "],[164.8138, "e "],
                    [174.6141, "f "],[184.9972, "fs "],[195.9977, "g "],[207.6523, "gs "],[220.0000, "a "],
                    [233.0819, "as "],[246.9417, "b "],
                    ###Middle c4 - b4
                    [261.6256, "c'"],[277.1826, "cs'"],[293.6648, "d'"],[311.1270, "ds'"],[329.6276, "e'"],
                    [349.2282, "f'"],[369.9944, "fs'"],[391.9954, "g'"],[415.3047, "gs'"],[440.0000, "a'"],
                    [466.1638, "as'"],[493.8833, "b'"],
                    #########
                    [523.2511, "c''"],[554.3653, "cs''"],[587.3295, "d''"],[622.2540, "ds''"],[659.2551, "e''"],
                    [698.4565, "f''"],[739.9888, "fs''"],[783.9909, "g''"],[830.6094, "gs''"],[880.0000, "a''"],
                    [932.3275, "as''"],[987.7666, "b''"],
                    [1046.502, "c'''"],[1108.731, "cs'''"],[1174.659, "d'''"],[1244.508, "ds'''"],[1318.510, "e'''"],
                    [1396.913, "f'''"],[1479.978, "fs'''"],[1567.982, "g'''"],[1661.219, "gs'''"],[1760.000, "a'''"],
                    [1864.655, "as'''"],[1975.533, "b'''"],
                    [2093.005, "c''''"],[2217.461, "cs''''"],[2349.318, "d''''"],[2489.016, "ds''''"],[2637.020, "e''''"],
                    [2793.826, "f''''"],[2959.955, "fs''''"],[3135.963, "g''''"],[3322.438, "gs''''"],[3520.000, "a''''"],
                    [3729.310, "as''''"],[3951.066, "b''''"]]
    
def createFreqArray2(filePath, Bpm, fastest):
    ## This lines gives actual samplerate usually 44100
    samplerate, sampleData = wavfile.read(filePath)
    ## First get window and hop based off Bpm
    ## My test will be 184 so I will go with 180 logic on it
    ## This may drop a note over a long song as we are moving 
    # slightly slower than the actual song.
    #if((175 < Bpm && Bpm > 185)){}        //bpm
    ## Different way -> ((samplerate * 60) / 180) / 2) = same answer
    splitAt = ((samplerate * 60) / Bpm) 
    ## Want to try for arpeggio detection so... 8ths not 16ths
    if(fastest == 8):
        splitAt = splitAt / 2
    if(fastest == 16):
        splitAt = splitAt / 4
    ## Under assumption of 44100 sample rate this is 3675.
    # This will need to be integer caste even for cases where it's an integer. 
    audioChannels = len(sampleData.shape)
    ## Mono v stereo
    if(audioChannels == 2):
        sampleData = sampleData.sum(axis=1) / 2
    hop = int(round(splitAt))
    frameValues = []
    ## Going to make them equal. so we have 0 overlap.
    windowSampleSize = hop
    hopSize = hop
    ######
    src = aubio.source(filePath, samplerate, hopSize)
    #https://aubio.org/manpages/latest/aubiopitch.1.html
    # Not sure on the best pitch method of the options.
    pitch = aubio.pitch("yin",windowSampleSize,hopSize,samplerate)
    pitch.set_unit("midi")
    #pitch.set_unit("Hz")
    pitch.set_tolerance(0.8)
    values = []
    confidences = []
    totalSegments = 0
    pitchOut = []
    while True:
        sample, read = src()
        totalSegments += 1
        pitchOut = pitch(sample)[0]
        ### Confidence in the reading
        confidenceOut = pitch.get_confidence()
        #print(pitchOut)
        #values += [pitchOut]
        confidences.append(confidenceOut)
        values.append(round(pitchOut))
        if(read < hopSize):
            break
    
    ## assumption is values is an array of frequencies
    ## Will comment all prints at some point.
    frameValues = []
    while True:
        finalRun = False
        if(hop < sampleData.shape[0]):
            checkData, sampleData = sampleData[:hop], sampleData[hop:]
        else:
            checkData = sampleData
            finalRun = True
            hop = sampleData.shape[0]
        time = np.linspace(0, hop, checkData.shape[0])
        sampleSpace = time[1] - time[0]
        amplitude = 2.0 * np.abs(fftpack.fft(checkData)/len(time))
        frequencies = fftpack.fftfreq(len(time), sampleSpace)
        indexValues = []
        ## Get two values for everthing because 1 is the negative freq
        ## and 1 is the positive freq.  They will be identical because of this
        ## Hope to not get values of equal amp. (Very unlikely anyway.)
        Even = False
        while True:
            index = np.argmax(np.abs(amplitude))
            listing = [amplitude[index], abs(frequencies[index] * samplerate)]
            if(listing[0] < 250):
                if(len(indexValues) == 0):
                    listing.append(getMidiVal(listing[1]))
                    indexValues.append(copy.deepcopy(listing))
                break
            if(not Even):
                listing.append(getMidiVal(listing[1]))
                indexValues.append(copy.deepcopy(listing))
                Even = True
            else:
                Even = False
            amplitude[index] = 0
        frameValues.append(copy.deepcopy(indexValues))
        if(finalRun):
            break
    #for i in range(len(values)):
                        #Based on confidence value we can choose to throw out the value/note.
        #print(values[i], confidences[i])
    
    #print(len(frameValues))
    print(f"Total segments read = {totalSegments}")

    returnVals = []
    for i in range(len(frameValues)):
        vals = []
        sumOfvals = []
        for j in range(len(frameValues[i])):
            addedVal = False
            for m in range(len(sumOfvals)):
                if(frameValues[i][j][2] == sumOfvals[m][0]):
                    sumOfvals[m][1] = sumOfvals[m][1] + frameValues[i][j][0]
                    sumOfvals[m][2] = sumOfvals[m][2] + 1
                    addedVal = True
                    break
            if(not addedVal):
                sumOfvals.append([frameValues[i][j][2], frameValues[i][j][0], 1])
        sumOfvals.sort()

        returnVals.append(copy.deepcopy(sumOfvals))
    #print(values)
    #print(confidences)
    #print(returnVals)
    #print(values[6])
    #print(confidences[6])
    #print(returnVals[0])
    #print(returnVals[1])
    #print(returnVals[2])
    #print(returnVals[3])
    #print(returnVals[4])
    #print(returnVals[5])
    #print(returnVals[6])
    #print(returnVals[7])
    #print(returnVals[8])
    #print(returnVals[9])
    #print(returnVals[10])
    #print(returnVals[13])
### Removed checking not so good
        #print(sumOfvals)
        ## Search for in betweens
        ## think of the outputs like points on graph
        ## first and last value lucky variant for now.
#        technicalList = []
#        if(len(sumOfvals) > 0):
            #if(sumOfvals[0][1] > 300.000):
#                technicalList.append(1)
            #else:
            #    technicalList.append(0)
        
#        for n in range(1, len(sumOfvals) - 1):
#            if(sumOfvals[n][1] == sumOfvals[n + 1][1] - 1 and sumOfvals[n][1] == sumOfvals[n - 1][1] + 1):
#                if(sumOfvals[n][0] * 1.2 < sumOfvals[n + 1][0] and sumOfvals[n][0] * 1.2 < sumOfvals[n - 1][0]):
#                    technicalList.append(0)
#            else:
#                technicalList.append(1)
        
#        if(len(sumOfvals) > 0 and len(sumOfvals) != 1):
            #if(sumOfvals[len(sumOfvals) - 1][1] > 300.000):
#                technicalList.append(1)
            #else:
            #    technicalList.append(0)
        
#        for m in range (len(technicalList)):
#            if(technicalList[m] == 1):
#                if(sumOfvals[m][0] > 23 and sumOfvals[m][0] < 108):
#                    vals.append(sumOfvals[m])
        
        #returnVals.append([values[i],confidences[i],copy.deepcopy(vals)])
        #returnVals.append(copy.deepcopy(vals))
    #for i in range(len(returnVals)):
    #    print(returnVals[i])
    actualVals = []
    ### Maybe add extra checking against the results
    ### The worse the aubio reading the more likely 
    ### a chord might exist.
    for i in range(len(values)):
        ### We call this dominance.
        newlisting = []
        dominance = 0
        # Single note and it must be this alone.
        if(confidences[i] > 0.95):
            dominance = 1
        # exists and has great Dominace
        # other notes might exist
        elif(confidences[i] > 0.90):
            dominance = 2
        # Note probably exists and other
        # notes might exist.
        elif(confidences[i] > 0.75):
            dominance = 3
        
        # Note may exist look for note in listings.
        elif(confidences[i] > 0.50):
            dominance = 4
        
        # Reading is bad. Do a general look over all lists.
        else:
            dominance = 0
        #print("hi")
        if(values[i] > 119 or values[i] < 24):
            dominance = 0
        if(dominance > 0):
            Keepindex = None
            for m in range(len(returnVals[i])):
                if(values[i] == returnVals[i][m][0]):
                    newlisting.append(returnVals[i][m])
                    Keepindex = m
                    #actualVals.append(copy.deepcopy(returnVals[i][2][m]))
                    break
            if(len(newlisting) == 0):            ##Random high value
                newlisting.append([values[i], 2000.00, 0])
            if(dominance == 2):
                for m in range(len(returnVals[i])):
                    if(newlisting[0][1] < returnVals[i][m][1]):
                        newlisting.append(returnVals[i][m])
            if(dominance == 3):
                for m in range(len(returnVals[i])):
                    if(newlisting[0][0] > 59 and returnVals[i][m][0] < 60):
                        if(returnVals[i][m][1] > 425.00):
                            newlisting.append(returnVals[i][m])
                    if(newlisting[0][1] < returnVals[i][m][1] + 500 and Keepindex != m):
                        newlisting.append(returnVals[i][m])
            if(dominance == 4):
                for m in range(len(returnVals[i])):
                    
                    #print(newlisting[0][0])
                    if(newlisting[0][0] > 59 and returnVals[i][m][0] < 60):
                        if(returnVals[i][m][1] > 300.00):
                            newlisting.append(returnVals[i][m])
                    if(newlisting[0][1] < returnVals[i][m][1] + 750 and Keepindex != m):
                        newlisting.append(returnVals[i][m])
        if(dominance == 0):
            technicalList = []
            if(len(returnVals) > 0):
                if(returnVals[i][0][1] > 300.000):
                    technicalList.append(1)
                else:
                    technicalList.append(0)
        
            for n in range(1, len(returnVals[i]) - 1):
                if(returnVals[i][n][1] == returnVals[i][n + 1][1] - 1 and returnVals[i][n][1] == returnVals[i][n - 1][1] + 1):
                    if(returnVals[i][n][0] * 1.2 < returnVals[i][n + 1][0] and returnVals[i][n][0] * 1.2 < returnVals[i][n - 1][0]):
                        technicalList.append(0)
                else:
                    technicalList.append(1)
        
            if(len(returnVals[i]) > 0 and len(returnVals[i]) != 1):
                if(returnVals[i][len(returnVals[i]) - 1][1] > 300.000):
                    technicalList.append(1)
            else:
                technicalList.append(0)
            for m in range (len(technicalList)):
                if(technicalList[m] == 1):
                    if(returnVals[i][m][0] > 23 and returnVals[i][m][0] < 108):
                        newlisting.append(returnVals[i][m])            
        actualVals.append(copy.deepcopy(newlisting))
    
    while(True):
        if(actualVals[-1] == []):
            actualVals.pop(-1)
        else:
            break
            #for n in range(len(returnVals[i][2])):
    #print(actualVals)    
    #for i in range(len(returnVals)):
    #    listing = returnVals[i][2]
    #    actualVals.append(listing)
    #for i in range(len(actualVals)):
    #    print(values[i],confidences[i], actualVals[i])        
    #print(f"Total segments with confidence level greater than 0.7 = {len(returnVals)}")
    return actualVals

if __name__ == "__main__": 
    createFreqArray2("Backend/Recordings/opener.wav", 184, 16)
