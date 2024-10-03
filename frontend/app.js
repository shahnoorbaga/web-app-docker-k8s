document.addEventListener("DOMContentLoaded", async function () {
    try {
        const configResponse = await fetch('/config');
        const config = await configResponse.json();
        const backendUrl = config.backend_url;

        document.getElementById('dataForm').addEventListener('submit', async function (e) {
            e.preventDefault();

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;

            const response = await fetch(`${backendUrl}/submit`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, email })
            });

            const result = await response.json();
            document.getElementById('message').textContent = result.message;
        });
    } catch (error) {
        console.error("Error loading configuration:", error);
    }
});
