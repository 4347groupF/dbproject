document.addEventListener("DOMContentLoaded", function() {
    var loginForm = document.getElementById('loginForm');
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();

        var input1 = document.getElementById("userid").value.trim();
       


        if(input1 === "ABC200001") {
            window.location.href = "index.html";
        } else {
            document.getElementById("rejection").style.display = "block";
        }
    });
});
