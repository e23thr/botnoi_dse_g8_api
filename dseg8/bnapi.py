from flask_restful import Resource
from flask import request

import requests

TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTk0MDA4MzUsImlkIjoiMWRkNzIzOTktNDBkNy00Yjk1LWJjNDYtYTI3NGE2Y2NjNjNkIiwiaXNzIjoiVU5BSk5uUkU0aXhYQjRQWXo0Y0gxRGFrTHkyTGVMM3giLCJuYW1lIjoi8J-HufCfh60gUHJhcGhhbiDwn4e58J-HrSIsInBpYyI6Imh0dHBzOi8vcHJvZmlsZS5saW5lLXNjZG4ubmV0LzBoUS1DcHc3MzREZ0otQ1NKamkwSnhWVUpNQUc4Skp3aEtCbTFJWVF4YVZ6VlRhUnNFU20wVlpWc0FXVElCTzBFRVJHa1NaVk5kVVdkVCJ9.oxj1Y1_IW-7srG7WlQuUJBTLorYLliDgDpQnWycaKgc'

apiHeaders = {
    "Authorization": "Bearer "+TOKEN
}


class PredictCondoPrice(Resource):
    def get(self):
        try:
            # Get query parameter
            area = float(request.args.get('area'))
            bedrooms = float(request.args.get('bedrooms'))
            restrooms = float(request.args.get('restrooms'))
            floors = float(request.args.get('floors'))
            response = requests.get(
                "https://openapi.botnoi.ai/service-api/DSE-G8-P2?area={}&bedrooms={}&restrooms={}&floors={}".format(area, bedrooms, restrooms, floors), headers=apiHeaders)
            return response.json()
        except:

            return {'message': 'Internal Error, Wrong input'}, 500
