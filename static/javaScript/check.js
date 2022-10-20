const card_number = document.getElementById('card-num');
const card_holder = document.getElementById('card-holder');
const form = document.getElementById('form');
const errorElement = document.getElementById('error')

form.addEventListener('submit', (e) =>{
    let message = [];
    if(card_number.value === '' || card_number.value== null){
        message.push('Card number is required')
    }
    if(card_holder.value.length <=8){
        message.push('Enter card holder name')
    }
    if(message.length > 0){
        e.preventDefault()
        errorElement.innerText = message.join(',')
    }
})