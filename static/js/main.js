document.addEventListener('DOMContentLoaded', function() {
    const addRecipeBtn = document.getElementById('add-recipe-btn');
    const authModal = document.getElementById('authModal');
    const authClose = document.getElementById('authClose');
    const showRegister = document.getElementById('show-register');
    const showLogin = document.getElementById('show-login');
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    // Check if the 'Add Recipe' button exists
    if (addRecipeBtn) {
        // Add event listener to the 'Add Recipe' button
        addRecipeBtn.addEventListener('click', function() {
            checkLoginStatus().then(loggedIn => {
                if (loggedIn) {
                    window.location.href = '/add';
                } else {
                    authModal.style.display = 'block';
                }
            });
        });
    }

    // Check if the 'Close' button of the modal exists
    if (authClose) {
        // Add event listener to the 'Close' button to hide the modal
        authClose.onclick = function() {
            authModal.style.display = 'none';
        }
    }

    // Hide the modal when clicking outside of it
    window.onclick = function(event) {
        if (event.target == authModal) {
            authModal.style.display = 'none';
        }
    }

    // Check if the 'Show Register' link exists
    if (showRegister) {
        // Add event listener to switch from login form to register form
        showRegister.addEventListener('click', function() {
            loginForm.style.display = 'none';
            registerForm.style.display = 'block';
        });
    }

    // Check if the 'Show Login' link exists
    if (showLogin) {
        // Add event listener to switch from register form to login form
        showLogin.addEventListener('click', function() {
            registerForm.style.display = 'none';
            loginForm.style.display = 'block';
        });
    }

    // Function to check login status
    async function checkLoginStatus() {
        const response = await fetch('/is_logged_in');
        const data = await response.json();
        return data.logged_in;
    }

    // Check if the register form exists
    if (registerForm) {
        // Add event listener to handle the register form submission
        document.querySelector('#register-form form').addEventListener('submit', function(event) {
            event.preventDefault();
            const form = event.target;
            const formData = new FormData(form);

            // Send the registration data to the server
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            }).then(response => response.json()).then(data => {
                if (data.success) {
                    // If registration is successful, hide the modal and mark the user as logged in
                    authModal.style.display = 'none';
                    window.location.href = '/add'; // Redirect to add recipe page
                } else {
                    // If registration fails, show an alert with the error messages
                    alert('Registration failed: ' + JSON.stringify(data.errors));
                }
            }).catch(error => {
                console.error('Error:', error);
            });
        });
    }

    // Check if the login form exists
    if (loginForm) {
        // Add event listener to handle the login form submission
        document.querySelector('#login-form form').addEventListener('submit', function(event) {
            event.preventDefault();
            const form = event.target;
            const formData = new FormData(form);

            // Send the login data to the server
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            }).then(response => response.json()).then(data => {
                if (data.success) {
                    // If login is successful, hide the modal and mark the user as logged in
                    authModal.style.display = 'none';
                    window.location.href = '/add'; // Redirect to add recipe page
                } else {
                    // If login fails, show an alert with the error messages
                    alert('Login failed: ' + JSON.stringify(data.errors));
                }
            }).catch(error => {
                console.error('Error:', error);
            });
        });
    }
});
