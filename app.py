from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut_selection.html')


if __name__ == '__main__':
    app.run(debug=True)