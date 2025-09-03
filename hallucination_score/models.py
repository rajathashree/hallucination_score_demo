from django.db import models

class SurveyResponse(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True)
    question = models.TextField()
    response = models.TextField()
    trust_score = models.FloatField(null=True, blank=True) 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response {self.id} - {self.user_id}"
