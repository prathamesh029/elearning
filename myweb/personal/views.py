from django.shortcuts import render

def index(request):
    return  render (request,'personal/home.html')

def contact(request):
      return  render (request,'personal/basic.html')

def PROGRAMMING(request):
      return  render (request,'personal/PROG.html')


def callme(request):
      return  render (request,'personal/callme.html')


def cpp(request):
      return  render (request,'personal/cpp.html')

    

def javaa(request):
      return  render (request,'personal/javaa.html')


def PYTHONN(request):
      return  render (request,'personal/PYTHONN.html')

