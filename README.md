# Trabalho4
Faça uma API que retorna o resultado das operações fatorial e/ou Fibonacci com entrada em JSON.

Os testes:

curl -X POST -H "Content-Type: application/json" -d '{"numero": 5}' http://127.0.0.1:5000/fatorial

curl -X POST -H "Content-Type: application/json" -d '{"numero": 6}' http://127.0.0.1:5000/fibonacci

curl -X POST -H "Content-Type: application/json" -d '{"numero": 5}' http://127.0.0.1:5000/fatorial_fibonacci
