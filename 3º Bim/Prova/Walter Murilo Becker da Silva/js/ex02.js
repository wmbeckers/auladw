function ex2() {

const num1 = parseInt(prompt("Insira o primeiro número: "));
const num2 = parseInt(prompt("Insira o segundo número: "));
const num3 = parseInt(prompt("Insira o terceiro número: "));
let maior;

if(num1 >= num2 && num1 >= num3) {
    maior = num1;
}
else if (num2 >= num1 && num2 >= num3) {
    maior = num2;
}
else {
    maior = num3;
}

document.getElementById("maior").innerHTML=("O maior número é: " + maior);
}