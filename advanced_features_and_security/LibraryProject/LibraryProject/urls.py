from django.http import HttpResponse

def csp_test_view(request):
    response = HttpResponse("CSP Enabled")
    response["Content-Security-Policy"] = "default-src 'self';"
    return response
