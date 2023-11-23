from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

@app.route('/fatorial', methods=['POST'])
def fatorial():
    data = request.get_json()
    num = data.get('numero')
    resultado = calcular_fatorial(num)
    return jsonify({"resultado_fatorial": resultado})

@app.route('/fibonacci', methods=['POST'])
def fibonacci():
    data = request.get_json()
    num = data.get('numero')
    resultado = calcular_fibonacci(num)
    return jsonify({"resultado_fibonacci": resultado})

@app.route('/fatorial_fibonacci', methods=['POST'])
def fatorial_fibonacci():
    data = request.get_json()
    num = data.get('numero')
    resultado_fatorial = calcular_fatorial(num)
    resultado_fibonacci = calcular_fibonacci(num)
    return jsonify({"resultado_fatorial": resultado_fatorial, "resultado_fibonacci": resultado_fibonacci})

if __name__ == '__main__':
    app.run(debug=True)
