document.addEventListener('DOMContentLoaded', () => {
  // Grab elements from the DOM
  const imageUploadInput = document.getElementById('imageUpload');
  const allergySelect = document.getElementById('allergySelect');
  const processButton = document.getElementById('processButton');
  const flashcard = document.getElementById('flashcard');

  // We no longer need separate divs for label, summary, etc.
  // All relevant info will be displayed inside the flashcard element.
  // Hence, we remove references to healthLabelDiv, summaryOutputDiv, etc.

  let selectedFile = null;
  let selectedAllergies = [];

  // Debugging: Log elements to ensure they're found
  console.log({
    imageUploadInput, allergySelect, processButton, flashcard
  });

  // Listen for file selection
  imageUploadInput.addEventListener('change', (event) => {
    selectedFile = event.target.files[0];
  });

  // Listen for multiple select changes
  allergySelect.addEventListener('change', (event) => {
    // Get all selected options (ignoring "None")
    const options = Array.from(allergySelect.selectedOptions);
    selectedAllergies = options.map(option => option.value).filter(val => val !== "None");
  });

  // Process button click
  processButton.addEventListener('click', () => {
    if (!selectedFile) {
      flashcard.innerHTML = '<p>Please select an image first.</p>';
      return;
    }

    // Build form data to send to backend
    const formData = new FormData();
    formData.append('file', selectedFile);
    // Join selected allergies into a comma-separated string
    formData.append('allergy', selectedAllergies.join(',') || "None");

    // Display processing message
    flashcard.innerHTML = `<p>Processing... Please wait.</p>`;

    // Send request to backend endpoint with full URL and CORS mode
    fetch('http://127.0.0.1:8000/upload/', {
      method: 'POST',
      mode: 'cors', // Tells the browser to expect CORS headers from the server
      body: formData
    })
      .then(response => {
        console.log("Response status:", response.status);
        return response.json();
      })
      .then(data => {
        console.log("Data received from backend:", data);

        // Clear the processing message
        flashcard.innerHTML = "";

        // 1) Health Label (model_prediction)
        let healthLabel = data.model_prediction || "Unknown";
        let badgeColor = "";
        if (healthLabel.toLowerCase() === "healthy") {
          badgeColor = "green";
        } else if (healthLabel.toLowerCase() === "moderately_healthy") {
          badgeColor = "orange";
        } else if (healthLabel.toLowerCase() === "unhealthy") {
          badgeColor = "red";
        } else {
          badgeColor = "gray";
        }

        // 2) Allergy Warning
        const allergyWarning = data.allergy_warning || "Not provided";

        // 3) Nutrition Summary
        const nutritionSummary = data.nutrition_summary || "Not provided";

        // 4) Daily Intake Recommendation
        const dailyIntake = data.daily_intake_recommendation || "Not provided";

        // Display all fields inside the flashcard
        flashcard.innerHTML += `
          <p><strong>Health Label:</strong>
            <span style="color: ${badgeColor}; font-weight: bold;">
              ${healthLabel}
            </span>
          </p>
          <p style="color: red;">
            <strong>Allergy Warning:</strong>
            ${allergyWarning}
          </p>
          <p><strong>Nutrition Summary:</strong> ${nutritionSummary}</p>
          <p><strong>Daily Intake Recommendation:</strong> ${dailyIntake}</p>
        `;
      })
      .catch(error => {
        console.error("Error occurred:", error);
        flashcard.innerHTML = `<p>Error: ${error.message}</p>`;
      });
  });
});
