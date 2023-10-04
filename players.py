from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os

app = Flask(__name__)
api = Api(app)

# created classes for both endpoints in the api (players and moreinfo)

players_path = 'players.csv'


class players(Resource):
    def get(self):
        data = pd.read_csv(players_path)
        data = data.to_dict()
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('playerNumber', required=True,
                            type=int, location='args')
        parser.add_argument('name', required=True,
                            type=str, location='args')
        parser.add_argument('rating', required=True,
                            type=int, location='args')
        args = parser.parse_args()

        data = pd.read_csv(players_path)

        if args['name'] in data['name'].tolist():
            return {
                'message': f"{args['name']} already exists"
            }, 409
        else:
            temp_df = pd.DataFrame([[args['playerNumber'], args['name'], args['rating']]], columns=[
                                   'playerNumber', 'name',  'rating'])

            new_df = pd.concat([data, temp_df], ignore_index=True)

            new_df.to_csv(players_path, index=False)
            return {'data': new_df.to_dict()}, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True,
                            type=str, location='args')
        args = parser.parse_args()

        data = pd.read_csv(players_path)

        if args['name'] in data['name'].tolist():
            data = data[data['name'] != str(args['name'])]
            data.to_csv(players_path, index=False)
            return {'data': data.to_dict()}, 200
        else:
            return {
                'message': f"{args['name']} does not exist!"

            }, 404


# moreinfo_path = 'moreinfo.csv'


# class moreinfo(Resource):
#     def get(self):
#         data = pd.read_csv(moreinfo_path)
#         data = data.to_dict()
#         return {'data': data}, 200

#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('playerId', required=True,
#                             type=str, location='args')
#         parser.add_argument('skillmoves', required=True,
#                             type=int, location='args')
#         parser.add_argument('weakfoot', required=True,
#                             type=int, location='args')
#         parser.add_argument('workrates', required=True,
#                             type=str, location='args')
#         parser.add_argument('links', required=True, type=str, location='args')
#         args = parser.parse_args()

#         data = pd.read_csv(moreinfo_path)

#         if args['playerId'] in data['playerId'].tolist():
#             return {
#                 'message': f"{args['playerId']} already exists"
#             }, 409
#         else:
#             temp_df = pd.DataFrame([[args['playerId'], args['skillmoves'], args['weakfoot'], args['workrates'], args['links']]], columns=[
#                                    'playerId', 'skillmoves',  'weakfoot', 'workrates', 'links'])

#             new_df = pd.concat([data, temp_df], ignore_index=True)

#             new_df.to_csv(moreinfo_path, index=False)
#             return {'data': new_df.to_dict()}, 200

#     def delete(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('playerId', required=True,
#                             type=str, location='args')
#         args = parser.parse_args()

#         data = pd.read_csv(moreinfo_path)

#         if args['playerId'] in data['playerId'].tolist():
#             data = data[data['playerId'] != str(args['playerId'])]
#             data.to_csv(moreinfo_path, index=False)
#             return {'data': data.to_dict()}, 200
#         else:
#             return {
#                 'message': f"{args['playerId']} does not exist!"

#             }, 404


api.add_resource(players, '/players')
# api.add_resource(moreinfo, '/moreinfo')

if __name__ == "__main__":
    if os.environ["ENV"] == 5000:
        app.run(host='0.0.0.0', debug=True, port=5000)
    elif os.environ["ENV"] == 3000:
        app.run(host='0.0.0.0', debug=True, port=3000)
