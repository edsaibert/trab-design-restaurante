document.getElementById('submitButton').addEventListener('click', async (event) => {
    event.preventDefault();

    const usuario = document.getElementById("usuario").value;
    const senha = document.getElementById("senha").value;
    const errorDisplay = document.getElementById("error-message");

    try {

        const response = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({usuario: usuario, senha: senha})
        });

        const data = await response.json();

        if (!response.ok) {
            const errorMessage = Array.isArray(data.detail) 
                ? data.detail[0].msg 
                : (data.detail || "Login falhou");
            throw new Error(errorMessage);
        }

        localStorage.setItem("access_token", data.token);

        window.location.href = 'pedido.html';
    } catch (error) {
        errorDisplay.textContent = error.message;
    }
    
});