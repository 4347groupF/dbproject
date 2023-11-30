console.log('menu.js loaded');
document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const menuList = document.getElementById("menu-list");

    menuIcon.addEventListener("click", function () {
        if (menuList.style.display === "block") {
            menuList.style.display = "none";
        } else {
            menuList.style.display = "block";
            menuList.style.position = "absolute";
            menuList.style.top = menuIcon.getBoundingClientRect().bottom + "px";
            menuList.style.right = "0"; // Adjust this if needed
        }
    });

});
