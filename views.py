from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#index response
def index(request):
    return HttpResponse("this is the index method view")

#detail method for data request
def detail(request,question_id):
    return HttpResponse('Related Question is' %question_id)

#result method  for data request
def results(request,question_id):
    response="you are looking at the result of "
    return HttpResponse(response %question_id)

