from flask import Flask, render_template

app = Flask(__name__)
  
"""
@app.route('/')
def principal():
    return "AGENCIA DE VIAJES SENDEROS!"
    
"""
@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes = ("PHP", "Python", "Java", "C#",
                    "JavaScript", "Perl", "Ruby", "Rust")
    return render_template('lenguajes.html', lenguajes=misLenguajes)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/sendero')
def sendero():
    return render_template('sendero.html')

@app.route('/termal')
def termal():
    return render_template('termal.html')

@app.route('/religion')
def religion():
    return render_template('religion.html')

@app.route('/ecoturistico')
def ecoturistico():
    return render_template('ecoturistico.html')

@app.route('/aventura')
def aventura():
    return render_template('aventura.html')

@app.route('/arqueologia')
def arqueologia():
    return render_template('arqueologia.html')

@app.route('/vinternacional')
def vinternacional():
    return render_template('vinternacional.html')

@app.route('/america')
def america():
    return render_template('america.html')

@app.route('/vnacional')
def vnacional():
    return render_template('vnacional.html')

@app.route('/cruceros')
def cruceros():
    return render_template('cruceros.html')

@app.route('/viajesdisney')
def viajesdisney():
    return render_template('viajesdisney.html')

@app.route('/seguroviaje')
def seguroviaje():
    return render_template('seguroviaje.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/alquilerc')
def alquilerc():
    return render_template('alquilerc.html')

@app.route('/sim')
def sim():
    return render_template('sim.html')

@app.route('/asia')
def asia():
    return render_template('asia.html')

@app.route('/africa')
def africa():
    return render_template('africa.html')

@app.route('/europa')
def europa():
    return render_template('europa.html')

@app.route('/andina')
def andina():
    return render_template('andina.html')

@app.route('/amazonas')
def amazonas():
    return render_template('amazonas.html')

@app.route('/atlantico')
def atlantico():
    return render_template('atlantico.html')

@app.route('/pacifico')
def pacifico():
    return render_template('pacifico.html')

@app.route('/llano')
def llano():
    return render_template('llano.html')

@app.route('/disn')
def disn():
    return render_template('disn.html')


@app.route('/australia')
def australia():
    return render_template('australia.html')

if __name__ == '__main__':
    app.run()





    
    
    
    
