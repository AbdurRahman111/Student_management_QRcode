from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', admin.site.urls),
    path('student_page/<int:pk>', views.student_page, name="student_page"),
]