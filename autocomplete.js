// Array of sample data for autocomplete suggestions
const searchData = [
    "Allie",
    "Melody",
    "Jacqueline",
    "Kristie",
    "iEEE"
];

let selectedIndex = -1; // Tracks the current selected suggestion

function showSuggestions() {
    const input = document.getElementById("search-input").value.toLowerCase();
    const suggestionsBox = document.getElementById("suggestions");
    suggestionsBox.innerHTML = ""; // Clear previous suggestions
    selectedIndex = -1; // Reset the selected index

    if (input) {
        // Filter the searchData array for suggestions that match the input
        const filteredSuggestions = searchData.filter(item =>
            item.toLowerCase().includes(input)
        );

        // Create a suggestion item for each match
        filteredSuggestions.forEach((suggestion, index) => {
            const suggestionItem = document.createElement("div");
            suggestionItem.classList.add("suggestion-item");
            suggestionItem.textContent = suggestion;

            // Handle click event to select the suggestion
            suggestionItem.onclick = () => selectSuggestion(suggestion);

            suggestionsBox.appendChild(suggestionItem);
        });
    }
}

function selectSuggestion(suggestion) {
    document.getElementById("search-input").value = suggestion; // Fill input with selected suggestion
    document.getElementById("suggestions").innerHTML = ""; // Clear suggestions
}

// Handle keyboard navigation for autocomplete
function handleKeyDown(event) {
    const suggestionsBox = document.getElementById("suggestions");
    const items = Array.from(suggestionsBox.getElementsByClassName("suggestion-item"));

    if (event.key === "ArrowDown") {
        // Move selection down
        selectedIndex = (selectedIndex + 1) % items.length;
        updateSelection(items);
    } else if (event.key === "ArrowUp") {
        // Move selection up
        selectedIndex = (selectedIndex - 1 + items.length) % items.length;
        updateSelection(items);
    } else if (event.key === "Enter") {
        // Select the current item on Enter
        if (selectedIndex > -1) {
            selectSuggestion(items[selectedIndex].textContent);
            selectedIndex = -1;
            event.preventDefault(); // Prevent form submission
        }
    }
}

function updateSelection(items) {
    // Remove 'selected' class from all items and apply it to the selected one
    items.forEach((item, index) => {
        item.classList.toggle("selected", index === selectedIndex);
    });
}
