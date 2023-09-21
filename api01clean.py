from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

# created classes for both endpoints in the api (users and locations)

players_path = '/Users/ksalka/Desktop/api001/players.csv'


class players(Resource):
    def get(self):
        data = pd.read_csv(players_path)
        data = data.to_dict()
        return {'data': data}, 200

    # def post(self):


moreinfo_path = '/Users/ksalka/Desktop/api001/moreinfo.csv'


class moreinfo(Resource):
    def get(self):
        data = pd.read_csv(moreinfo_path)
        data = data.to_dict()
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('playerId', required=True,
                            type=str, location='args')
        parser.add_argument('skillmoves', required=True,
                            type=int, location='args')
        parser.add_argument('weakfoot', required=True,
                            type=int, location='args')
        parser.add_argument('workrates', required=True,
                            type=str, location='args')
        parser.add_argument('links', required=True, type=str, location='args')
        args = parser.parse_args()
        # return {
        #     'playerId': args['playerId'],
        #     'skillmoves': args['skillmoves'],
        #     'weakfoot': args['weakfoot'],
        #     'workrates': args['workrates'],
        #     'links': args['links']
        # }, 200

        data = pd.read_csv(moreinfo_path)

        if args['playerId'] in data['playerId'].tolist():
            return {
                'message': f"{args['playerId']} already exists"
            }, 409
        else:
            # print("Args:")
            # print(args['playerId'])
            # print("Data:")
            # print(data['playerId'])
            # print(args['playerId'] in data['playerId'].tolist())
            # ===============================
            # ===============================
            temp_df = pd.DataFrame([[args['playerId'], args['skillmoves'], args['weakfoot'], args['workrates'], args['links']]], columns=[
                'playerId',  'skillmoves',  'weakfoot', 'workrates', 'links'])

            # new_df = pd.concat([data, temp_df], ignore_index=True)
            new_df = pd.concat([data, temp_df], ignore_index=True)
            # print('**********************')
            # print(new_df)

            # new_df.to_csv(moreinfo_path, index=False)
            # return {'data': new_df.to_dict()}, 200
            new_df.to_csv(moreinfo_path, index=False)
            return {'data': new_df.to_dict()}, 200
        # return {'data': 'hello'}, 200
        # ===============================
        # ===============================

        # else:
        #     temp_df = pd.DataFrame([[args['playerId'], args['skillmoves'], args['weakfoot'], args['workrates']]], columns=[
        #                            'playerId',  'skillmoves',  'weakfoot', 'workrates', 'links'])

        #     new_df = pd.concat([data, temp_df])
        #     print(new_df)
        #     # data = data.concat({
        #     #     'playerId': args['playerId'],
        #     #     'skillmoves': args['skillmoves'],
        #     #     'weakfoot': args['weakfoot'],
        #     #     'workrates': args['workrates'],
        #     #     'links': [],
        #     # }, ignore_index=True)
        #     # data.to_csv(moreinfo_path, index=False)
        #     return {'data': data.to_dict()}, 200


# http://127.0.0.1:5000/moreinfo?skill=5&weak=5&work=M/M&link="['Morocco', 'laliga', 'real']"
# This is to map the classes in the url of the api (ex: api.com/users or api.com/locations)
api.add_resource(players, '/players')
api.add_resource(moreinfo, '/moreinfo')

if __name__ == "__main__":
    app.run(debug=True)
