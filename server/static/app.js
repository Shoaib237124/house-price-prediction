document.addEventListener('DOMContentLoaded', () => {
    const locationSelect = document.getElementById('location');
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('result');

    // Fetch locations from backend
    fetch('/get_location_names')
        .then(response => response.json())
        .then(data => {
            locationSelect.innerHTML = '';
            data.locations.forEach(loc => {
                const option = document.createElement('option');
                option.value = loc;
                option.textContent = loc;
                locationSelect.appendChild(option);
            });
        })
        .catch(() => {
            locationSelect.innerHTML = '<option value="">Failed to load</option>';
        });

    // Handle form submission
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        resultDiv.textContent = 'Predicting...';

        const area = document.getElementById('area').value;
        const bedrooms = document.getElementById('bedrooms').value;
        const bathrooms = document.getElementById('bathrooms').value;
        const location = locationSelect.value;

        const formData = new FormData();
        formData.append('total_sqft', area);
        formData.append('bhk', bedrooms);
        formData.append('bath', bathrooms);
        formData.append('location', location);

        fetch('/predict_price', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data && data.estimated_price) {
                const price = parseFloat(data.estimated_price).toFixed(2);
                resultDiv.textContent = `Predicted Price: ₹${price} Lakh`;
            } else {
                resultDiv.textContent = 'Prediction failed.';
            }
        })
        .catch(() => {
            resultDiv.textContent = 'Error connecting to server.';
        });
    });
});
