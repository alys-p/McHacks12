const canvas = document.querySelector("canvas");
const secondsCount = document.querySelector(".seconds");
const level = document.querySelector(".grade");
const context = canvas.getContext("2d");
const timerDiv = document.querySelector(".timer");
const animalDim = { width: 160 * 2.5, height: 120 * 2.5};
const startTime = Date.now();

const levels = {
  5: "Sr Assistant",
  10: "Apprentice",
  15: "Sr Apprentice",
  15: "Jr Honoror",
  15: "Master Honoror",
  35: "S Tier Honoror",
  50: "Master",
  75: "GrandMaster",
  100: "GranderMaster",
  150: "Priest",
  250: "Sage",
  350: "CEO",
  450: "Pope",
  500: "Underlord",
  750: "Lord",
  900: "OverLord",
  1000: "King",
  2000: "GOD",
  3600: "unemployed",
}

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
context.translate(window.innerWidth / 2, window.innerHeight / 2);

const image = new Image()
image.src = "./capybaraa.png";

const loopingCapys = 50;
const offsetDistance = 190;
let currentOffset = 0;

const gif = document.createElement("img");
gif.src = "./capybaragif.gif";
gif.style.position = "absolute";
gif.style.top = "50%";
gif.style.left = "50%";
gif.style.transform = "translate(-50%, -50%)";
gif.style.opacity = "0"
gif.style.width = "700px"; // Adjust the width of the GIF
gif.style.height = "auto";
gif.style.zIndex = "101"
document.body.appendChild(gif);

const video = document.createElement("video");
video.src = "./galaxy.mp4";
video.style.position = "absolute";
video.style.top = "0";
video.style.left = "0";
video.style.width = "100vw"; // Full canvas width
video.style.height = "auto";
video.style.opacity = "0";
video.style.zIndex = "100"
video.loop = true;
document.body.appendChild(video);

image.onload = () => {
 startLooping();
};

function draw(offset) {
 context.drawImage(image,-animalDim.width/2 - offset/2 ,-animalDim.height/2 - offset/2, animalDim.width + offset , animalDim.height + offset)
}

function loopDraw() {
  for (let i = loopingCapys; i >= 1; i--) {
    draw(i * offsetDistance + currentOffset);
    draw(offsetDistance,1);

  }
  currentOffset++;
  if (currentOffset >= offsetDistance) {
    currentOffset = 0;
  }

  const newTime = Math.floor((Date.now() - startTime) / 1000);

  secondsCount.innerText = newTime;


  if(levels[newTime]) {
    level.innerText = levels[newTime]
  }

  requestAnimationFrame(loopDraw)
}

function startLooping() {
  requestAnimationFrame(loopDraw);
}

// Show GIF on mouse down and hide on mouse up
window.addEventListener("mousedown", () => {
  gif.style.opacity = "1"; // Make the GIF visible
  video.style.opacity = "1";
  video.play();
  canvas.style.opacity = "0"; // Hide the canvas
  timerDiv.style.opacity = "1";
  timerDiv.style.zIndex = "102";
});


window.addEventListener("mouseup", () => {
  gif.style.opacity = "0"; // Hide the GIF
  video.style.opacity = "0";
  video.pause();
  canvas.style.opacity = "1"; // Show the canvas
  timerDiv.style.opacity = "1"; // Show the timer
});


