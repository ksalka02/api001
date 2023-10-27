from flask import Flask, json, jsonify
from flask_restful import Resource, Api, reqparse
import maindb
# import maindbhost
import pymongo
from bson import json_util

connectionString = maindb.connection_string
# connectionString = maindbhost.connection_string
client = pymongo.MongoClient(connectionString)


app = Flask(__name__)
api = Api(app)

db = client["library"]
col = db["PlayerAPI"]

# created classes for both endpoints in the api (players and moreinfo)


class players(Resource):

    def get(self):

        x = col.find()

        return {'data': json.loads(json_util.dumps(x))}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('playername', required=True,
                            type=str, location='args')
        parser.add_argument('number', required=True,
                            type=int, location='args')
        parser.add_argument('rating', required=True,
                            type=int, location='args')
        args = parser.parse_args()

        player_record = col.find_one({"playername": args['playername']})
        json_object = json.loads(json_util.dumps(player_record))

        if json_object:
            return {
                'message': f"{args['playername']} already exists"
            }, 409
        else:
            document = {"playername": args['playername'],
                        "rating": args['rating'], "number": args['number']}
            # x = col.insert_one(document)
            x = col.insert_one(document)
            x = col.find()
            return {'data': json.loads(json_util.dumps(x))}, 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('playername', required=True,
                            type=str, location='args')
        parser.add_argument('number', required=True,
                            type=int, location='args')
        parser.add_argument('rating', required=True,
                            type=int, location='args')
        parser.add_argument('newname', required=False,
                            type=str, location='args')
        args = parser.parse_args()

        player_record = col.find_one({"playername": args['playername']})
        json_object = json.loads(json_util.dumps(player_record))

        # need to check if the name exists first then update it
        if json_object and args['newname']:
            updates = {
                "$set": {"playername": args['newname'], "rating": args['rating'], "number": args['number']}
            }
            x = col.update_one({"playername": args['playername']}, updates)
            x = col.find()
            return {'data': json.loads(json_util.dumps(x))}, 200

        elif json_object:
            updates = {
                "$set": {"rating": args['rating'], "number": args['number']}
            }
            x = col.update_one({"playername": args['playername']}, updates)
            x = col.find()
            return {'data': json.loads(json_util.dumps(x))}, 200

        else:
            return {
                'message': f"{args['playername']} doesn't exists"
            }, 409

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('playername', required=True,
                            type=str, location='args')
        args = parser.parse_args()

        player_record = col.find_one({"playername": args['playername']})
        json_object = json.loads(json_util.dumps(player_record))

        if json_object:
            x = col.delete_one({"playername": args['playername']})
            x = col.find()
            return {'data': json.loads(json_util.dumps(x))}, 200
        else:
            return {
                'message': f"{args['playername']} does not exist!"
            }, 404


api.add_resource(players, '/players')
# api.add_resource(moreinfo, '/moreinfo')

# port = os.environ["ENV"]¸


if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True, port=port)
    app.run(host='0.0.0.0', debug=True, port=5000)


# if __name__ == "__main__":
#     if os.environ["ENV"] == "5000":
#         app.run(host='0.0.0.0', debug=True, port=5000)
#     elif os.environ["ENV"] == "3000":
#         app.run(host='0.0.0.0', debug=True, port=3000)
