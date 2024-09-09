# models.py
from django.db import models

class UserFeedback(models.Model):
    user_message = models.CharField(max_length=100)
    bot_response = models.CharField(max_length=100)

    def __str__(self):
        return f"User: {self.user_message}, Bot: {self.bot_response}"

    class Meta:
        verbose_name_plural = "User Feedback"
        db_table = "user_feedback"