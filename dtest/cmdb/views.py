from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request, "blank.html")

def cmdb(request):
    return HttpResponse("CMDB page")

def asset(request,asset_id):
    return HttpResponse(f"Asset page {asset_id}")