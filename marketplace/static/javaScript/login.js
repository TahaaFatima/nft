const email = document.getElementById('email');
const password = document.getElementById('password');
const form = document.getElementById('form');
const errorElement = document.getElementById('error')

form.addEventListener('submit', (e) =>{
    let message = [];
    if(email.value === '' || email.value== null){
        message.push('Email is required')
    }
    if(password.value.length <=6){
        message.push('Password must be longer tha 6 character')
    }
    if(message.length > 0){
        e.preventDefault()
        errorElement.innerText = message.join(',')
    }
})
