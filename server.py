'''Building server'''

from flask import Flask, render_template, url_for, request, redirect
from pprint import pformat
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


# @app.route('/index.html')
# def home_button():
#     return render_template('index.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # with open('database.txt', 'a', encoding='utf-8') as f:
            #     f.write(pformat(data, width=1))
            #     f.write('\n')
            return redirect('/thankyou.html')
        except:
            return 'Something wrong!'
    else:
        return "Something wrong!"
