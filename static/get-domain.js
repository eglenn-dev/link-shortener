function getDomain() {
    var url = window.location.href;
    var domain = new URL(url).hostname;
    return domain;
}

function updatePageContent() {
    var domain = getDomain();
    var linkElement = document.getElementById("entire-url");
    if (domain && linkElement) {
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