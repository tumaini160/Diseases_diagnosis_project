from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

def index(request):
    return render(request,"index.html")

def hiv(request):
    return render(request, "hiv.html")

def result(request):
    
    data=pd.read_csv('C:/Users/ATECH-G3/OneDrive/Desktop/mydiagnos/HIV_data.csv')
    x=data.drop(columns=['Diagnosis'])
    y=data['Diagnosis']
    model=DecisionTreeClassifier()
    model.fit(x,y)

    age=int(request.GET['age'])
    weight=float(request.GET['weight'])
    cd4_count=int(request.GET['CD4'])
    viral_load=int(request.GET['Viral'])

    pred=model.predict([[age,weight,cd4_count,viral_load]])
    diagnose="The diagnosis shows that the patient is HIV " + pred

    return render(request, "hiv.html", {"result":diagnose})

def malaria(request):
    return render(request,"malaria.html")

def malariaresult(request):
    malariadata=pd.read_csv('C:/Users/ATECH-G3/OneDrive/Desktop/mydiagnos/malaria_data.csv')
    x=malariadata.drop(columns=['Diagnosis'])
    y=malariadata['Diagnosis']
    cat_features=["Age","Chills","Fever","Sweating","Fatigue"]
    one_hot=OneHotEncoder()
    transformer=ColumnTransformer([("one_hot",one_hot,cat_features)],remainder="passthrough")
    transformedx=transformer.fit_transform(x)

    age=int(request.GET['age'])
    chills=request.GET['chills']
    fever=request.GET['fever']
    sweating=request.GET['sweating']
    fatigue=request.GET['fatigue']

    "Age"==age
    "Chills"==chills
    "Fever"==fever
    "Sweating"==sweating
    "Fatigue"==fatigue

    x_train,x_test,y_train,y_test=train_test_split(transformedx,y,test_size=0.3)
    model=DecisionTreeClassifier()
    model.fit(transformedx,y)

    pred=model.predict(x_test)[0]
    diagnose="Status... " + pred

    return render(request, "malaria.html", {"result2":diagnose})

def TB(request):
    return render(request,"tb.html")

def tbresult(request):
    malariadata=pd.read_csv('C:/Users/ATECH-G3/OneDrive/Desktop/mydiagnos/TB_data.csv')
    x=malariadata.drop(columns=['Diagnosis'])
    y=malariadata['Diagnosis']
    cat_features=["Age","Chest pain","Fever","Persistent cough","Fatigue",
                  "Night sweats","Loss of appetite","Weight loss","Shortness of breath"]
    one_hot=OneHotEncoder()
    transformer=ColumnTransformer([("one_hot",one_hot,cat_features)],remainder="passthrough")
    transformedx=transformer.fit_transform(x)

    age=int(request.GET['age'])
    chest=request.GET['chest_pain']
    fever=request.GET['fever']
    cough=request.GET['cough']
    fatigue=request.GET['fatigue']
    sweats=request.GET['sweats']
    appetite=request.GET['appetite']
    weight=request.GET['weight']
    breath=request.GET['breath']

    "Age"==age
    "Chest pain"==chest
    "Fever"==fever
    "Persistent cough"==cough
    "Fatigue"==fatigue
    "Night sweats"==sweats
    "loss of appetite"==appetite
    "Weight loss"==weight
    "Shortness of breath"==breath

    x_train,x_test,y_train,y_test=train_test_split(transformedx,y,test_size=0.3)
    model=DecisionTreeClassifier()
    model.fit(transformedx,y)

    pred=model.predict(x_test)[0]
    diagnose="Status... " + pred

    return render(request, "tb.html", {"result3":diagnose})






