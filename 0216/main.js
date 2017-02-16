var c=document.getElementById("slate")
var ctx=c.getContext("2d")
ctx.fillStyle = "#ff0000"

var animateDot = function(){
    var x=20;
    var drawDot = function(){
	console.log("dot!");
	ctx.clearRect(0,0,500,300)
	ctx.beginPath();
	ctx.arc(x%500,150,20,0,2*Math.PI);
	ctx.fill();
	x++;
	rid=window.requestAnimationFrame(drawDot);
    };
    drawDot();
};
var stopIt = function(){
    window.cancelAnimationFrame(rid)
};

var sb=document.getElementById("stop");
sb.addEventListener("click", stopIt);
c.addEventListener("click", animateDot);

