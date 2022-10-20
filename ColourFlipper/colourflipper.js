const colors = ["green", "red", "blue", "#f15025", "rgba(133,122,200"];
const button = document.getElementById("button");
const color = document.querySelector(".colors");

button.addEventListener("click", function() {
    //get random number between 0-3
    const randomNumber = getRandomNumber();
    console.log(randomNumber);

    document.body.style.backgroundColor = colors[randomNumber];
    color.textContent=colors;
});

function getRandomNumber() {
    return Math.floor(Math.random() * colors.length);
}
