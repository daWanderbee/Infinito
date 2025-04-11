from django.db import models
from django.core.validators import RegexValidator

class Student(models.Model):
    GAMES = [
        ('Basketball', 'Basketball'),
        ('Badminton', 'Badminton'),
        ('Chess', 'Chess'),
        ('Table Tennis', 'Table Tennis'),
        ('Throwball', 'Throwball'),
        ('Carrom', 'Carrom'),
        ('Squid Games', 'Squid Games'),
        ('Lemon & Spoon Race', 'Lemon & Spoon Race'),
        ('Marathon', 'Marathon'),
        ('Other', 'Other'),
    ]

    BLOCKS = [
        ('A', 'A Block'),
        ('B', 'B Block'),
        ('C', 'C Block'),
        ('D', 'D Block'),
        ('E', 'E Block'),
        ('F', 'F Block'),
        ('G', 'G Block'),
        ('H', 'H Block'),
        ('I', 'I Block'),
        ('J', 'J Block'),
    ]

    name = models.CharField(max_length=100)
    registration_number = models.CharField(
        max_length=9,
        validators=[RegexValidator(r'^\d{2}[A-Z]{3}\d{4}$', 'Registration number must be in format 00XXX0000.')]
    )
    phone = models.CharField(max_length=15)
    vit_email = models.EmailField(
        validators=[RegexValidator(r'^[a-zA-Z0-9._%+-]+@vitstudent\.ac\.in$', 'Email must be a valid VIT student email.')]
    )
    hostel = models.CharField(max_length=1, choices=BLOCKS)
    room_number = models.CharField(max_length=10)
    game_playing = models.CharField(max_length=30, choices=GAMES)
    position = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        unique_together = ('registration_number', 'game_playing')
        constraints = [
            models.UniqueConstraint(fields=['vit_email', 'game_playing'], name='unique_email_game')
        ]

    def __str__(self):
        return f"{self.name} ({self.registration_number})"
