const input = document.getElementById("messageInput");
const messages = document.getElementById("messages");
const sendButton = document.getElementById("sendButton");
const welcome = document.getElementById("welcome");


function addMessage(text, type) {

    const message = document.createElement("div");

    message.className = `message ${type}`;

    const content = document.createElement("div");

    content.className = "message-content";

    content.innerText = text;

    message.appendChild(content);

    messages.appendChild(message);

    messages.scrollTop = messages.scrollHeight;
}


function showTyping() {

    const message = document.createElement("div");

    message.className = "message bot";

    message.id = "typing";

    message.innerHTML = `
        <div class="message-content">
            <span class="typing">
                MediBot is thinking...
            </span>
        </div>
    `;

    messages.appendChild(message);

    messages.scrollTop = messages.scrollHeight;
}


function removeTyping() {

    const typing = document.getElementById("typing");

    if (typing) {
        typing.remove();
    }
}


async function sendMessage() {

    const message = input.value.trim();

    if (!message) {
        return;
    }


    welcome.style.display = "none";

    addMessage(message, "user");

    input.value = "";

    sendButton.disabled = true;

    showTyping();


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        if (!response.ok) {
            throw new Error("Request failed");
        }


        const data = await response.json();

        removeTyping();

        addMessage(
            data.answer,
            "bot"
        );


    } catch (error) {

        removeTyping();

        addMessage(
            "Sorry, I couldn't process your question. Please try again.",
            "bot"
        );

        console.error(error);

    } finally {

        sendButton.disabled = false;

        input.focus();
    }
}


function askQuestion(question) {

    input.value = question;

    sendMessage();
}


function newChat() {

    messages.innerHTML = "";

    welcome.style.display = "block";

    input.value = "";

    input.focus();
}


function handleKeyDown(event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        sendMessage();
    }
}