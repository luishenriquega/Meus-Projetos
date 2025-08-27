// callback function 

function sayMyName(name) { 
    console.log('antes de executar a função callback')

    name()
    
    console.log('depoisde exexutar a callback')
}

sayMyName(
    () => {
        console.log('estou em uma callback')
    }
)