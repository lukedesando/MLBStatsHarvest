import pandas as pd
from matplotlib import pyplot
from pandas.core.frame import DataFrame
from pandas.plotting import scatter_matrix
import seaborn as sns

TestFile = "Statcast Batter Stats.csv"

#Select Important Data
ColumnNames = ['release_pos_x','release_pos_z','estimated_ba_using_speedangle','pfx_x','pfx_z','plate_x','plate_z','vx0','vy0','vz0','ax','ay','az','launch_angle','effective_speed','pitch_type']
DataSet = pd.read_csv(TestFile,usecols=ColumnNames)

#DataSet = DataSet['release_pos_x','release_pos_z']
#print(DataSet)

#print (DataSet.describe())

# DataSet.plot(kind='box', subplots=True, sharex = False, sharey = False)
# pyplot.show()

# # histograms
# DataSet.hist()
# pyplot.show()

# # scatter plot matrix
# scatter_matrix(DataSet)
# pyplot.show()

DataSet.plot(kind='scatter',x=DataSet('ax'),y=DataSet('ay'))