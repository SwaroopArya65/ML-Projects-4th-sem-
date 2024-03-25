function showLoginForm() {
    var loginForm = document.getElementById("loginForm");
    var registerBtn = document.getElementById("registerBtn");
    var loginBtn = document.getElementById("loginBtn");

    // Show login form
    loginForm.style.display = "block";
    // Hide registration button and login button
    registerBtn.style.display = "none";
    loginBtn.style.display = "none";
}

function showRegistrationForm() {
    var registrationForm = document.getElementById("registrationForm");
    var registerBtn = document.getElementById("registerBtn");
    var loginBtn = document.getElementById("loginBtn");

    // Show registration form
    registrationForm.style.display = "block";
    // Hide login button and registration button
    loginBtn.style.display = "none";
    registerBtn.style.display = "none";
}