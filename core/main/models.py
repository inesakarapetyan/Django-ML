# from django.db import models

# # Create your models here.

# class Prediction(models.Model):
#     feature1 = models.FloatField()
#     feature2 = models.FloatField()
#     prediction = models.FloatField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.feature1



# class Prediction(models.Model):
#     input_data = models.CharField(max_length=255)
#     predicted_output = models.CharField(max_length=255)



from django.db import models

class Prediction(models.Model):
    feature1 = models.FloatField()
    feature2 = models.FloatField()
    prediction = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
