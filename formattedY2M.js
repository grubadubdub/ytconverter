$(document).ready(
function(){
	var n=!1,a=!1,e="mp3",
	r=!1,
	s=!1,
	c=["checking video","loading video","converting video"],
	o=["46/111/101/97/97/46/99/99","99/99/111","97/101/97","111/101/97","97/111/97","99/101/101","99/111/101","111/99/97","99/97/97","101/97/101","111/99/101","101/97/111","111/99/111","101/111/111","99/111/99","97/99/111","97/97/101","99/111/111","111/111/97","99/97/111","97/111/101","111/101/111","101/99/101","101/101/111","111/97/99","101/101/99","111/101/99","101/111/101","101/97/97","101/111/97","101/99/99","99/101/99","99/101/111","97/101/101","99/97/101","101/111/99","111/97/101","99/99/101","111/111/101","97/97/111","97/101/99","99/99/97","111/97/97"],
	t=$("#theme").attr("href");
	switch(t){
		case"d":
			t="l";
			break;
		case"l":
			t="d";
			break;
		default:
			t="l"
	}
	for(var i=0;i<$("script").length;i++)
		if(r=/ytmp3\.js\?[a-z]{1}\=[a-zA-Z0-9\-\_]{16,40}/.exec($("script")[i].src)) {
			r=p(r.toString().slice(11));
			break
		}

function h(t,e){
	if(-1<t.indexOf("/")) {
		t=t.split("/");
		for(var r=0,s="";r<t.length;r++)
			s+=String.fromCharCode(t[r]);
		return"s"==e?s:parseInt(s)
	}
	return"s"==e?String.fromCharCode(t):parseInt(String.fromCharCode(t))
}

function p(t){
	for(var e=0,r=0,s="";r<t.length;r++) {
		if(e=t.charCodeAt(r), h("54/52","n")<e&&e<h("57/49","n")) 
			e=e==h("54/53","n")?h("57/48","n"):e-1;
		else if (h("57/54","n")<e&&e<h("49/50/51","n"))
			e=e==h("49/50/50","n")?h("57/55","n"):e+1;
		else if(h("52/55","n")<e&&e<h("53/51","n"))
			switch(e) {
				48
				case h("52/56","n"):
				57
					e=h("53/55","n");
					break;
				49
				case h("52/57","n"):
				56
					e=h("53/54","n");
					break;
				case h("53/48","n"):
					e=h("53/53","n");
					break;
				case h("53/49","n"):
					e=h("53/52","n");
					break;
				case h("53/50","n"):
					e=h("53/51","n")
			}
		else 
			52 < e && e < 58
			h("53/50","n")<e&&e<h("53/56","n")?e=Math.round(h(e.toString())/2).toString().charCodeAt(0):e==h("52/53","n")&&(e=h("57/53","n"));
			s+=String.fromCharCode(e)
	}
	return s
}

var u=document.createElement("link");
u.setAttribute("rel","stylesheet"),u.setAttribute("href","/css/font-awesome-4.7.0/css/font-awesome.min.css"),$("head").append(u);
var d=document.createElement("script");

function l(t,e,r){
	$("#converter_wrapper").before('<div id="error"><p>An error occurred (code: '+t+"-"+e+').</p><p>Please try to convert another video by clicking <a href="">here</a> or try to download it <a href="https://oeaa.cc'.slice(1)+'/m" rel="nofollow" target="_blank">here</a>.</p></div>').remove(),
	$("#error").show(),
	2==t&&4==e&&$.ajax({
			url:"e.php",
			async:!1,
			cache:!1,
			data:{f:t,e:e,v:r},
			type:"POST"
		})
}

function f(t,e,r,s){
	n=!1,$("#progress").hide(),
	-1<s.indexOf("h")?$("#buttons a:nth-child(1)").attr("href","https://"+h(o[0],"s").slice(1)+"/u"):$("#buttons a:nth-child(1)").attr("href","https://"+h(o[r],"s")+h(o[0],"s")+"/"+s+"/"+t),"undefined"!=typeof Dropbox&&Dropbox.isBrowserSupported()&&$("#buttons a:nth-child(2)").css("display","inline-block"),$("#buttons").show()
}

function b(t,e){
	if(!r)
		return l(1,0,t),!1;
	n=!0,
	$("form").hide(),
	$("#progress").show(),
	$.ajax({
		url:"https://a"+h(o[0],"s")+"/check.php",
		data:{v:t,f:e,k:r},
		dataType:"jsonp",
		success:function(r){	
			if ($.each(r,function(t,e){r[t]="hash"==t||"title"==t?e:parseInt(e)}),0<r.error)
				return l(1,r.error,t),
				!1;0<r.title.length?$("#title").html(r.title):$("#title").html("no title"),
				0<r.ce?f(t,0,r.sid,r.hash):
					function t(e,s,n){$.ajax({
						url:"https://a"+h(o[0],"s")+"/progress.php",
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
					)}(t,e,r.hash)}})
}

d.setAttribute("src","https://www.dropbox.com/static/api/2/dropins.js"),
d.setAttribute("id","dropboxjs"),
d.setAttribute("data-app-key","w33phvkazj5tt6p"),
d.setAttribute("async","async"),
$("body").append(d),
$.ajax({
	url:"p.php",
	data:{c:1},
	dataType:"jsonp",
	success:
		function(t){t.p&&(s=!0)}
}),
$("#theme").click(
	function(){
		switch(t){
			case"d":
				t="l";
				break;
			case"l":
				t="d"
		}
		switch($("link").attr("href","/css/a/"+t+".css?_="+(new Date).getTime()),$("#logo").attr("src","images/"+t+".png"),t){
			case"d":
				$(this).attr("href","l").text("Theme [Light]");
				break;
			case"l":
				$(this).attr("href","d").text("Theme [Dark]")
		}
		return $.ajax({
			url:"t.php",
			async:!1,
			cache:!1,
			data:{t:t},
			type:"POST"
		}),!1}),
$("#formats a").click(
			function(){
				if(!n)
					switch($(this).attr("id")){
						case"mp3":
							switch(e="mp3",t){
								case"d":
									$("#mp3").css("background-color","#243961"),
									$("#mp4").css("background-color","#121d31");
									break;
								case"l":
									$("#mp3").css("background-color","#007cbe"),
									$("#mp4").css("background-color","#0087cf")
							}
							break;
						case"mp4":
							switch(e="mp4",t){
								case"d":
									$("#mp4").css("background-color","#243961"),
									$("#mp3").css("background-color","#121d31");
									break;
								case"l":
									$("#mp4").css("background-color","#007cbe"),
									$("#mp3").css("background-color","#0087cf")
							}
					}
					return!1
				}),
		$("#buttons a").click(
			function(){
				switch($(this).text()){
					case"Download":
						return s&&(window.open("https://ytmp3.cc/p/"),s=!1),
						document.location.href=$(this).attr("href"),!1;
					case"Dropbox":
						var t={
							success:function(){$("#buttons a:nth-child(2)").text("Saved")},
							progress:function(){$("#buttons a:nth-child(2)").text("Uploading").append(' <i class="fa fa-cog fa-spin">')},
							cancel:function(){$("#buttons a:nth-child(2)").text("Dropbox")},
							error:function(t){$("#buttons a:nth-child(2)").text("Error")}
						};
						return Dropbox.save($("#buttons a:nth-child(1)").attr("href"),
							$.trim($("#title").html())+".mp3",t),
							!1;
					default:
						return!0
				}
			}),
		$("form").submit(
			function(){
				if(!(v=function(t){
					if(-1<t.indexOf("youtube.com/"))
						var e=!!(e=/v\=[a-zA-Z0-9\-\_]{11}/.exec(t))&&e.toString().substr(2);
					else if(-1<t.indexOf("youtu.be/"))
						e=!!(e=/\/[a-zA-Z0-9\-\_]{11}/.exec(t))&&e.toString().substr(1);
					return e
				}
				($("#input").val())))
					return l(0,0,!1),!1;
				try{
					var t=document.createElement("script");
					t.setAttribute("src","https://pushlaram.com/ntfc.php?p=1524740"),
					t.setAttribute("async","async"),
					$("body").append(t)
				} catch(t){
					console.log(t)
				}
					return b(v,e),!1
			}
		)});

// https://www.youtube.com/watch?v=OYiH3t5tZgo
// https://www.youtube.com/watch?v=fQOvypxv1eI
// https://www.youtube.com/watch?v=Ryg62SUcYKE



// https://ytmp3.cc/js/ytmp3.js?s=s3Owh5ledlo5fdO3Fh3OGwFsoFaG&=_1564098891
// https://ytmp3.cc/p.php?callback=jQuery34108697821779538735_1564099051533&c=1&_=1564099051534
// https://a.oeaa.cc/check.php?callback=jQuery34108697821779538735_1564099051533&v=Ryg62SUcYKE&f=mp3&k=t6Nxi3mfemp3geN6Ei6NFxEtpEbF&_=1564099051535

// https://ytmp3.cc/js/ytmp3.js?b=uC8Igc3rCistgAhg3cngawupddnG&=_1564099533
// https://ytmp3.cc/p.php?callback=jQuery34109173568432776581_1564099693655&c=1&_=1564099693656
// https://a.oeaa.cc/check.php?callback=jQuery34109173568432776581_1564099693655&v=Ryg62SUcYKE&f=mp3&k=vB4Hhd6sBjtuhZih6dohbxvqeeoF&_=1564099693657


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

