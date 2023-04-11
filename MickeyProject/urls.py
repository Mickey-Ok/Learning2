

from django.contrib import admin
from django.urls import path,include

from homeApp.views import (
    homeview,
    logoutview,
    registerview,
    loginview,
    
 
) 


from accountsApp.views import (
    accountview,
  
    contentview,
 
   
) 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview,name='home'),
    path('register/', registerview,name='register'), 
    path('login/', loginview,name='login'),
    path('accounts/',accountview,name='accounts'),   
    path('logout/', logoutview,name='logout'),
    path('contents/', contentview,name='contents'),

    
]

    
    
    

