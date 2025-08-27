let student1 = prompt("Qual é seu nome ?")
let n1 = prompt("Qual foi a nota da sua primeira prova?")
let n2 = prompt("Qual foi a nota da sua segunda prova?")
let n3 = prompt("Qual foi a nota da sua terceira prova?")

let average = (Number(n1)) + (Number(n2)) + (Number(n3)) / 3

let result = average > 7

alert(result)