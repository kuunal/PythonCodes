$(document).ready(()=>  {
        
    $.ajax({
        url:"/register/check/",
        headers:{
            "x-token" : localStorage.key(0)
        },success: function(data){
            if(data==302){
                window.location = "/home/"+localStorage.key(0)+"/";
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
            console.log("SAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", data.user, data)
            localStorage.setItem(data.user, data.token);
            window.location = "/home/" + data.user + "/";
        } else {
            for (status in data) {
                alert(data[status]);
            }
        }
    })
        .fail(() => {
            // alert(data.status)
        })

}