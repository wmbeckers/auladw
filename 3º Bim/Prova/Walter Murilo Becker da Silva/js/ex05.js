function ex5(){
    var n1 = parseInt(document.querySelector("#n1").value);
    var n2 = parseInt(document.querySelector("#n2").value);
    var n3 = parseInt(document.querySelector("#n3").value);
    var n4 = parseInt(document.querySelector("#n4").value);
    var n5 = parseInt(document.querySelector("#n5").value);
    var n6 = parseInt(document.querySelector("#n6").value);
    var n7 = parseInt(document.querySelector("#n7").value);
    var n8 = parseInt(document.querySelector("#n8").value);
    var n9 = parseInt(document.querySelector("#n9").value);
    var n10 = parseInt(document.querySelector("#n10").value);

    if((n1>n2)&&(n1>n3)&&(n1>n4)&&(n1>n5)&&(n1>n6)&&(n1>n7)&&(n1>n8)&&(n1>n9)&&(n1>n10)) {
        x = n1;
    }
    if((n2>n1)&&(n2>n3)&&(n2>n4)&&(n2>n5)&&(n2>n6)&&(n2>n7)&&(n2>n8)&&(n2>n9)&&(n2>n10)) {
        x = n2;
    }
    if((n3>n1)&&(n3>n2)&&(n3>n4)&&(n3>n5)&&(n3>n6)&&(n3>n7)&&(n3>n8)&&(n3>n9)&&(n3>n10)) {
        x = n3;
    }
    if((n4>n1)&&(n4>n2)&&(n4>n3)&&(n4>n5)&&(n4>n6)&&(n4>n7)&&(n4>n8)&&(n4>n9)&&(n4>n10)) {
       x = n4;
    }
    if((n5>n1)&&(n5>n2)&&(n4>n3)&&(n5>n4)&&(n5>n6)&&(n5>n7)&&(n5>n8)&&(n5>n9)&&(n5>n10)) {
       x = n5;
    }
    if((n6>n1)&&(n6>n2)&&(n6>n3)&&(n6>n4)&&(n6>n5)&&(n6>n7)&&(n6>n8)&&(n6>n9)&&(n6>n10)) {
       x = n6;
    }
    if((n7>n1)&&(n7>n2)&&(n7>n3)&&(n7>n4)&&(n7>n5)&&(n7>n6)&&(n7>n8)&&(n7>n9)&&(n7>n10)) {
       x = n7;
    }
    if((n8>n1)&&(n8>n2)&&(n3>n3)&&(n3>n4)&&(n3>n5)&&(n3>n6)&&(n3>n7)&&(n3>n9)&&(n3>n10)) {
       x = n8;
    }
    if((n9>n1)&&(n9>n2)&&(n9>n3)&&(n9>n4)&&(n9>n5)&&(n9>n6)&&(n9>n7)&&(n9>n8)&&(n9>n10)) {
       x = n9;
    }
    if((n10>n1)&&(n10>n2)&&(n10>n3)&&(n10>n4)&&(n10>n5)&&(n10>n6)&&(n10>n7)&&(n10>n8)&&(n10>n9)) {
        x = n10;
    }
    var fim = ("O maior número é: " + x);

    alert(fim);
}