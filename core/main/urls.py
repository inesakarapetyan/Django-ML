from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),
    # path('predict_form/', views.predict_form, name='predict_form'),
]

