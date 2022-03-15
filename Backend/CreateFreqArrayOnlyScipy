import sys
import numpy as np
import copy
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpack
import numpy as np

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
        ### CHANGE THIS PART TO BETTER SEARCH ALGORITHM MAYBE
        for j in range(len(frequencyStrings) - 1):
            if(val < frequencyStrings[j + 1][0]):
                if(abs(val - frequencyStrings[j][0]) < abs(val - frequencyStrings[j + 1][0])):
                    return 24 + j
                else:
                    return 25 + j
    return 0
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
    
def createFreqArraySci(filePath, Bpm, fastest):
    ## This lines gives actual samplerate usually 44100
    samplerate, sampleData = wavfile.read(filePath)
    ## First get window and hop based off Bpm
    ## My test will be 184 so I will go with 180 logic on it
    ## This may drop a note over a long song as we are moving 
    # slightly slower than the actual song.
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
    finalRun = False
    while True:
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
    
    print(f"Total segments read = {len(frameValues)}")

    returnVals = []
    for i in range(len(frameValues)):
        #vals = []
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
        sumOfvals.sort(key = lambda row: row[1])
        sumOfvals.reverse()
        returnVals.append(copy.deepcopy(sumOfvals))
    actualVals = []
    while(True):
        if(returnVals[0] == []):
            actualVals.pop(0)
        else:
            break
    ### Maybe add extra checking against the results
    ### The worse the aubio reading the more likely 
    ### a chord might exist.
    currVals = []
    storage = []
    removeHold = []
    AddAfter = []
    #print(len(storage))
    #print(returnVals[1])
    for i in range(len(returnVals)):
        if(i != 0):
            for j in range(len(returnVals[i])):
                didSomething = False
                for n in range(len(storage)):
                    if(storage[n][0] == returnVals[i][j][0]):
                        didSomething = True
                        if(storage[n][1] > returnVals[i][j][1] or storage[n][3] > 1):
                            val = 0
                            noPass = True
                            fadeCheck = 0
                            #continue the trail or end note
                            if(storage[n][3] == 1):
                                val = fastest
                                fadeCheck = 0.70
                                if(returnVals[i][j][1] > storage[n][1] * 0.80 ):
                                    storage[n][3] = storage[n][3] + 1
                                    break
                            elif(storage[n][3] == 2):
                                val = fastest / 2
                                fadeCheck = 0.60
                                if(returnVals[i][j][1]  > storage[n][1] * 0.70):
                                    storage[n][3] = storage[n][3] + 1
                                    if(val == 2):
                                        val = 1
                                        noPass = False
                                    else:
                                        break
                            elif(storage[n][3] == 3):
                                val = fastest / 4
                                fadeCheck = 0.50
                                if(returnVals[i][j][1]  > storage[n][1] * 0.60):
                                    storage[n][3] = storage[n][3] + 1
                                    if(val == 2):
                                        val = 1
                                        noPass = False
                                    else:
                                        break
                            elif(storage[n][3] == 4):
                                val = fastest / 8
                                fadeCheck = 0.40
                                if(returnVals[i][j][1] > storage[n][1] * 0.50 ):
                                    storage[n][3] = storage[n][3] + 1
                            #print("What")
                            currVals.append(copy.deepcopy(storage[n]))
                            removeHold.append(storage[n][0])
                            
                            if(noPass):
                                #FADE can play a role
                                if(returnVals[i][j][0] < 60 and returnVals[i][j][0] > 23):
                                    if(returnVals[i][j][1] > 450.000):
                                        AddAfter.append([returnVals[i][j][0], returnVals[i][j][1], i, 1])
                                elif(returnVals[i][j][1] > 600.000 and returnVals[i][j][1] > storage[n][1] * fadeCheck):
                                    AddAfter.append([returnVals[i][j][0], returnVals[i][j][1], i, 1])
                            
                        else:
                            #Update
                            storage[n][2] = i
                            storage[n][1] = returnVals[i][j][1]

                if(didSomething == False):
                    if(returnVals[i][j][0] < 60 and returnVals[i][j][0] > 23):
                        if(returnVals[i][j][1] > 450.000):
                            storage.append([returnVals[i][j][0], returnVals[i][j][1], i, 1])
                    elif(returnVals[i][j][1] > 600.000):
                        storage.append([returnVals[i][j][0], returnVals[i][j][1], i, 1])

            for r in range(len(removeHold)):
                for ug in range(len(storage)):
                    if(removeHold[r] == storage[ug][0]):
                        storage.remove(storage[ug])
                        break
            removeHold = []

            for add in range(len(AddAfter)):
                storage.append(AddAfter[add])
            AddAfter = []
        else:
            # I will not write on song start
            for m in range(len(returnVals[i])):
                if(returnVals[i][m][0] < 60 and returnVals[i][m][0] > 23):
                    if(returnVals[i][m][1] > 450.000):
                        storage.append([returnVals[i][m][0], returnVals[i][m][1], i, 1])
                elif(returnVals[i][m][1] > 600.000):
                    storage.append([returnVals[i][m][0], returnVals[i][m][1], i, 1])
    
    for i in range(len(storage)):
        currVals.append(storage[i])
    
    currVals.sort(key = lambda row: row[2])
    #print(currVals)
    index = 0
    indexList = 0
    Framelisting = []
    Frames = 0
    #print(currVals)
    while(len(currVals) > indexList):
        if(currVals[indexList][2] != index):
            actualVals.append(copy.deepcopy(Framelisting))
            Framelisting = []
            index = index + 1
        else:
            if(currVals[indexList][3] == 3):
                Frames = fastest / 4
            elif(currVals[indexList][3] == 4):
                Frames = fastest / 8
            elif(currVals[indexList][3] == 5):
                Frames = fastest / 16
            else:
                Frames = fastest / currVals[indexList][3]
            round(Frames)
            Framelisting.append([currVals[indexList][0], Frames])
            indexList = indexList + 1
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
    #    print(actualVals[i])        
    #print(f"Total segments with confidence level greater than 0.7 = {len(returnVals)}")
    return actualVals

if __name__ == "__main__": 
    createFreqArraySci("Backend/Recordings/opener.wav", 184, 16)
