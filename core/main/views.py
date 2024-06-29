# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Prediction
# import pickle
# import os

# def predict(request):
#     if request.method == 'POST':
#         data = request.POST
#         # Load the model
#         model_path = os.path.join(os.path.dirname(__file__), 'ml_models', 'model.pkl')
#         with open(model_path, 'rb') as f:
#             model = pickle.load(f)
        
#         # Prepare the data for prediction (example assumes numerical input)
#         feature1 = float(data['feature1'])
#         feature2 = float(data['feature2'])
#         features = [feature1, feature2]
        
#         # Make a prediction
#         prediction = model.predict([features])[0]
        
#         # Save to the database
#         prediction_record = Prediction(feature1=feature1, feature2=feature2, prediction=prediction)
#         prediction_record.save()
        
#         # Return the prediction result as JSON
#         return JsonResponse({'prediction': prediction})
#     return JsonResponse({'error': 'Invalid request method'}, status=400)


# def predict_form(request):
#     return render(request, 'main/index.html')




#--------------------------------------------------------------------------------




# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Prediction  # Only if using a model to store predictions
# import pickle
# import os

# def predict(request):
#     if request.method == 'POST':
#         data = request.POST
#         # Load the model
#         model_path = os.path.join(os.path.dirname(__file__), 'ml_models', 'model.pkl')
#         with open(model_path, 'rb') as f:
#             model = pickle.load(f)
        
#         # Prepare the data for prediction
#         feature1 = float(data['feature1'])
#         feature2 = float(data['feature2'])
#         features = [feature1, feature2]
        
#         # Make a prediction
#         prediction = model.predict([features])[0]
        
#         # Save to the database if using a model
#         prediction_record = Prediction(feature1=feature1, feature2=feature2, prediction=prediction)
#         prediction_record.save()
        
#         # Return the prediction result as JSON
#         return JsonResponse({'prediction': prediction})
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

# def predict_form(request):
#     return render(request, 'main/index.html')


# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
# import os
# import pandas as pd
# import pickle

# # Load the trained regression model
# model = pickle.load(open('model.pkl', 'rb'))

# def predict(request):
#     if request.method == 'POST':
#         # Load the test data
#         test_data = pd.read_csv('test_data.csv')

#         # Generate predictions using the trained model
#         predictions = model.predict(test_data)

#         # Save the predictions to a CSV file
#         pd.DataFrame(predictions).to_csv('predictions.csv', index=False)

#         # Download the predictions file
#         filename = 'predictions.csv'
#         response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
#         response['Content-Length'] = os.path.getsize(filename)
#         response['Content-Disposition'] = 'attachment; filename=%s' % 'predictions.csv'
#         return response

#     else:
#         return render(request, 'predict.html')

#--------------------------------------------------------------------
# import os
# import pickle
# import numpy as np
# from django.shortcuts import render

# # Load the trained model from the pickle file
# with open('model.pkl', 'wb') as file:
#     model = pickle.load(file)

# def predict(request):
#     if request.method == 'POST':
#         # Get the input data from the form
#         input_data = np.array(request.POST.getlist('input_data[]')).reshape(1, -1)

#         # Make predictions using the trained model
#         predictions = model.predict(input_data)

#         # Render the template with the predictions
#         return render(request, 'predict.html', {'predictions': predictions[0]})

#     else:
#         # Render the empty form
#         return render(request, 'main/index.html')


#------------------------------------------------------------------------


import pickle
import numpy as np
from django.shortcuts import render

# Load the trained model from the pickle file
with open('model.pkl', 'wb') as file:
    dt = pickle.load(file)

def predict(request):
    if request.method == 'POST':
        # Get the input data from the form
        input_data = np.array(request.POST.getlist('input_data[]')).reshape(1, -1)

        # Make predictions using the trained model
        predictions = dt.predict(input_data)

        # Render the template with the predictions
        return render(request, 'main/index.html', {'predictions': predictions[0]})

    else:
        # Render the empty form
        return render(request, 'main/index.html')