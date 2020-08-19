//const date1 = new Date();
//document.querySelector('.year').innerHTML = date1.getFullYear();

function initMap(){
	//Your location
	const loc = { lat: 25.7574, lng: -80.3733 };
	//centered map on location
	const map = new google.maps.Map(document.querySelector('.map')
		,{
			zoom:14,
			center: loc
		});
	//marker positioned at location
	const marker = new google.maps.Marker({position: loc, map:
		map });
}