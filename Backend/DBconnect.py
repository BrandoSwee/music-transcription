import pymongo
import bson
import datetime

def getPdfName(id):
    client = pymongo.MongoClient("mongodb+srv://Brandon:Password23@cluster0.6el1g.mongodb.net/Music?retryWrites=true&w=majority")
    db = client['Music']
    Recordings = db['Recordings']
    objectid = bson.ObjectId(id)
    val = Recordings.find_one({'_id':objectid})
    client.close()
    if(val['PDFFileName'] == None):
        return 'error'
    else:
        return val['PDFFileName']
    
def addsampleRecording(data):
    client = pymongo.MongoClient("mongodb+srv://Brandon:Password23@cluster0.6el1g.mongodb.net/Music?retryWrites=true&w=majority")
    db = client['Music']
    Recordings = db['Recordings']
    now = datetime.datetime.now()
    Rec = {
        'PDFFileName': data,
        'Timestamp': now
    }
    Recordings.insert_one(Rec)
    x = Recordings.find_one({'Timestamp': now})
    outval = str(x["_id"])
    client.close()

    return outval
    