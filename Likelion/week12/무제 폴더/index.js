var numberClicked = false;
var mul = false;
var multi = false;


function add(char) {
    var display = document.getElementById('display');
    if(numberClicked == false) {
        if (isNaN(char)) {

        }
        else {
            display.value += char;
        }
    }
    else {
        display.value += char;
    }


    if(isNaN(char) == true) {
        numberClicked = false;
    }
    else {
        numberClicked = true;
    }

}

function calculate() {
    var display = document.getElementById('display');
    var result = eval(display.value);
    document.getElementById('result').value = result;
}

function remove() {
    document.getElementById('display').value = "";
    document.getElementById('result').value = "";
    mul = false;
    multi = false;
}