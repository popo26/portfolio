function showContent(num) {
    const mainDiv = document.querySelector(`.main${num}`)
  mainDiv.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(`.c${num}`).style.display = "block";
    document.querySelector(`.title${num}`).innerText = "";
    document.querySelector(`.modal${num}`).style.backgroundColor = "transparent";
    document.querySelector(`.modal${num}`).style.opacity = 1;

    mainDiv.style.backgroundColor = "transparent";
    mainDiv.style.opacity = 1;

  });
}

const numOfItems = 12
for (let i=1;i<=numOfItems;i++){
    showContent(i);
}
