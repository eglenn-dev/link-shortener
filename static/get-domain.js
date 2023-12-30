function getDomain() {
    // Return the domain that the project is running on. 
    return window.location.hostname;
}

function updatePageContent() {
    // Gets the page domain.
    var domain = getDomain();
    // Getting the element to host the domain URL.
    var linkElement = document.getElementById("entire-url");
    if (domain && linkElement) {
        // Setting the text content of the element to the domain. 
        linkElement.textContent = domain;
    }
}

function copyToClipboard() {
    // Get the text field
    var copyText = document.getElementById("whole-url");

    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);

    // Alert the copied text
    alert("Copied the text: " + copyText.value);
}