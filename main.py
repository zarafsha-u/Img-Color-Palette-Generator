import base64
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request, redirect, url_for
from palette import PaletteGenerator
import io



app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return render_template('index.html')
    return render_template('index.html')


@app.route('/result', methods= ['GET', 'POST'])
def result():
    if request.method == 'POST':
        picture = request.form.get('filename')
        pal = PaletteGenerator(picture)
        palette = pal.palette()
        fig, ax = plt.subplots()
        ax.imshow(palette)
        ax.axis('off')
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('result.html', data = data, plt = plt)



if __name__ == "__main__":
    app.run(debug=True)


