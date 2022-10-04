function ex6(){
    var age01 = parseInt(prompt("Insira a idade da primeira pessoa: "));
    var age02 = parseInt(prompt("Insira a idade da segunda pessoa: "));
    var age03 = parseInt(prompt("Insira a idade da terceira pessoa: "));
    var age04 = parseInt(prompt("Insira a idade da quarta pessoa: "));
    var age05 = parseInt(prompt("Insira a idade da quinta pessoa: "));
    var age06 = parseInt(prompt("Insira a idade da sexta pessoa: "));
    var age07 = parseInt(prompt("Insira a idade da sétima pessoa: "));
    var age08 = parseInt(prompt("Insira a idade da oitava pessoa: "));
    var age09 = parseInt(prompt("Insira a idade da nona pessoa: "));
    var age10 = parseInt(prompt("Insira a idade da décima pessoa: "));

    x = 0;
    y = 0;

    if(age01>=18){ x++
    } else { y++
    }
    if(age02>=18){ x++
    } else { y++
    }
    if(age03>=18){ x++
    } else { y++
    }
    if(age04>=18){ x++
    } else { y++
    }
    if(age05>=18){ x++
    } else { y++
    }
    if(age06>=18){ x++
    } else { y++
    }    
    if (age07>=18){ x++
    } else { y++
    }
    if(age08>=18){ x++
    } else { y++
    }    
    if(age09>=18){ x++
    } else { y++
    }    
    if(age10>=18){ x++
    } else { y++
    }

    document.getElementById("idade").innerHTML=( "Temos " + x + " maiores de idade e " + y + " menores de idade!")
}