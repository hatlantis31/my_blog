from django.urls import path

from . import views

# URLConf
urlpatterns = [
    # path to index.html
    path('home/', views.IndexView.as_view(), name='index'),
    # path to blog.html
    path('home/blog', views.BlogView.as_view(), name='blog'),
    path('home/blog/<slug:slug>/', views.PostView.as_view(), name='post'),
    path('home/about', views.AboutView.as_view(), name='about'),
    path('home/contact', views.ContactView.as_view(), name='contact'),
    # path for social media icons

]
