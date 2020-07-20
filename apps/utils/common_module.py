from django.shortcuts import render


def page_not_found(request):
    response = render('404.html')
    response.status_code = 404
    return response


def page_error(request):
    response = render('500.html')
    response.status_code = 500
    return response