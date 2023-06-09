"""
URL configuration for vhms1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('vhms1/', include('vhmsapp.urls')),
# ]



from django.contrib import admin
from django.urls import path, include
#from blockchain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('get_chain/', views.get_chain, name="get_chain"),
    # path('mine_block/', views.mine_block, name="mine_block"),
    # path('is_valid/', views.is_valid, name="is_valid"),
    path('vhms1/', include('vhmsapp.urls')),
    path('vhms/', include('vhmsapp.urls')),
]
