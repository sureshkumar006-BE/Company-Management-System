from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    email_id = models.EmailField()

    company_code = models.CharField(
        max_length=5,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z]{2}[0-9]{2}[EN]$',
                message='Format: 2 letters, 2 digits, E or N'
            )
        ]
    )

    strength = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]
    )

    website = models.URLField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
