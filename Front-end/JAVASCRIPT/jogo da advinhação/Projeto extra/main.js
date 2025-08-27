// variáveis
const btnTry = document.querySelector("#btnTry")
const btnReset = document.querySelector("#btnReset")
const screen1 = document.querySelector(".screen1")
const screen2 = document.querySelector(".screen2")
let randomNumber = Math.round(Math.random() * 10)
let xAttempts = 1

//eventos
btnTry.addEventListener('click', handletTryClick)
btnReset.addEventListener('click', handleResetClick)
document.addEventListener('keydown', function(e){
	if(e.key == 'Enter' && screen1.classList.contains('hide')){
		handleResetClick()
	}
})

//função callback
function handletTryClick(event) {
	event.preventDefault() //nao faça o padrao

	const inputNumber = document.querySelector('#inputNumber')


	if(Number(inputNumber.value)== randomNumber) {
		togglescreen()
		
		document.querySelector(".screen2 h2").innerText = `acertou em ${xAttempts} tentativas`
	}
	inputNumber.value =""
	xAttempts++
	
}

function handleResetClick() {
	togglescreen()
	xAttempts = 1
	randomNumber = Math.round(Math.random() * 10)
}

function togglescreen(){
	screen1.classList.toggle("hide")
	screen2.classList.toggle("hide")
}