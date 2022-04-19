from django.urls import path

from .views import homePageView, addView, deleteView, downloadView, phishing, removingimage, admininfoleaked

urlpatterns = [
    path('', homePageView, name='home'),
    path('add/', addView, name='add'),
    path('download/<int:fileid>', downloadView, name='add'),
    path('delete/', deleteView, name='delete'),
    path('phishing/', phishing, name='phishing'),
    path('removingimage/', removingimage, name='removingimage'),
    path('admininfoleaked/', admininfoleaked, name='admininfoleaked'),
]
