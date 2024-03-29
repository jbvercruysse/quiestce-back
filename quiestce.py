from flask import Flask
from flask import abort, logging, jsonify,make_response, redirect
from flask import has_request_context, request
from flask.logging import default_handler
from pprint import pprint
from TableCards import TableCards
from DrawCards import DrawCards
from fpdf import FPDF
import time
from random import randint
import config

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 #1Mb
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]

# doc: https://flask.palletsprojects.com/en/1.1.x/quickstart/

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/whoswho-data', methods=['POST'])
def whoswho_data():
    app.logger.info('Starting new request....')
    #check_file_input(request.files)

    # key for this run
    key = str(int(time.time())) + "-" + str(randint(1, 999))

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font("Arial", size=11)

    t = TableCards(pdf, request.files, request.form,key)
    t.generate_page_recto()
    pdf = t.generate_page_verso()

    d = DrawCards(pdf, request.files, request.form,key)
    pdf = d.generate_page_recto()

    result_pdf_name =  "final_" + key + ".pdf"
    result_pdf_path = config.RESULT_DIRECTORY + result_pdf_name

    pdf.output(result_pdf_path)

    response = make_response(config.RESULT_WEB_ROOT+result_pdf_name)
    response.headers.add('Access-Control-Allow-Origin', '*')
    app.logger.info('Done for new request....')
    return response

def check_file_input(files):
    for file in files.items():
        if not allowed_extension(file[1].filename):
            print("That file extension is not allowed")
            return redirect(request.url)
        if not check_filename_exist(file[1].filename):
            print("No filename")
            return redirect(request.url)


def check_filename_exist(filename):
    if filename== "":
        app.logger.info('The filename is empty')
        return False
    else:
        return  True

def allowed_extension(filename):
    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        app.logger.info('That file extension is not allowed %s', ext)
        return False


if __name__ == '__main__':
    app.run(host='0.0.0.0')
