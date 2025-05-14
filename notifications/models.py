from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Notification(models.Model):
    # Tipos de notificación
    MESSAGE = 'message'
    ALERT = 'alert'
    SYSTEM = 'system'
    
    TYPE_CHOICES = [
        (MESSAGE, 'Mensaje'),
        (ALERT, 'Alerta'),
        (SYSTEM, 'Sistema'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=SYSTEM
    )
    read = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'

    def __str__(self):
        return f"{self.title} - {self.user.username}"