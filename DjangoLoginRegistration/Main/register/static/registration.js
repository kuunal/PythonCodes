    function validate() {
        event.preventDefault();
        console.log("asdasds");
        let pass = $('#password').val();
        if (pass.match("^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}")) {
            // registerUser();
            $.post("http://localhost:8000/register/",
                { 
                    csrfmiddlewaretoken: window.CSRF_TOKEN,
                    first_name: $('#firstname').val(),
                    last_name: $('#lastname').val(),
                    email: $('#email').val(),
                    password: $('#password').val()
                }). done(function() {
                    alert("Email registered!");
                })
                .fail(function() {
                    alert("Email already registered!");
                });
        } else {
            alert("Password doest matches given format!");
        }
    }