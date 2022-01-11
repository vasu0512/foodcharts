from django.shortcuts import render
import pandas as pd
from .forms import foodForm
from .models import fooddata
# Create your views here.
def indexPage(request):
     data=fooddata.objects.all()
                                     if request.method=='POST'
        context={'data':data,
                }
    
   
                                         return render(request,'index.html',context)
