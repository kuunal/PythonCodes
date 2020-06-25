
function authenticate(){    
    let email = $('#email-id').val();
    let password = $('#pass').val();    
    event.preventDefault();
    $.post("/login/",{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            email:email,
            password:password
            }).done((data)=>{
                for(status in data){
                    if(status==200){
                        window.location="/home/";
                        break;
                    }
                    alert(data[status]);
                }
                })
        .fail(()=>{
            // alert(data.status)
        })

}