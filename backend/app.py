from flask import Flask, request
from flask_cors import CORS

from location import Location
from power import power

api = Flask(__name__)
CORS(api)

@api.route('/locationlocationlocation')
def locationlocationlocation():
    latitude = float(request.args.get('lat'))
    longitude = float(request.args.get('lng'))
    radius = float(request.args.get('rad'))

    power_report = power(Location(latitude, longitude, radius))
    print(power_report.get_corn_power())
    print(type(power_report.get_corn_power()))

    response = {
        'solar': power_report.get_solar_power(),
        'wind': power_report.get_wind_power(),
        'nuclear': power_report.get_nuclear_power(),
        'corn': power_report.get_corn_power(),
    }

    return response
