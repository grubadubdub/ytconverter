// o=["46/111/101/97/97/46/99/99","99/99/111","97/101/97","111/101/97","97/111/97","99/101/101","99/111/101","111/99/97","99/97/97","101/97/101","111/99/101","101/97/111","111/99/111","101/111/111","99/111/99","97/99/111","97/97/101","99/111/111","111/111/97","99/97/111","97/111/101","111/101/111","101/99/101","101/101/111","111/97/99","101/101/99","111/101/99","101/111/101","101/97/97","101/111/97","101/99/99","99/101/99","99/101/111","97/101/101","99/97/101","101/111/99","111/97/101","99/99/101","111/111/101","97/97/111","97/101/99","99/99/97","111/97/97"]

// // .oeaa.cc cco aea oea aoa cee coe oca caa eae oce eao oco eoo coc aco aae coo ooa cao aoe oeo ece eeo oac eec oec eoe eaa eoa ecc cec ceo aee cae eoc oae cce ooe aao aec cca oaa

// function h(t){
// //   for (var i = 0,s="";i < t.length;i++) {
// //     var str = t[i];
//     var sp = t.split("/");
//     for(var r=0, s="";r<sp.length;r++)
//       s += String.fromCharCode(sp[r]);
//     s+=" "
// //   }
//   return s
// }

// function p(t){
// 	for(var e=0, r=0, s=""; r<t.length; r++) {
// 		if(e=t.charCodeAt(r), 64<e && e<91) 
// 			e = e == 65 ? 90 : e-1;
// 		else if (96<e && e<123)
// 			e = e == 122 ? 97 : e+1;
// 		else if(47<e && e<53)
// 			switch(e) {
// 				case 48:
// 					e=57;
// 					break;
// 				case 49:
// 					e=56;
// 					break;
// 				case 50:
// 					e=55;
// 					break;
// 				case 51:
// 					e=54;
// 					break;
// 				case 52:
// 					e=53;
// 			}
// 		else 
// 			52<e && e<58 ? e=Math.round(h(e.toString())/2).toString().charCodeAt(0):e==45&&(e=95);
// 		s+=String.fromCharCode(e)
// 	}
// 	return s
// }
// console.log(p('s3Owh5ledlo5fdO3Fh3OGwFsoFaG'))

var r = {
	'a': '',
	'b': '',
	'c': ''
}

console.log(r.a)