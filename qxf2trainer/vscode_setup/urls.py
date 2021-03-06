from django.urls import path
from . import views

urlpatterns = [
    path('before-you-begin', views.beforeyoubegin, name='beforeyoubegin'),
    path('what-to-expect', views.whattoexpect, name='whattoexpect'),
    path('tutorial', views.install_python, name='tutorial'),
    path('did-you-complete', views.didyoucomplete, name='didyoucomplete'),
    path('once-you-complete',views.onceyoucomplete, name='onceyoucomplete'),
]
