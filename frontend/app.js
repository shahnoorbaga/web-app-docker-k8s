const backendUrl = "/api"

document.getElementById('rootForm').addEventListener('submit', async function (e) {
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

    // Fetch and display submitted data
    fetchData();
});

async function fetchData() {
    const response = await fetch(`${backendUrl}/data`); // Endpoint to fetch data
    const data = await response.json();

    // Display each entry
    const dataDisplay = document.getElementById('dataTable');
    dataDisplay.innerHTML = ''; // Clear previous data
    data.forEach(entry => {
        const div = document.createElement('div');
        div.textContent = `Name: ${entry.name}, Email: ${entry.email}`;
        dataDisplay.appendChild(div);
    });
}
