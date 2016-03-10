from django.shortcuts import render
import time

from hendrix.contrib.async.messaging import hxdispatcher
from hendrix.experience import crosstown_traffic

# Create your views here.

def hello(request):

    llama = True

    @crosstown_traffic()
    def my_long_thing():
        for i in range(5):
            time.sleep(1)
            hxdispatcher.send('noodly_messages', "Another noodle")

    return render(request, 'hello.html')
