import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def index(request):
    context = {
        'user':{'email':'demo@darient.com'},
    }
    return render(request,'core/index.html',context=context)
    
