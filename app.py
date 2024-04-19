from flask import Flask, request, render_template, jsonify
# Alternatively can use Django, FastAPI, or anything similar
from src.pipelines.pred_pipeline import CustomData, PredictPipeline

application = Flask(__name__, static_folder='templates')
app = application

@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/predict', methods = ['POST', "GET"])

def predict_datapoint(): 
    if request.method == "GET": 
        return render_template("form.html")
    else: 
        data = CustomData(
            assists = int(request.form.get('assists')),
            boosts = int(request.form.get('boosts')),
            damageDealt= float(request.form.get("damageDealt")), 
            DBNOs= int(request.form.get("DBNOs")), 
            headshotKills= int(request.form.get("headshotKills")),
            heals = int(request.form.get("heals")),
            killPlace = int(request.form.get("killPlace")),
            killPoints = int(request.form.get("killPoints")),
            kills = int(request.form.get("kills")),
            killStreaks = int(request.form.get("killStreaks")),
            longestKill= float(request.form.get("longestKill")), 
            matchDuration = int(request.form.get("matchDuration")),
            matchType = request.form.get("matchType"),
            maxPlace = int(request.form.get("maxPlace")),
            numGroups= int(request.form.get("numGroups")),
            rankPoints= int(request.form.get("rankPoints")),
            revives= int(request.form.get("revives")),
            rideDistance= float(request.form.get("rideDistance")),
            swimDistance = float(request.form.get("swimDistance")),
            walkDistance = float(request.form.get("walkDistance")),
            weaponsAcquired= int(request.form.get("weaponsAcquired")),
            winPoints= int(request.form.get("winPoints"))
        )
    new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = round(pred[0],2)

    return render_template("results.html", final_result = results)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", debug= True)
#http://127.0.0.1:5000/ in browser