from django.shortcuts import render
import json
import requests
from urllib.request import urlopen
from .models import Rec
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, date, time, timedelta
from .serializers import RecSerializer
from django.http import JsonResponse


@api_view(['GET'])
def get_rec(request, pair_name):
    
    if Rec.objects.filter(pair_name=pair_name).count() == 0:
        url = urlopen(f'https://api.kraken.com/0/public/OHLC?pair={pair_name}&since=0&interval=60').read()
        ohlc_list = json.loads(url).get('result')[pair_name]
        for ohlc in ohlc_list:
            Rec.objects.create(
                pair_name=pair_name, 
                time = datetime.fromtimestamp(ohlc[0]), 
                close = float(ohlc[4]),
                open = float(ohlc[1]),
                high = float(ohlc[2]),
                low = float(ohlc[3]),
                volume = float(ohlc[6]),
                )
    else:
        last_rec = Rec.objects.all().order_by('time').last()
        last_time = last_rec.time.timestamp()
        lol = datetime.today().timestamp() - last_time
        url_since_last_rec = urlopen(f'https://api.kraken.com/0/public/OHLC?pair={pair_name}&since={last_time}&interval=60').read()
        
        ohlc_list = json.loads(url_since_last_rec).get('result')[pair_name]
        for ohlc in ohlc_list:
            Rec.objects.create(
                pair_name=pair_name, 
                time = datetime.fromtimestamp(ohlc[0]), 
                close = float(ohlc[4]),
                open = float(ohlc[1]),
                high = float(ohlc[2]),
                low = float(ohlc[3]),
                volume = float(ohlc[6]),
                )

    recs = Rec.objects.all()
    first_rec_time = recs[0].time
    json_list = []
    index = 0
    date = first_rec_time
    while date.timestamp() <= datetime.today().timestamp():
        max_high = 0
        max_index = index
        min_low = recs[index].low
        min_index = index
        
        while recs[index].time.date() == date.date() :
            high = recs[index].high
            low = recs[index].low
            if high>max_high:
                max_high=high
                max_index=index
            if low<min_low:
                min_low=low
                min_index=index
            index+=1
                
        json_list.append(
            {
                'type': 'max',
                'time': recs[max_index].time,
                'close': recs[max_index].close,
                'open': recs[max_index].open,
                'high': recs[max_index].high,
                'low': recs[max_index].low,
                'volume': recs[max_index].volume
            }
        )
        json_list.append(
            {
                'type': 'min',
                'time': recs[min_index].time,
                'close': recs[min_index].close,
                'open': recs[min_index].open,
                'high': recs[min_index].high,
                'low': recs[min_index].low,
                'volume': recs[min_index].volume
            }
        )
        date += timedelta(days=1)        
        
    serializer = RecSerializer(recs, many=True)
    return JsonResponse(json_list, safe=False) 


    
        
