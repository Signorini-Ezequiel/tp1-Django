from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL de aplicaciones
    re_path('', include("applications.carrer.urls")),
    re_path('', include("applications.signature.urls")),
    re_path('', include("applications.student.urls")),
    re_path('', include("applications.students_signatures.urls")),
]
