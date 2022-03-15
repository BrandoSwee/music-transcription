
### Frequencies from wikipedia
# https://en.wikipedia.org/wiki/Piano_key_frequencies
#######################################################
### Changing this to a list of lists could be helpful? 
### I won't change the code to use it yet, but it will be a simple change for the code.
### Ex: [[261.6256,"c' "],[277.1826, "cs' "], ...] This is probably easier to maintain in the long run.
### Calling sort on frequencyStrings list will order the values 0 to +infinity.
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
                    ##83 values

def addRest(notes, peg):
    leng = (len(peg) + 2)
    meg = int(peg)
    if(len(notes) < leng):
        notes = notes + "r" + peg + " "
    elif(notes[(leng*-1):] == ("r" + peg + " ")):
        notes = notes[:leng * -1]
        ##Assume that peg is not set to 1.
        notes = notes + "r" + str(int(meg / 2)) + " "
        meg = int(meg / 2)
        peg = str(meg)
        while(True):
            leng = len(peg) + 2
            #print(notes[(((leng + leng) * -1)):leng * -1])
            #print(notes[(leng * -1):])
            if(notes[(((leng + leng) * -1)):(leng * -1)] == notes[(leng * -1):]):
                meg = int(meg / 2)
                peg = str(meg)
                if(meg == 0):
                    break
                else:
                    notes = notes[:(leng + leng) * -1]
                    notes = notes + "r" + peg + " "
            else:
                break


    else:
        notes = notes + "r" + peg + " "

    return notes


def analyzeFrequenciesSci(freq, peg = 4):
    if(isinstance(freq, list) and len(freq) > 0):
        returnString = ""
        returnString2 = ""
        if(peg != 16 and peg != 1 and peg != 2 and peg != 4 and peg != 8):
            return None, None
        else:
            pegi = str(peg)
            for i in range(len(freq)):
                ##empty
                if(not freq[i]):
                    if(returnString == ""):
                        continue
                    else:
                        returnString = addRest(returnString, pegi)
                        returnString2 = addRest(returnString2, pegi)
                else:
                    returnString = returnString + "<"
                    returnString2 = returnString2 + "<"
                    for j in range(len(freq[i])):
                        if(freq[i][j][0] < 60):
                            returnString2 = returnString2 + frequencyStrings[freq[i][j][0] - 24][1]
                        else:
                            returnString = returnString +  frequencyStrings[freq[i][j][0] - 24][1]
                    if(returnString[-1] == "<"):
                        returnString = returnString[:-1]
                        returnString = addRest(returnString, pegi)
                    else:
                         returnString += ">" + pegi + " "
                    if(returnString2[-1] == "<"):
                        returnString2 = returnString2[:-1]
                        returnString2 = addRest(returnString2, pegi)
                    else:
                        returnString2 += ">" + pegi + " "
            #print(returnString)
            #print(returnString2)

            if(returnString == "" and returnString2 == ""):
                return "r1", "r1"
            #print("hi")
            return returnString, returnString2
#######################################################
### This function is made with the idea that it
### will take a list of frequencies and output
### a single string to be wrote to a pdf of sheet music.
### More parameters can be added.
def analyzeFrequencies(freq, peg = 4):
    if(isinstance(freq, list) and len(freq) > 0):
        returnString = ""
        returnString2 = ""
        if(peg != 16 and peg != 1 and peg != 2 and peg != 4 and peg != 8):
            return None, None
        else:
            pegi = str(peg)
            for i in range(len(freq)):
                ##empty
                if(not freq[i]):
                    if(returnString == ""):
                        continue
                    else:
                        returnString = addRest(returnString, pegi)
                        returnString2 = addRest(returnString2, pegi)
                else:
                    returnString = returnString + "<"
                    returnString2 = returnString2 + "<"
                    for j in range(len(freq[i])):
                        if(freq[i][j][0] < 60):
                            returnString2 = returnString2 + frequencyStrings[freq[i][j][0] - 24][1]
                        else:
                            returnString = returnString +  frequencyStrings[freq[i][j][0] - 24][1]
                    if(returnString[-1] == "<"):
                        returnString = returnString[:-1]
                        returnString = addRest(returnString, pegi)
                    else:
                         returnString += ">" + pegi + " "
                    if(returnString2[-1] == "<"):
                        returnString2 = returnString2[:-1]
                        returnString2 = addRest(returnString2, pegi)
                    else:
                        returnString2 += ">" + pegi + " "
            #print(returnString)
            #print(returnString2)

            if(returnString == "" and returnString2 == ""):
                return "r1", "r1"
            #print("hi")
            return returnString, returnString2