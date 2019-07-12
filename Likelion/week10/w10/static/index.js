function signup() {
    var id = document.getElementById("id").value;
    var pw = document.getElementById("pw").value;
    var pwr = document.getElementById("pwr").value;
    var id_check = /^[A-Za-z]+[A-za-z0-9]{7,19}$/g;
    var pw_check = /^[A-Za-z0-9]{8,20}$/g;

    if(id==""){
        alert("id를 입력해 주세요.");
        return true;
    }
    if(pw==""){
        alert("pw를 입력해 주세요.");
        return true;
    }
    if(pwr==""){
        alert("pwr를 입력해 주세요.");
        return true;
    }


    if(id_check.test(id)==false){
        alert("id 형식을 맞춰주세요.");
        return true;
    }

    if(pw_check.test(pw)==false){
        alert("password 형식을 맞춰주세요.");
        return true;
    }

    if(pw != pwr){
        alert("password와 동일하게 입력하세요")
        return true;
    }


    alert("회원가입성공");
}