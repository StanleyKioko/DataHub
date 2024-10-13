# content/urls.py

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('upload/', views.upload_document, name='upload_document'),  # Document upload page
    path('signup/', views.signup, name='signup'),  # User signup page
    path('documents/<int:document_id>/', views.document_detail, name='document_detail'),  # Document detail page
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),

]


