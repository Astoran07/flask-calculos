from flask import Flask, request

app = Flask(__name__)

lista_calculos = []

@app.route("/soma", methods=["POST"])
def somar():
    json = request.get_json()
    numero1 = json['numero1']
    numero2 = json['numero2']
    resultado = numero1 + numero2
    lista_calculos.append(f"{numero1} + {numero2} = {resultado}")
    return {'resultado': resultado}

@app.route("/calculos")
def calcular():
    if len(lista_calculos) != 0:
        print(len(lista_calculos))
        for item in lista_calculos:
            return item
    else:
        return[]

if __name__ == "__main__":
    app.run()