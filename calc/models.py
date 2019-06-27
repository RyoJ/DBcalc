from django.db import models

class ANS(models.Model):
    answer = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"{0}:{1}... ".format(self.id, self.answer)