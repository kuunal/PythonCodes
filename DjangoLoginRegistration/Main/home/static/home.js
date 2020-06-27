$(document).ready(()=>{
    nav1 = $('#nav ul li:first-child');
    nav2 = $('#nav ul li:nth-child(2) a');
    nav3 = $('#nav ul li:last-child a');
    email=localStorage.key(0);
    token=localStorage.getItem(email);
        $.ajax({
        url:"/home/"+email+"/",
        headers:{'x-token': 'bearer ' +token},
        success: function(data){
            if (data.status==200){
                nav1.text("Welcome "+data.user);
                nav2.text("Settings").css("color","white");  
                nav3.text("Logout").css("color","white");     
                console.log(data)        
            }
        }
    })        


    $(document).on("onclick",nav3,function(){
        event.preventDefault();
        console.log("ASSSSSSSSSSSSSSSSSSSSSSSSSSSS")
        if(nav3.text()==="Login"){
            window.location = "/login/";
            console.log("ADADASDASDASDASDASDASDSADSSD")
        }else{
            localStorage.removeItem(email); 
            $.ajax({
                url:"/home/logout",
                headers:{
                    'x-email':email,
                    'x-token':token
                },
                success: (data)=>{
                    if(data==200){
                        window.location = "/login/"; 
                    }
                }
            })
        }
    })
}); 
