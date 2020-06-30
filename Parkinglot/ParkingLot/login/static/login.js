$(document).ready(()=>  {
    $.ajax({
        url:"/register/check/",
        headers:{
            "x-token" : localStorage.key(0)
        },success: function(data){
            if(data==302){
                window.location = "/home/";
            }
        }
    })
});


function authenticate() {
    let email = $('#email-id').val();
    let password = $('#pass').val();
    event.preventDefault();
    $.post("/login/", {
        csrfmiddlewaretoken: window.CSRF_TOKEN,
        email: email,
        password: password
    }).done((data) => {
        if (data.status == 200) {
            localStorage.setItem(data.user, data.token);
            window.location = "/home/";
        } else {
            for (status in data) {
                alert(data[status]);
            }
        }
    }).fail(() => {
            alert("Something went wrong!");
        })

}

