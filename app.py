from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Emem Ukpong! This is my first HTML page.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/favorite-course', methods=['GET', 'POST'])
def favoritecourse():
    print('Subject: ' + request.args.get('subject'))
    print('Course Number: ' + request.args.get('course_number'))

    return render_template('favorite-course.html')

@app.route('/contact', methods={'GET', 'POST'})
def contact():
    if request.method == 'POST':
        print('First name entered: ' + request.form.get('first_name' or 'N/A'))
        print('Last name entered: ' + request.form.get('last_name' or 'N/A'))
        print('Email: ' + request.form.get('email' or 'N/A'))
        print('Additional Comments: ' + request.form.get('additional_comments' or 'N/A'))
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')
if __name__ == '__main__':
    app.run()
