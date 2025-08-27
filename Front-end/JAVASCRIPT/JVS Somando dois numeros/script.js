let firstNumber = prompt('digite o primeiro numero')
let secondNumber = prompt('digite o segundo numero')

firstNumber = Number(firstNumber)
secondNumber = Number(secondNumber)
let comparison = firstNumber == secondNumber
const sum = firstNumber + secondNumber
const sub = firstNumber - secondNumber
const mult = firstNumber * secondNumber
const div = firstNumber / secondNumber
const restdiv = firstNumber % secondNumber


if(sum % 2 == 0 ){
alert('este numero é par')
} else {
    alert('esse numero é impar')
}

alert('os numeros são iguais ? ' + comparison)
alert('soma ' + sum) 
alert('subtração ' + sub)
alert('multiplicação ' + mult)
alert('divisão ' + div)
alert('resto div ' + restdiv)