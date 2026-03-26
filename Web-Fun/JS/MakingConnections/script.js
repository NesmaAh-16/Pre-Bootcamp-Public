
function changeName() {
    var userName = document.querySelector("#user-name");
    userName.innerText = "Nesma Ahmad";
}

var connectionRequests = document.querySelector("#connection-requests");
var yourConnections = document.querySelector("#your-connections");

function accept(id) {
    var elem = document.querySelector("#" + id);
    elem.remove();

    connectionRequests.innerText--;
    yourConnections.innerText++;
}

function reject(id) {
    var elem = document.querySelector("#" + id);
    elem.remove();

    connectionRequests.innerText--;

}