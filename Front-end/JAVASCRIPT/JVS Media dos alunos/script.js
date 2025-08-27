let student = prompt("Qual o nome do(a) aluno(a)?")
let n1 = prompt("Qual a nota da primeira prova?")
let n2 = prompt("Qual a nota da segunda prova?")
let n3 = prompt("Qual a nota da terceira prova?")

let average = (Number(n1) + Number(n2) + Number(n3)) / 3



average = average.toFixed(2)

let student1 = prompt("Qual o nome do(a) aluno(a)?")
let p1 = prompt("Qual a nota da primeira prova?")
let p2 = prompt("Qual a nota da segunda prova?")
let p3 = prompt("Qual a nota da terceira prova?")

let average2 = (Number(p1) + Number(p2) + Number(p3)) / 3



average = average2.toFixed(2)

let student2 = prompt("Qual o nome do(a) aluno(a)?")
let b1 = prompt("Qual a nota da primeira prova?")
let b2 = prompt("Qual a nota da segunda prova?")
let b3 = prompt("Qual a nota da terceira prova?")

let average3 = (Number(b1) + Number(b2) + Number(b3)) / 3



average = average3.toFixed(2)


let result = average > 6

if (result) {
alert("Parabéns, " + student + "! Você foi aprovado no concurso!: " + average)

} else if (average < 3){
    alert("Reprovado")
} else {
    alert("não foi dessa vez!" + student + "Tente Novamente!" +  average)   
}
   
  let resultado = average2 > 7
if (resultado) {
    alert("Parabéns, " + student1 + "! Você foi aprovado no concurso!: " + average2)
 } else if (average2 < 3){
        alert("Reprovado")
  } else {
        alert("não foi dessa vez!" + student1 + "Tente Novamente!" +  average2)   
}

let resultados = average3 > 7

    if (resultados) {
        alert("Parabéns, " + student2 + "! Você foi aprovado no concurso!: " + average3)
    
} else if (average3 < 3){
    alert("Reprovado")
} else {
 alert("não foi dessa vez!" + student2 + "Tente Novamente!" +  average3)   
      }

