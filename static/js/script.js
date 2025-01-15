document.getElementById("upload-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(this);

    fetch("/upload", {
        method: "POST",
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById("result");
            if (data.error) {
                resultDiv.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `<p>Deepfake Probability: <strong>${data.deepfake_percentage}</strong></p>`;
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
});
