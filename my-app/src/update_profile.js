// src/update_profile.js

document.addEventListener("DOMContentLoaded", function () {
    const updateProfileForm = document.getElementById("updateProfileForm");

    if (updateProfileForm) {
        updateProfileForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const formData = new FormData(updateProfileForm);

            fetch("/update_profile", {
                method: "POST",
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    // Handle the response data or update the UI as needed
                })
                .catch((error) => {
                    console.error("Error:", error);
                    // Handle errors or show an error message
                });
        });
    }
});
