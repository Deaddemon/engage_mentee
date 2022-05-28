# pages/urls.py



# from django.urls import path


# from .views import homePageView



# urlpatterns = [
     
#      path('', homePageView, name='home')
# ]



from django.urls import path
from .views import AnalysisPageView, HomePageView, PredictionPageView  


urlpatterns = [
    
    
    path('prediction/', PredictionPageView.as_view(), name='prediction'), 
    path('analysis/', AnalysisPageView.as_view(), name='analysis'),
    path('', HomePageView.as_view() , name='home')
]
