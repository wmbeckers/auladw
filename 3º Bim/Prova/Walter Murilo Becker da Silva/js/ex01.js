function votos() {
var e;
var eleitores=prompt ("Quantos eleitores há no município?");
	if (eleitores!=null) {
		e = ("O município possui " + eleitores + " eleitores!");
	
	var vb;
	var branco=prompt ("Quantos dos votos foram brancos?")
		if (branco<=eleitores){
			vb = (branco + " votos foram brancos!")
		}
		else {
			vb = ("O número de votos brancos não pode ser maior do que o número de eleitores!")
		}

	var vn;
	var nulo=prompt ("Quantos dos votos foram nulos?")
		if (nulo<=eleitores) {
			vn = (nulo + " votos foram nulos!")
		}	
		else {
			vn = ("O número de votos nulos não pode ser maior do que o número de eleitores!")
		}

	var vv;
	var valido = (eleitores - branco) - nulo;
		vv = ("O número de votos válidos foi de: " + valido + "!")


	var p100b;
	var	porcentagemb = (100 * branco) / eleitores;
		p100b = ("Os votos brancos representam " + porcentagemb + "% dos votos!")

	var p100n;
	var	porcentagemn = (100 * nulo) / eleitores;
		p100n = ("Os votos nulos representam " + porcentagemn + "% dos votos!")

	var p100v;
	var	porcentagemv = (100 * valido) / eleitores;
		p100v = ("Os votos válidos representam " + porcentagemv + "% dos votos!")

		document.getElementById("total").innerHTML=e;
		document.getElementById("votobranco").innerHTML=vb;
		document.getElementById("votonulo").innerHTML=vn;
		document.getElementById("votovalido").innerHTML=vv;
		document.getElementById("p100branco").innerHTML=p100b;
		document.getElementById("p100nulo").innerHTML=p100n;
		document.getElementById("p100valido").innerHTML=p100v;

	}	
}	
