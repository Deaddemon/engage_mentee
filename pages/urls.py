# pages/urls.py



# from django.urls import path


# from .views import homePageView



# urlpatterns = [
     
#      path('', homePageView, name='home')
# ]



from django.urls import path
from .views import AnalysisPageView, HomePageView, ReportPageView  


urlpatterns = [
    
    
    path('prediction/', ReportPageView.as_view(), name='report'), 
    path('analysis/', AnalysisPageView.as_view(), name='analysis'),
    path('', HomePageView.as_view() , name='home')
]
