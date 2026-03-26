var count = 3;

function addLike() {
    var likesCount = document.querySelector("#likes");
    count++; //count=count+1
    likesCount.innerText = count;
}