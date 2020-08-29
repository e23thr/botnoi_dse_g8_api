from flask_restful import Resource
from flask import request

from helpers import predict_house_price


class HousePricePrediction(Resource):
    def get(self):
        try:
            # Get query parameter
            area = float(request.args.get('area'))
            bedrooms = float(request.args.get('bedrooms'))
            restrooms = float(request.args.get('restrooms'))
            floors = float(request.args.get('floors'))
            return {
                'expected_price': predict_house_price(area, bedrooms, restrooms, floors),
            }
        except:

            return {'message': 'Internal Error, Wrong input'}, 500
