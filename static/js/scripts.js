// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.getElementById("toggleTextButton");
    const toggleText = document.getElementById("toggleText");

    toggleButton.addEventListener("click", () => {
        // Toggle the visibility of the text
        if (toggleText.classList.contains("d-none")) {
            toggleText.classList.remove("d-none");
            toggleButton.textContent = "Show Less";
        } else {
            toggleText.classList.add("d-none");
            toggleButton.textContent = "Read More";
        }
    });
});
