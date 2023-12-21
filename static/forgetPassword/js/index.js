let codeInput = document.querySelectorAll(".js-code-input")
let form = document.getElementById("account__form")
let emailInput = document.getElementById("emailInput")
codeInput.forEach(element => {
    element.addEventListener("keyup", handleKeyDown)
    element.addEventListener("input", handleInput)
})

emailInput.addEventListener("keydown",(e)=>{
    e.preventDefault()
})

function handleKeyDown(event) {
    const inputId = event.target.id;
    let indexOfInput = +(inputId.slice(inputId.length - 1, inputId.length))
    if (event.key === 'Backspace' && event.target.value === "" && indexOfInput !== 1) {
        const prevInput = document.getElementById(`input-number-${indexOfInput - 1}`);
        if (prevInput) {
            prevInput.focus();
        }
    } else if (event.target.value !== "" && indexOfInput !== 4) {
        const nextInput = document.getElementById(`input-number-${indexOfInput + 1}`);
        if (nextInput) {
            nextInput.focus();
        }
    } else {
        for (let element of codeInput) {
            if (element.value === "") {
                break;
            } else if (codeInput[codeInput.length - 1] === element) {
                // console.log(form)
                form.submit()
            }
        }
    }
}

function handleInput(event) {

    let inputValue = event.target.value;
    event.target.value = inputValue.replace(/[^0-9.]/g, '');
    console.log(event.target.getAttribute("maxLength"))
    if (event.target.value.length > event.target.getAttribute("maxLength")) {
        event.target.value = event.target.value.slice(0, event.target.getAttribute("maxLength"))
    }
}


const urlParams = new URLSearchParams(window.location.search);
const email = urlParams.get('email');

if (email) {
    emailInput.value = email
} else {
    window.location = "/forget-password/"
}