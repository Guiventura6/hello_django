from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, num1, num2):
    result = num1 + num2
    return HttpResponse('<h1>Soma</h1>'
                        '<h2>{} + {} = {}</h2>'.format(num1, num2, result))

def multiplicacao(request, num1, num2):
    result = num1 * num2
    return HttpResponse('<h1>Multiplicacao</h1>'
                        '<h2>{} * {} = {}</h2>'.format(num1, num2, result))

def divisao(request, num1, num2):
    result = num1 / num2
    return HttpResponse('<h1>Divisao</h1>'
                        '<h2>{} / {} = {}</h2>'.format(num1, num2, result))

def subtracao(request, num1, num2):
    result = num1 - num2
    return HttpResponse('<h1>Subtracao</h1>'
                        '<h2>{} - {} = {}</h2>'.format(num1, num2, result))