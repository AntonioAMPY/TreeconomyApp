from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

import requests
import json


def getResponseProducts(request):
  try:
    getResponse = requests.get('https://testbankapi.firebaseio.com/products.json')
    arrayJson = list(getResponse.json().items())
    sumvalue = sum([o[1]['value'] for o in arrayJson ])
  except:
    return JsonResponse({"Ocurrio un error"},safe=False)
    
  return render(request,'index.html',{'arrayJson':arrayJson, 'sumvalue': sumvalue})

def postResponseProducts(request):
  data = {
    "category": request.POST['category'],
    "description": request.POST['description'],
    "identification": request.POST['identification'],
    "initdate": request.POST['initdate'],
    "productname": request.POST['productname'],
    "value":int(request.POST['value'])
  }
  getResponse = requests.post('https://testbankapi.firebaseio.com/products.json',data=json.dumps(data))
  try:
    getResponse.raise_for_status()
    return redirect('/')
  except requests.exceptions.HTTPError  as err:
    return JsonResponse({'Status':'ERROR','message':'Error al guardar'})
    raise SystemExit(err)
  


def putProducts (request):
  data = {
    "category": request.POST['category'],
    "description": request.POST['description'],
    "identification": request.POST['identification'],
    "initdate": request.POST['initdate'],
    "productname": request.POST['productname'],
    "value":int(request.POST['value'])
  }

  url = 'https://testbankapi.firebaseio.com/products/'+request.POST['id']+".json"

  putResponse = requests.put(url, data=json.dumps(data))
  try:
    putResponse.raise_for_status()
    print(putResponse.raise_for_status())
    return redirect('/')
  except requests.exceptions.HTTPError as err:
    return JsonResponse({'status':'Error','message':'Error al actualizar el producto'})

  print(putResponse)

def deleteProducts (request):
  url = 'https://testbankapi.firebaseio.com/products/'+request.POST['id']+".json"
  deleteResponse = requests.delete(url)
  try:
    deleteResponse.raise_for_status()
    print(deleteResponse.raise_for_status())
    return redirect('/')
  except requests.exceptions.HTTPError as err:
    return JsonResponse({'status':'Error','message':'Error al eliminar el producto'})

  print(deleteResponse)