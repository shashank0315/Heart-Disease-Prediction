document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("prediction-form").addEventListener("submit", function(event) {
        event.preventDefault();

        // Get form data
        let formData = new FormData(this);

        // Send data to Flask backend
        fetch("/predict", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("result").textContent = "Error: " + data.error;
            } else {
                document.getElementById("result").textContent = "Prediction: " + data.prediction;
            }
        })
        .catch(error => console.error("Error:", error));
    });
});
