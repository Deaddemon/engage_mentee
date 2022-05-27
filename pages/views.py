# pages/views.py


# from django.http import HttpResponse

# def homePageView(request):

#     return HttpResponse('Hello, World!')





from django.views.generic import TemplateView

class AnalysisPageView(TemplateView):

    template_name = 'analysis.html'

class PredictionPageView(TemplateView):
    template_name = 'prediction.html'