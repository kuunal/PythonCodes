

function authenticate(){    
    let email = $('#email-id').val();
    let password = $('#pass').val();
    
    console.log(email,password,"SADSADSADSADSADSADSADASDAS")
    $.post("http://localhost:7000/login/",{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            email:email,
            password:password
        }).done()
        .fail(()=>{
            alert("Somethong went wrong!")
        })

}