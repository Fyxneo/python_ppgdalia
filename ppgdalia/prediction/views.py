from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from prediction.serializers import ActivitySerializer
from django.shortcuts import render
import joblib
import numpy as np

@csrf_exempt
def predict(request):
    if request.method == 'GET':
        return(JsonResponse(serializer.errors, status=400))

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)
        
        if serializer.is_valid():
            data["Activities"] = predict_activities(data)
            serializer = ActivitySerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return(JsonResponse(serializer.data,status=201))
            
        return(JsonResponse(serializer.errors, status=400))

def predict_activities(unscaled_data):

    colonnes = ['BVP', 'wrist_ACC_X', 'wrist_ACC_Y', 'wrist_ACC_Z', 'EDA',
       'chest_ACC_X', 'chest_ACC_Y', 'chest_ACC_Z', 'chest_ECG', 'chest_EMG',
       'chest_EDA', 'chest_Temp', 'chest_Resp', 'rpeaks', 'WEIGHT', 'AGE',
       'HEIGHT', 'SKIN', 'SPORT', 'f', 'm']
	   
    path_to_model = './prediction/RF_clf.pkl'
    unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    unscaled_data = np.array(unscaled_data).reshape(1,-1)

    # on load le modèle appris préalablement
    model   = joblib.load(path_to_model)
    
    # on prédit
    activities = model.predict(unscaled_data)

    return(activities)
    

