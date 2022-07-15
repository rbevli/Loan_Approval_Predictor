# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle
import numpy as np
app = Flask(__name__)
api = Api(app)

def log_transform(x):
    print(x)
    return np.log(x + 1)
    
model = pickle.load(open( "modelpipe_best_xgb.pickle", "rb" ) )
class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from model.
        res = model.predict(np.array([list(json_data.values())]))
        return res.tolist() 

# assign endpoint
api.add_resource(Scoring, '/scoring')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



