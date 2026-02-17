from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

frases = [
    ("Según estudios publicados en revistas científicas, el ejercicio reduce el riesgo cardiovascular.", "argumento"),
    ("No le crean a ese profesor, ni siquiera es tan conocido.", "falacia"),
    ("Desde que uso esta aplicación, mis notas mejoraron; por eso la app me hizo más inteligente.", "falacia"),
    ("Si todos los mamíferos tienen corazón y el perro es mamífero, entonces el perro tiene corazón.", "argumento"),
    ("Millones de personas invierten en esa criptomoneda, así que es segura.", "falacia"),
    ("El consumo excesivo de azúcar puede provocar problemas metabólicos.", "argumento"),
    ("Dos políticos fueron corruptos; entonces todos los políticos son corruptos.", "falacia"),
    ("Si aumentan los impuestos, muchas empresas reducen inversión.", "argumento"),
    ("Mi abuelo fumó toda su vida y no enfermó; fumar no hace daño.", "falacia"),
    ("Un ingeniero en sistemas afirma que ese software es seguro porque cumple estándares internacionales.", "argumento")
]

indice = 0
puntaje = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global indice, puntaje

    resultado = ""
    estado = ""

    if request.method == "POST":
        respuesta_usuario = request.form["respuesta"]
        correcta = frases[indice][1]

        if respuesta_usuario == correcta:
            resultado = "¡Correcto!"
            estado = "correcto"
            puntaje += 1
        else:
            resultado = f"Incorrecto. Era: {correcta}"
            estado = "incorrecto"

        indice += 1

        if indice >= len(frases):
            return redirect(url_for("resultado_final"))

    frase_actual = frases[indice][0]

    return render_template(
        "index.html",
        frase=frase_actual,
        resultado=resultado,
        estado=estado,
        numero=indice + 1,
        total=len(frases),
        puntaje=puntaje
    )

@app.route("/resultado")
def resultado_final():
    global puntaje, indice

    puntaje_final = puntaje

    # Reiniciar juego
    puntaje = 0
    indice = 0

    return render_template("resultado.html", puntaje=puntaje_final)

if __name__ == "__main__":
    app.run(debug=True)
