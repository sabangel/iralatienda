from django.template import Context, loader
from django.http import HttpResponse
from main.models import Stores as st

def start_store(request):
    latest_poll_list = st.objects.all().order_by('name')[:5]
    t = loader.get_template('start_store.html')
    c = Context({
        'Stores': latest_poll_list,
    })
    return HttpResponse(t.render(c))
