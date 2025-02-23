// Grab elements from the DOM
const imageUploadInput = document.getElementById('imageUpload');
const allergyDropdown = document.getElementById('allergyDropdown');
const processButton = document.getElementById('processButton');
const flashcard = document.getElementById('flashcard');

let selectedFile = null;
let selectedAllergy = null;

// Listen for file selection
imageUploadInput.addEventListener('change', (event) => {
  selectedFile = event.target.files[0]; // The file object
});

// Listen for dropdown change
allergyDropdown.addEventListener('change', (event) => {
  selectedAllergy = event.target.value;
});

// Process button click
processButton.addEventListener('click', () => {
  if (!selectedFile) {
    flashcard.textContent = 'Please select an image first.';
    return;
  }
  if (!selectedAllergy) {
    flashcard.textContent = 'Please select an allergy.';
    return;
  }

  // Example: Show basic info locally (no backend call yet)
  flashcard.innerHTML = `
    <p>File name: ${selectedFile.name}</p>
    <p>Allergy chosen: ${selectedAllergy}</p>
    <p>Processing... (Here you would call the backend)</p>
  `;

  // If you want to send data to a backend endpoint, do something like:
  /*
  const formData = new FormData();
  formData.append('image', selectedFile);
  formData.append('allergy', selectedAllergy);

  fetch('YOUR_BACKEND_ENDPOINT_URL', {
    method: 'POST',
    body: formData
  })
    .then((res) => res.json())
    .then((data) => {
      // data might have the extracted text
      flashcard.textContent = data.extractedText;
    })
    .catch((err) => {
      flashcard.textContent = 'Error: ' + err.message;
    });
  */
});
