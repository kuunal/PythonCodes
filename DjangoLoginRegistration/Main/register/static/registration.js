    $.ajax({
        url:"/register/check/",
        headers:{
            "x-token" : localStorage.key(0)
        },success: function(data){
            if(data==302){
                window.location = "/home/";
            }
        }
    });


    
    function validation() {
        event.preventDefault();
        let pass = $('#password').val();
        if (pass.match("^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}") &&
        $('#password').val() == $('#password2').val()) {
            $.post("/register/",
                { 
                    csrfmiddlewaretoken: window.CSRF_TOKEN,
                    username: $('#username').val(),
                    password: $('#password').val(),
                    email: $('#email').val(),
                }).done(function(data) {
                    for(response in data){
                        if(response==200){
                            window.location="/login/"
                        } else if(response==400)
                            alert("Email already exist");
                        
                    }
                })  
                .fail(function() {
                    alert("Server Down");
                });
        } else {
            alert("Password doest matches given format!");
        }
    }





