from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
	path("submit_mas_entry", views.submit_mas_entry, name="submit_mas_entry"),
	path("show_excel", views.show_excel, name="show_excel"),
]
