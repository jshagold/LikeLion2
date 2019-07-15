var answerNumber = Math.floor(Math.random() * 100) + 1;
var guessHistory = document.querySelector('.guessHistory');
var yesOrNo = document.querySelector('.yesOrNo');
var highOrLow = document.querySelector('.highOrLow');
var guessButton = document.querySelector('.guessButton');
var guessForm = document.querySelector('.guessForm');
var guessCount = 1;





function checkYourNumber() {
    var userGuess = Number(guessForm.value);

    if(guessCount === 1) {
        guessHistory.textContent = '입력한 숫자들 : ';
    }


    if(userGuess === answerNumber) {
        guessHistory.textContent += userGuess + ' ';

        yesOrNo.textContent = '축! 정답!';
        yesOrNo.style.backgroundColor = 'green';
        highOrLow.textContent = '';
        setGameOver();
    }
    else if(guessCount === 10) {
        guessHistory.textContent += userGuess + ' ';

        yesOrNo.textContent = 'Game OVer';
        highOrLow.textContent = '';
        setGameOver();
    }
    else if(isNaN(userGuess) == true) {
        yesOrNo.textContent = '숫자를 입력해 주세요';
        yesOrNo.style.backgroundColor = 'red';
        highOrLow.textContent = '';
        guessForm.value = '';
        return;
    }
    else if(userGuess > 100 || userGuess < 1) {
        yesOrNo.textContent = '1부터 100사이의 숫자를 입력해 주세요'
        yesOrNo.style.backgroundColor = 'red';
        highOrLow.textContent = '';
        guessForm.value = '';
        return;
    }
    else {
        guessHistory.textContent += userGuess + ' ';

        yesOrNo.textContent = '오답!';
        yesOrNo.style.backgroundColor = 'red';
        if(userGuess < answerNumber){
            highOrLow.textContent = '정답은 더큼';
        }
        else if(userGuess > answerNumber) {
            highOrLow.textContent = '정답은 더작음';
        }
    }

    guessCount++;
    guessForm.value = '';
}



guessButton.addEventListener('click', checkYourNumber);

var restartButton;

function setGameOver() {
    guessForm.disabled = true;
    guessButton.disabled = true;
    restartButton = document.createElement('button');
    restartButton.textContent = '새 게임 시작하기';
    document.body.appendChild(restartButton);
    restartButton.addEventListener('click', restartGame);
}

function restartGame() {
    guessCount = 1;
    var resetParas = document.querySelectorAll('.resultDiv p');
    for(var i=0;i<resetParas.length;i++) {
        resetParas[i].textContent = '';
    }

    restartButton.parentNode.removeChild(restartButton);
    guessButton.disabled = false;
    guessForm.disabled = false;
    guessForm.value = '';
    guessForm.focus();
    yesOrNo.style.backgroundColor = 'white';
    answerNumber = Math.floor(Math.random() * 100) + 1;
}

