from django.db import models

# Create your models here.
genre=[
    ('Fantasy','Fantasy'),
    ('Folklore','Folklore'),
    ('HistoricalFiction','HistoricalFiction'),
    ('Horror','Horror'),
    ('Mystery','Mystery'),
    ('Poetry','Poetry'),
    ('Romance','Romance'),
    ('ScienceFiction','ScienceFiction'),
    ('SelfHelp','SelfHelp'),

]


class genres(models.Model):
    name=models.CharField(max_length=50, choices=genre)
    description=models.CharField(max_length=1000) 

    def __str__(self):
        return self.name 
    
class stories(models.Model):
    genres=models.ForeignKey(genres,choices=genre, on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    story=models.TextField(max_length=5000) 

    def __str__(self):
        return self.title








# choice=[
#     ('M','Male'),
#     ('F','Female')

# ]

# class profile(models.Model):
#     username=models.CharField(max_length=50)
#     email=models.EmailField
#     bio=models.TextField(max_length=200)
#     gender=models.CharField(max_length=10, choices=choice) 

#     def __str__(self):
#         return self.email
    