var r = [],
		youtube = 'Ryg62SUcYKE',
		res = {
			'sid' : '',
		  'hash' : '',
			'title' : ''
		};

for (var i=0;i<r.length;i++) {
	$.ajax({
	url:"https://a.oeaa.cc/check.php",
	data:{v:youtube,f:'mp3',k:r},
	dataType:"jsonp",
	success: arguments[0]
});
}