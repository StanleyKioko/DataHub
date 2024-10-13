// script.js

// This function handles form submission
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form"); // Selects the form element

    if (form) {
        form.addEventListener("submit", function(event) {
            // Show a simple alert on form submission
            alert("Form is being submitted!");
            // You can perform additional actions here (like form validation)
        });
    }
});
