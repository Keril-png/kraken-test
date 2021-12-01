from django.db import models

# import requests

# resp = requests.get('https://api.kraken.com/0/public/OHLC?pair=EOSETH&since=0&interval=60')

# print(resp.json())

CHOICES = [
    'min',
    'max',
]

class Rec(models.Model):
    pair_name = models.CharField(max_length=10)
    time = models.DateTimeField()
    close = models.FloatField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()
    
    