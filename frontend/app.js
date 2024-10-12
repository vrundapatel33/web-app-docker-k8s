document.getElementById('dataForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const value1 = document.getElementById('value1').value;
    const value2 = document.getElementById('value2').value;

    // Simple validation
    if (value1 === '' || value2 === '') {
        alert('Please fill in both values.');
        return;
    }

    const data = { value1, value2 };

    fetch('http://34.31.239.175:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert('Data submitted successfully!');
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
