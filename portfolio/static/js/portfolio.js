
function showContent(num) {
    const modalDiv = document.querySelector(`.modal${num}`);
    const cardBody = document.querySelector(`.c${num}`);
    const centerTitle = document.querySelector(`.title${num}`);
    modalDiv.addEventListener("click", function (e) {

      e.preventDefault();
      if (cardBody.style.display === "block"){
        cardBody.style.display = "none";
        centerTitle.style.display = "block";
        modalDiv.style.backgroundColor =
          "#777";
        modalDiv.style.opacity = 0.3;
    } else {
        cardBody.style.display = "block";
        centerTitle.style.display = "none";
        modalDiv.style.backgroundColor =
          "transparent";
        modalDiv.style.opacity = 1;
        modalDiv.style.backgroundColor = "transparent";
        modalDiv.style.opacity = 1;
    }
    });
  }
  


const numOfItems = 12;
for (let i = 1; i <= numOfItems; i++) {
  showContent(i);
}

