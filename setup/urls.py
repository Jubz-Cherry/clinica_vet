from django.contrib import admin
from django.urls import include, path
from clinicavet.views import AnimalsViewSet, AppointmentsViewSet, ClientesViewSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'animais', AnimalsViewSet)
router.register(r'clientes', ClientesViewSet)
router.register(r'agendamento', AppointmentsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
