
function authenticate(){    
    let email = $('#email-id').val();
    let password = $('#pass').val();    
    event.preventDefault();
    $.post("http://localhost:8000/login/",{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            email:email,
            password:password
            }).done((data)=>{
            alert(data)
        })
        .fail((data)=>{
            // alert(data.status)
        })

}