var landingDIV = document.getElementById('landing-div');
var canvas = document.getElementById('landing-canvas');
var ctx = canvas.getContext('2d');

alert("This portfolio site and link are out dated. You will be redirected to konnersawyers.ddns.net.")

function contact_function(){
    alert("Email me at konnersawyersofficial@gmail.com");
}


const pointArray = [];

var i = 0;
while (i < 16){
    pointArray.push([Math.random(), Math.random()])
    console.log(pointArray[i])
    i++
}

landingDIV.addEventListener("mousemove", (event) =>{

    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    //ctx.moveTo(0,0);
    //ctx.lineTo(event.pageX, event.pageY);
    ctx.stroke();
    i = 0;
    while (i < pointArray.length){
        var distance = Math.sqrt(Math.pow(Math.abs(event.pageX - pointArray[i][0] * canvas.width), 2) + Math.pow(Math.abs(event.pageY - pointArray[i][1] * canvas.height), 2))
        ctx.beginPath();
        ctx.arc(pointArray[i][0]*canvas.width,pointArray[i][1]*canvas.height,1,0,2*Math.PI);
        ctx.stroke();
        if( distance < 255 ){
            ctx.strokeStyle = (`rgba(52, 68, 73, ${(255/distance) - 1})`);
            ctx.lineTo(event.pageX,event.pageY)
        }
        ctx.stroke();
        ctx.strokeStyle = ('rgba(0,0,0,1')
        i++
    }



});

