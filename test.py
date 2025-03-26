from flask import Flask, request
import uuid

app = Flask(__name__)

lista_calculos = []

@app.route("/soma", methods=["POST"])
def somar():
    json = request.get_json()
    numero1 = json['numero1']
    numero2 = json['numero2']
    resultado = numero1 + numero2
    lista_calculos.append({
        "id": uuid.uuid4(),
        "numero1": numero1,
        "numero2": numero2,
        "resultado": resultado})
    return {'resultado': resultado}

@app.route("/calculos")
def calcular():
    return(lista_calculos)

if __name__ == "__main__":
    app.run()