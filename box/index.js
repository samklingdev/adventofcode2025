console.log(game);

game.width = 800;
game.height = 600;
const ctx = game.getContext("2d");

ctx.fillStyle = "black";
ctx.fillRect(0, 0, game.width, game.height);

ctx.fillStyle = "green";
ctx.fillRect(100, 100, 10, 10);

