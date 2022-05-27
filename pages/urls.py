# pages/urls.py



# from django.urls import path


# from .views import homePageView



# urlpatterns = [
     
#      path('', homePageView, name='home')
# ]



from django.urls import path
from .views import AnalysisPageView, PredictionPageView


urlpatterns = [
    path('prediction/', PredictionPageView.as_view(), name='prediction'), # new
    path('', AnalysisPageView.as_view(), name='analysis'),
]
