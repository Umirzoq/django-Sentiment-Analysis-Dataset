from datetime import time

from django.http import HttpResponse
from django.shortcuts import render
from django_contact_form.forms import ContactForm
import time
from . import pridec


def index(request):

    if request.method == 'POST':
        #time.sleep(5)
        txt = request.POST['txtData']
        print(txt)
        v = pridec.execute(txt)
        img = ''
        if v == 1:
            v = 'Ijobiy'
            img = 'positive.jpg'
        elif v == 2:
            v = 'Salbiy'
            img = 'negative.jpg'
        else :
            v = 'Neytral'
            img = 'neutral.jpg'


        return render(request, 'main/index.html',
                  {'show_modal': True, "prediction": v, 'imageName': img,'txtData': txt})
    else:
        return render(request, 'main/index.html')
