import hiplot as hip
import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def fifa_experiment():
    fifa = pd.read_csv('fifa19_data.csv',index_col='Unnamed: 0')
    fifa_hiplot = hip.Experiment.from_dataframe(fifa[['Age','Nationality','Value','Height', 'Weight', 'Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',]])
       
    return fifa_hiplot.to_html()

if __name__ == "__main__":
    app.run()