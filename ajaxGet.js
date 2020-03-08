var r = 'heu6q64eh6pf4moiBELtxuoqvvtZ'
$.ajax({
		url:"https://a.oeaa.cc/check.php",
		data:{v:'fQOvypxv1eI',f:'mp3',k:r},dataType:"jsonp",
		success:function(r){	
			console.log(r);
			if ($.each(r,function(t,e){
			   r[t]= "hash"==t||"title"==t ? e : parseInt(e)
			}),
					0<r.error)
				return l(1,r.error,t),
				!1;0<r.title.length?$("#title").html(r.title):$("#title").html("no title"),
				0<r.ce?f(t,0,r.sid,r.hash):
					function t(e,s,n){
					$.ajax({
						url:"https://a.oeaa.cc/progress.php",
						data:{id:n},dataType:"jsonp",
						success:function(r){
							if($.each(r,function(t,e){r[t]="hash"==t?e:parseInt(e)}),0<r.error)
								return l(2,r.error,e),!1;
							switch(r.progress){
								case 0:
								case 1:
								case 2:
									$("#progress span").html(c[r.progress]);
									break;
								case 3:
									a=!0,f(e,0,r.sid,n)
							}
							a||window.setTimeout(function(){t(e,s,n)},3e3)
						}
					}
					)}(t,e,r.hash)
		}
})


// callback=jQuery34107031663270877886_1564100623880
// v=Ryg62SUcYKE
// f=mp3
// k=heu6q64eh6pf4moiBELtxuoqvvtZ
// _=1564100623882

// Host: a.oeaa.cc
// User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
// Accept: */*
// Accept-Language: en-US,en;q=0.5
// Accept-Encoding: gzip, deflate, br
// Connection: keep-alive
// Referer: https://ytmp3.cc/