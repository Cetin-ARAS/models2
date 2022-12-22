from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
 
    def __str__(self):
        return f'{self.number} - {self.first_name} {self.last_name}'

    class Meta:
        ordering = ('-number',) # sıralamayı numaraya göre tersten yapar
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
        