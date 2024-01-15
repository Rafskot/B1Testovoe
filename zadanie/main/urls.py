from django.urls import path
from .views import upload_excel, display_data, save_to_file

urlpatterns = [
    path('', upload_excel, name='upload_excel'),
    path('display/', display_data, name='display_data'),
    path('save/', save_to_file, name='save_to_file'),

]