from sklearn import tree 
import pandas as pd 
import sklearn.tree import DecisionTreeClassifier

music_data= pd.read_csv("music.csv")
inputs= music_data.drop(columns=['genre'])
outputs= music_data['ge']

model = DecisionTreeClassifier()

model.fit(inputs, outputs)

tree.export_graphviz(model, 
out_file="music_model.dot",
feature_names= ['age','gender'],
class_names=sorted(y.unique()),
labels="all",
rounded = True
)