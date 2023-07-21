function manipularMensagem() {
    const form_mensagem = document.getElementById("form-mensagem")
    const input_msg = document.getElementById("msg")
    const input_alexa = document.getElementById("alexa")

    form_mensagem.onsubmit = async(event) => {
        event.preventDefault()
        const msg_mensagem = input_msg.value
        const alexa_mensagem = input_alexa.value
        await axios.post('https://fastapideta-1-r0743913.deta.app/', {
            message: msg_mensagem,
            alexa: alexa_mensagem
        })

        // carregarMensagem()
        alert('Mensagem enviada!')
    }
}

function app() {
    console.log("App iniciado")
        //carregarMensagem()
    manipularMensagem()
}

app()