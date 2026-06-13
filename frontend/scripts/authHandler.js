var formRegister = document.getElementById("RegisterForm")

formRegister.addEventListener('submit', async function (event) {
    event.preventDefault();
    form.style.display = "none";

    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const payload = {
        email: email,
        username: username,
        password: password
    };

    try {
        const response = await fetch("http://localhost:5500/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });


        if (response.ok) {
            console.log("User has been registered!");
        } else {
            console.error("Error while registering user");
        }

    } catch (error) {
        console.error("The user data has not been sent to the server, error:", error);
    }

    message.innerHTML = "<b>Form has been submitted</b>"
})