function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "admin" && password == "admin") {
        alert("Login Successful");
        return false;


    } else {
        alert("Login failed");
        return true;

    }


}