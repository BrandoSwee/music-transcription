from flask import Flask, request, jsonify, send_file
from DBconnect import addsampleRecording, getPdfName
import os
from werkzeug.utils import secure_filename
from AbjadTests import createSheet

app = Flask(__name__)

# Very similar case
#https://stackoverflow.com/questions/63801945/sending-a-file-from-flask-using-send-file-to-a-react-frontend-returns-a-string-o
@app.route('/putPDFonpage/<path>', methods=['GET'])
def give(path):
    fileName = os.path.join(os.getcwd(), 'Backend\\pdfFiles', secure_filename(path))
    return send_file(fileName)

# Need to convert id to pdfName
@app.route('/getPDF/<id>', methods=['GET'])
def get(id):
    pdfName = getPdfName(id)
    return jsonify(pdfName)

# Creation of pdf from wav on the flask backend
@app.route('/postWav', methods=['POST'])
def createIndex():
    theWav = request.files["wavfile"]
    #print(theWav.filename)
    title = request.form["title"]
    if(title == ""):
        title = "No Title"
    bpm = request.form["BPM"]
    if(bpm == ""):
        bpm = 65
    else:
        bpm = int(bpm)
    peg = request.form["FastestPeg"]
    peg = int(peg)
    if(peg != 4 and peg != 8 and peg != 16):
        peg = 4
    #print(request.form["composer"])
    #https://stackoverflow.com/questions/42424853/saving-upload-in-flask-only-saves-to-project-root#:~:text=UPLOAD_FOLDER%20is%20not%20a%20configuration%20option%20recognized%20by,that%20path.%20f.save%20%28os.path.join%20%28app.config%20%5B%27UPLOAD_FOLDER%27%5D%2C%20secure_filename%20%28f.filename%29%29%29
    theWav.save(os.path.join(os.getcwd(), 'Backend\\Recordings', secure_filename(theWav.filename)))
    #Call pdf creation code here
    x = createSheet(theWav.filename, title, bpm, peg)
    # let's say x is the name of the pdf so
    # HARDCODE FOR NOW
    # x = "/Sp.pdf"
    pageid = addsampleRecording(x)
    return{1: 'Good', 2: pageid}
    

if __name__ == '__main__':
    app.run(debug=True)
