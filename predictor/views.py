from django.shortcuts import render
from .forms import InputForm # Ensure InputForm exists in forms.py
import joblib
import numpy as np
import os
from django.conf import settings

# def index(request):
#     return render(request, 'predictor/index.html', {})

 
model_path = os.path.join(settings.BASE_DIR, 'predictor', 'model', 'scaler.pkl')
model = joblib.load('predictor/ml_model/scaler.pkl')
  

# def index(request):
#     form = InputForm()
#     return render(request, 'predictor/index.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # Do prediction...
            return render(request, 'predictor/index.html', {
                'form': form,
                'prediction': result
            })
    else:
        form = InputForm()
    return render(request, 'predictor/index.html', {'form': form})

    #return render(request, 'index.html', {'form': form})


