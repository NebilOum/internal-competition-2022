// writing the correct path is important, the ./ here means that `index.js` is in the same folder as methods.js
// otherwise, you would use the relative path. for example if `index.js` was in the same folder as `index.html`
// you would update the import to say `from "./js/methods.js"`
import {createArrow, createJoyStick} from "./methods.js"

// creates a left arrow under the div 'tutorial-right-arrow' with size 100px
//createArrow('left', 'arrows', 64)
let direction;
let jybaseSize = 300;
let x=jybaseSize/2,y=jybaseSize/2,xSpeed,ySpeed;
let intakePos = "noSpin"
buttonEvent("intake")
buttonEvent("out")
keyBoardEvent()
//wiiMoteEvent()

// creates a joystick 
const joystick = createJoyStick({
    baseSize: '300px',
    stickSize: '128px',
    baseColor: 'black',
    stickColor: 'darkred'
}, joystickHandler);

function joystickHandler(x, y) {
    console.log(x, y);
    if(x < 0) { direction = "negDirection" }
    else if (y < 0) { direction = "negDirection" }
    else { direction = "posDirection" }
    xSpeed = Math.abs((Math.abs(x)-(jybaseSize/2))/((jybaseSize/2)));
    ySpeed = Math.abs((Math.abs(y)-(jybaseSize/2))/((jybaseSize/2)));
    if(xSpeed > 100) {
        xSpeed = 100;
    }
    else if(ySpeed > 100){
            ySpeed = 100;
    }
    else if(xSpeed < 0){
        xSpeed = 0;
    }
    else if(ySpeed < 0){
        ySpeed = 0;
    }
    /// sends information to robot
    sendToBot({
        "xJoystickPos" : xSpeed,
        "yJoystickPos" : ySpeed,
        "driveDirection" : direction,
        "driveType" : "tank",
        "intake" : intakePos
    })
}

/// event listener for buttons
function buttonEvent(buttonID){
     const element = document.getElementById(buttonID);
     element.addEventListener("click",function({target}){buttonClick(target.id)});
}

function keyBoardEvent(){

    document.addEventListener('keydown', (event) => {
        if(!event.shiftKey){
            if(event.key.toLowerCase() == "w" ) {
                ySpeed = 50;
                direction = "posDirection";
                console.log('w pressed');
            }
            else if(event.key.toLowerCase() == "s") {
                ySpeed = 50;
                direction = "negDirection"
                console.log('s pressed');
            }
            if(event.key.toLowerCase() == "a") {
                xSpeed = 50;
                direction = "negDirection";
                console.log('a pressed');
            }
            else if(event.key.toLowerCase() == "d") {
                xSpeed = 50;
                direction = "posDirection";
                console.log('d pressed');
            }
            else if(event.key.toLowerCase() == "i") {
                intakePos = "spinInward";
                console.log('intake was pressed');
            }
            else if(event.key.toLowerCase() == "o") {
                intakePos = "spinOutward";
                console.log('spit was pressed');
            }
            console.log("yspeed" + ySpeed);
            console.log("xspeed" + xSpeed);
            sendToBot({
                "xJoystickPos" : xSpeed,
                "yJoystickPos" : ySpeed,
                "driveDirection" : direction,
                "driveType" : "tank",
                "intake" : intakePos
            })

        }
        else if(event.shiftKey){
            if(event.key.toLowerCase() == "w" ) {
                ySpeed = 100;
                direction = "posDirection";
                console.log('w pressed full');
            }
            else if(event.key.toLowerCase() == "s") {
                ySpeed = 100;
                direction = "negDirection";
                console.log('s pressed full');
            }

            if(event.key.toLowerCase() == "a") {
                xSpeed = 100;
                direction = "negDirection";
                console.log('a pressed full');
            }
            else if(event.key.toLowerCase() == "d") {
                xSpeed = 100;
                direction = "posDirection";
                console.log('d pressed full');
            }
            else if(event.key.toLowerCase() == "i") {
                intakePos = "spinInward";
                console.log('intake was pressed');
            }
            else if(event.key.toLowerCase() == "o") {
                intakePos = "spinOutward";
                console.log('spit was pressed');
            }
        }
    });
    document.addEventListener('keyup', (event) => {
        if(event.key.toLowerCase() == "i") {
            intakePos = "noSpin";
            console.log('intake was lifted');
        }
        else if(event.key.toLowerCase() == "o") {
            intakePos = "noSpin";
            console.log('spit was lifted');
        }
        sendToBot({
            "xJoystickPos" : xSpeed,
            "yJoystickPos" : ySpeed,
            "driveDirection" : direction,
            "driveType" : "tank",
            "intake" : intakePos
        })
    });
}

///shows that the button was clicked
function buttonClick(buttonId){
    switch(buttonId){
        case "intake":
            console.log("intake");
            intakePos = "spinInward"
            break;
        case "out":
            console.log("out");
            intakePos = "spinOutward"
            break;
        default:
            console.log("default");
            intakePos = "noSpin"
    }
    /// sends information to robot
    sendToBot({
        "xJoystickPos" : xSpeed,
        "yJoystickPos" : ySpeed,
        "driveDirection" : direction,
        "driveType" : "tank",
        "intake" : intakePos
    })
}
var newParent = document.getElementById('vidFrame');

const loadVideoID = setInterval(() => {
    const video = document.getElementById("bot-stream");
    if(video) {
        
        clearInterval(loadVideoID);
        newParent.appendChild(video);
    }
}, 1000);

//adds the joystick to the page
joystick.base.id = "joystick-1";
document.getElementById("movement-controls").appendChild(joystick.base);
