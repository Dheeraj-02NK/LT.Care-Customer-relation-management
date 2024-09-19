function signup() {
    window.location.href = 'signup.html';
}
function checkAuth() {
    const input = document.getElementById("input").value;
    let password = document.getElementById('password').value;

    if (input.length == 10) {
        alert("Login Successful!!")
        window.location.href = 'loginTable.html';
    }
    else if(password == String){
        window.location.href = 'complaint.html';
    }
    else {
        alert("Invalid Phone number")
    }
}
