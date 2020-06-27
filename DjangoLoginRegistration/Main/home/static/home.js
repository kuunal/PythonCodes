$(document).ready(function(){
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
            }
        }
    });        

    $(document).on("click","#logout",function(){
        event.preventDefault();
        if(!localStorage.key(0)){
            window.location = "/login/";
        }else{
            $.ajax({
                url:"/home/logout/",
                TYPE:"GET",
                headers:{
                    'x-email':email,
                    'x-token': 'bearer ' +token
                },
                success: function(data){
                    if(data==200){
                        localStorage.removeItem(email); 
                        window.location = "/login/"; 
                    }else{
                        alert(data);
                    }
                }
            });
        }
    });
}); 
