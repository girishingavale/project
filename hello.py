import sys

from django.conf import settings
from django.conf.urls import patterns
from django.http import HttpResponse
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG=True,
    SECRET_KEY='keytest',
    ROOT_URLCONF=sys.modules[__name__],
)

def index(request):
    return HttpResponse('hello')

urlpatterns = patterns('',
                       (r'^hello-world/$',index),
                       )

if __name__ =="__main__":
    execute_from_command_line(sys.argv)