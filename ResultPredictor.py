import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

class ResultPredictor():
    
    def __init__(self,data_file_path):
        self.data_main = pd.read_csv(data_file_path)
        print("Data loaded with shape",self.data_main.shape)
        
    def predict_result(self,model_ix,model_param,params):
        y = self.data_main['Attrition'].copy()
        X = self.data_main.loc[:, self.data_main.columns != 'Attrition'].copy()
        empty_columns = []
        final_params = {}
        for key in params:
            if params[key] is None:
                empty_columns.append(key)
            else:
                final_params[key] = params[key]
        X.drop(empty_columns,axis=1,inplace = True)
        input_df = pd.DataFrame([final_params])
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = None
        if model_ix == 1:
            model = LogisticRegression(fit_intercept = False, C = float(model_param))
        elif model_ix == 2:
            model = SVC(C = float(model_param))
        elif model_ix == 3:
            model = RandomForestClassifier(n_estimators=int(model_param), criterion ='entropy', random_state=0)
        else:
            model = KNeighborsClassifier(n_neighbors=int(model_param))
        
        return_data = {}
        model.fit(x_train,y_train)
        return_data['accuracy'] = accuracy_score(y_test, model.predict(x_test))
        return_data['prediction'] = 'Yes' if model.predict(input_df)[0] == 1 else 'No' 
        if model_ix == 3:
            importance_arr = model.feature_importances_
        else:
            rf = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
            rf.fit(x_train,y_train)
            importance_arr = rf.feature_importances_
        importances = pd.DataFrame({'feature':X.columns,'importance':np.round(importance_arr,3)})
        importances = importances.sort_values('importance',ascending=False).set_index('feature')
        return_data['feature_importance'] = importances.to_dict('index')
        return return_data
            
                
        
    
    