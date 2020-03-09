import sys
from flask import Flask, render_template, request, send_file
import os
import zipfile

application = Flask(__name__)

@application.route('/') #creates the flask html route
def root():
    return render_template('main.html')
@application.route('/', methods=['POST']) #creates the flask html route
def post():
    text1 = request.form['user1'] #getting usernames
    # text2 = request.form['user2'] 
    # text3 = request.form['user3']
    # text4 = request.form['user4'] 

    args2 = "rm img/*.png" #removing pictures and videos from previous run
    os.system(args2)
    args3 = "rm Video/*.avi"
    os.system(args3)

    args4 = "python main.py "+ str(text1)
    args5 = "mv *.avi Video/"
    os.system(args4) #running hw3queue to multiprocess the up to 4 usernames
    os.system(args5)
    zipFolder = zipfile.ZipFile('vids.zip','w', zipfile.ZIP_DEFLATED) #making the zip and sending it to the user!!!
    for root, directs, files in os.walk('Video/'):
        for f in files:
            zipFolder.write('Video/' + str(f))
    zipFolder.close()

    os.system(args3)    
    return send_file('vids.zip', mimetype ='zip', attachment_filename = 'vids.zip', as_attachment=True)

if __name__ == '__main__':

    application.run(host = '0.0.0.0', port = 8080)


