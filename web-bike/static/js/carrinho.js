let updateBtns = document.getElementsByClassName('update-cart')

for(let i=0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('ProductId:', productId, 'Action:', action)
        console.log('User:', user)

        if(user === 'AnonymousUser') {
            console.log('Não está logado!!')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log("Usuário logado! Enviando dados...")

    let url = '/carrinho/add/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action}),
    })
        .then((response) => {
        return response.json();
    })
        .then((data) => {
        console.log('data:', data)
    });
}