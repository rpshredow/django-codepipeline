from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
#from .models import Post

import requests
import json
    
def terrain(request):
    return render(request, 'projects/terrain.html', {'title': '3D Terrain App'})

def cluster(request):
    return render(request, 'projects/cluster.html', {'title': 'Raspberry Pi Cluster'})

def thesis(request):
    return render(request, 'projects/thesis.html', {'title': 'Masters Thesis'})

def fpgann(request):
    return render(request, 'projects/fpgann.html', {'title': 'FPGA Neural Network'})

def stock(request):
    return render(request, 'projects/stock.html', {'title': 'Show stock price'})

def price(request):
    stock = request.GET['stock']

    stock = stock.upper()

    td_consumer_key = 'WBQGUZ4CQPRMK7HF2MXHGHUE5BNMW4P9'

    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'

    full_url = endpoint.format(stock_ticker=stock)

    page = requests.get(url=full_url, params={'apikey' : td_consumer_key})

    content = json.loads(page.content)

    data = content[stock]

    symbol = data['symbol']
    description = data['description']
    bidPrice = data['bidPrice']
    askPrice = data['askPrice']
    lastPrice = data['lastPrice']
    openPrice = data['openPrice']
    highPrice = data['highPrice']
    lowPrice = data['lowPrice']
    closePrice = data['closePrice']
    totalVolume = data['totalVolume']
    fiftyTwoWkHigh = data['52WkHigh']
    fiftyTwoWkLow = data['52WkLow']
    peRatio = data['peRatio']
    divAmount = data['divAmount']
    divYield = data['divYield']
    divDate = data['divDate']


    return render(request, 'projects/result.html', {
        'symbol': symbol,
        'description': description,
        'bidPrice': bidPrice,
        'askPrice': askPrice,
        'lastPrice': lastPrice,
        'openPrice': openPrice,
        'highPrice': highPrice,
        'lowPrice': lowPrice,
        'closePrice': closePrice,
        'totalVolume': totalVolume,
        'fiftyTwoWkHigh': fiftyTwoWkHigh,
        'fiftyTwoWkLow': fiftyTwoWkLow,
        'peRatio': peRatio,
        'divAmount': divAmount,
        'divYield': divYield,
        'divDate': divDate,
        })