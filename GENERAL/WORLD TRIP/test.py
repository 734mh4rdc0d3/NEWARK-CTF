from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test_app")
location = geolocator.reverse("38.05986232308507, 15.8432894525962")
print(location.raw['display_name'])