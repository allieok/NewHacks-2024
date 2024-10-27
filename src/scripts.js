// Function to show selected tab content
function showContent(tabName) {
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => {
        content.style.display = content.id === tabName ? 'block' : 'none';
    });
}

//need to add data limits

// Event listeners for input changes
document.getElementById("dataLimit").addEventListener("input", function() {
    suggestLimit(this, dataLimits, document.getElementById("dataSuggestion"));
});

document.getElementById("callLimit").addEventListener("input", function() {
    suggestLimit(this, callLimits, document.getElementById("callSuggestion"));
});

// Validate limits to ensure non-negative values and save to local storage
function validateLimits() {
    const dataLimit = document.getElementById("dataLimit").value;
    const callLimit = document.getElementById("callLimit").value;

    if (dataLimit < 0 || callLimit < 0) {
        alert("Monthly limits for data and calls cannot be negative. Please enter valid numbers.");
        return false;
    }

    // Save to local storage (web storage feature)
    localStorage.setItem("monthlyDataLimit", dataLimit);
    localStorage.setItem("monthlyCallLimit", callLimit);
    
    alert("Settings saved!");
    return true;
}

// Load saved limits when the page loads
window.onload = function() {
    const savedDataLimit = localStorage.getItem("monthlyDataLimit");
    const savedCallLimit = localStorage.getItem("monthlyCallLimit");

    if (savedDataLimit !== null) {
        document.getElementById("dataLimit").value = savedDataLimit;
    }
    if (savedCallLimit !== null) {
        document.getElementById("callLimit").value = savedCallLimit;
    }
};


// Function to register a user
function registerUser() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Save email and password to localStorage (for demo purposes; in real apps, use a secure backend)
    if (email && password) {
        localStorage.setItem("userEmail", email); //Storing email
        sendConfirmationEmail(email); // Send confirmation email
        alert("Registration successful! Check your email for confirmation.");
        window.location.href = "login.html";  // Redirect to login page
        return true;
    } else {
        alert("Please enter a valid email and password.");
        return false;
    }
}

// Function to send a confirmation email
function sendConfirmationEmail(email) {
    const templateParams = {
        to_email: email,
        subject: "Registration Confirmation",
        message: "Thank you for registering with our Telecom App!"
    };

    emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", templateParams)
        .then((response) => {
            console.log('Email sent successfully!', response.status, response.text);
        }, (err) => {
            console.error('Failed to send email. Error:', err);
        });
}

// Function to log telecom usage and send notification if below threshold
function logTelecomRemain() {
    const dataRemain = parseInt(document.getElementById("dataRemain").value, 10); // Get data usage input
    const email = localStorage.getItem("userEmail"); // Retrieve stored email

    // Check if the data usage is below the threshold
    if (dataRemain <= 100 && email) {
        sendUsageNotificationEmail(email, Remain); // Send notification email
        alert("You are low in data and notification email sent!");
    } else if (dataRemain > 100 ){
        alert("Usage logged successfully. You have sufficient amount of data.");
    }
}

// Function to send a usage notification email
function sendUsageNotificationEmail(email, dataRemain) {
    const templateParams = {
        to_email: email,
        subject: "Data Usage Notification",
        message: `Your current data usage is ${dataRemain}. Please be mindful that it's below the threshold of 100.`
    };

    emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", templateParams)
        .then((response) => {
            console.log('Usage notification email sent successfully!', response.status, response.text);
        }, (err) => {
            console.error('Failed to send usage notification email. Error:', err);
        });
}

// Function to log in a user
function loginUser() {
    const enteredEmail = document.getElementById("loginEmail").value;
    const enteredPassword = document.getElementById("loginPassword").value;

    // Retrieve stored email and password
    const storedEmail = localStorage.getItem("userEmail");
    const storedPassword = localStorage.getItem("userPassword");

    // Check if entered credentials match stored credentials
    if (enteredEmail === storedEmail && enteredPassword === storedPassword) {
        alert("Login successful!");
        window.location.href = "index.html";  // Redirect to homepage
        return true;
    } else {
        alert("Incorrect email or password. Please try again.");
        return false;
    }
}

// Function to check login status on the homepage
function checkLoginStatus() {
    const userEmail = localStorage.getItem("userEmail");
    if (userEmail) {
        document.getElementById("welcome-section").innerHTML = `<h2>Welcome back, ${userEmail}!</h2>`;
    } else {
        document.getElementById("welcome-section").innerHTML = "<h2>Welcome to Telecom App! Please log in to access your account.</h2>";
    }
}

// Function to log out
function logoutUser() {
    localStorage.removeItem("userEmail"); // Remove email from local storage
    alert("You have been logged out.");
    window.location.reload();  // Refresh the page to update UI
}




/*
// Function to suggest closest limit based on user input
function suggestLimit(inputElement, limitArray, suggestionElement) {
    const inputValue = parseInt(inputElement.value, 10);
    suggestionElement.textContent = ''; // Clear previous suggestion

    if (!isNaN(inputValue) && inputValue >= 0) {
        // Find closest limit
        const closestLimit = limitArray.reduce((prev, curr) => {
            return (Math.abs(curr - inputValue) < Math.abs(prev - inputValue) ? curr : prev);
        });

        // Display suggestion
        suggestionElement.textContent = `Did you mean: ${closestLimit}?`;
    }
}
*/