
    function validate() {
        event.preventDefault();
        let pass = $('#password').val();
        if (pass.match("^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}") &&
        $('#password').val() == $('#password2').val()) {
            // registerUser();
            $.post("http://localhost:8000/register/",
                { 
                    csrfmiddlewaretoken: window.CSRF_TOKEN,
                    username: $('#username').val(),
                    password: $('#password').val(),
                    email: $('#email').val(),
                }). done(function() {
                    alert("registered!")
                })  
                .fail(function() {
                    alert("Email already registered!");
                });
        } else {
            alert("Password doest matches given format!");
        }
    }