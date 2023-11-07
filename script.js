document.addEventListener("DOMContentLoaded", function() {
    var loginForm = document.getElementById('loginForm');
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();

        var input1 = document.getElementById("userid").value.trim();
        var input2 = document.getElementById("password").value.trim();


        if(input1 === "ABC200001" && input2 === "P4ssword@UTD") {
            window.location.href = "home.html";
        } else {
            document.getElementById("rejection").style.display = "block";
        }
    });
});
