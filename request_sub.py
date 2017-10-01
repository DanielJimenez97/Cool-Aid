from django.http import HttpResponse

def requestSub(request):
	output = '''
		<html>
		<head>
			<link rel="stylesheet" href="request.css" style="text/css">
			<title>Cool-Aid</title>
		</head>
		<body style="background-color: gray;">
			<div id="container">
				<img style="float: left" src="Cool-Aid.png" height=150px width=150px >
				<div id="header">
					<h1 style="text-color: white">Request Submitted</h1>
				</div>
			</div>
			</br>
		
			<div id="p">
			<p>Check out these Volunteering</br>
			Opportunities near you</p>
		
			<div id="info">
				<p>Volunteer One</br>
				....................</br>
				.....................</br>
				Volunteer Two</br>
				...............</br>
				....................</br>
				Volunteer Three</br>
				.....................</p>
			</div>
			</div>
		
			<div id="map">
				<img src="googleMap.png" height=400px width=800px >
			</div>
			
			<div id="input">
				<p>Change Locations</p>
				<form>
					Address: <input type="text">
					Town: <input type="text">
					ZipCode: <input type="text">
				</form>
			</div>
		</body>
		</html>'''
	return HttpResponse(output)