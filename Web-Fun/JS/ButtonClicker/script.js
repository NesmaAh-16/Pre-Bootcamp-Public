function changInnerTxt(element) {
    if(element.innerText == "Login"){
        element.innerText = "Logout";
        console.log("buttonLogout")
    }
    else if(element.innerText == "Logout") {
        element.innerText = "Login";
         console.log("buttonLogin")
    }
};
function remove(element) {
    element.remove();
};
function showAlert() {
    alert("Ninja was liked!");
};
