import hiplot as hip
def fetch_my_experiment():
    fifa = pd.read_csv('fifa19_data.csv',index_col='Unnamed: 0')

    return hip.Experiment.from_dataframe(fifa[['Age','Nationality','Value','Height', 'Weight', 'Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',]]).display()