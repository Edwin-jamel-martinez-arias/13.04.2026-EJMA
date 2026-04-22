from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/cuenta')
def cuenta():
    return render_template('crearcuenta.html')

@app.route('/gestor')
def gestor():
    return render_template('gestor.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
