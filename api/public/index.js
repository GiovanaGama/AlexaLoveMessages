// async function carregarMensagem(){
//     const response = await  axios.get('http://127.0.0.1:8000/mensagem')

//     const mensagens = response.data

//     const lista = document.getElementById('lista-mensagens')

//     lista.innerHTML = ''

//     mensagens.forEach(mensagem => {
//         const item = document.createElement('li')

//         const linha = `${mensagem.message}, ${mensagem.alexa}`
//         item.innerText = linha

//         item.appendChild(item)
//     });
// }

function manipularMensagem(){
    const form_mensagem = document.getElementById("form-mensagem")
    const input_msg = document.getElementById("msg")
    const input_alexa = document.getElementById("alexa")

    form_mensagem.onsubmit = async (event) => {
        event.preventDefault()
        const msg_mensagem = input_msg.value
        const alexa_mensagem = input_alexa.value
        await axios.post('http://127.0.0.1:8000/mensagem', {
            message: msg_mensagem,
            alexa: alexa_mensagem
        })

       // carregarMensagem()
        alert('Mensagem enviada!')
    }
}

function app(){
    console.log("App iniciado")
    //carregarMensagem()
    manipularMensagem()
}

app()