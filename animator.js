const canvas = document.querySelector("canvas");
const context = canvas.getContext("2d");
const animalDim = { width: 353 * 1.2, height: 325 * 1.2 };


canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const image = new Image()
image.src = "./capyybara.png";
image.onload = () => {
  draw();
};

function draw() {
  context.drawImage(
    image,0,0, 400, 500)
}