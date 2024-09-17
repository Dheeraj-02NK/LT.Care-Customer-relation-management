function checkAuth() {
    const input = document.getElementById("input").value;
    if (input.length == 10) {
        alert("Signup Successful!!")
        window.location.href = 'table.html';
    }
    else {
        alert("Invalid Phone number")
    }
}

function signup(){
    let fullname = $("#fullname").val();
    let phone = $("#phone").val();
    let email = $("#email").val();
    let password = $("#password").val();
    let role = $("#role").val();
    $.ajax({
        type:'POST',
        url:'/create_user/',
        data:{"fullname":fullname, "phone":phone, "email":email, "password":password, "role": role},
        success: function(data){
            if (data){
                window.location.replace('/login')
            }
        }
    })
}