from django.contrib import admin
from django.urls import include, path
from clinicavet.views import AnimalsViewSet, AppointmentsViewSet, ClientesViewSet
from rest_framework import routers 
from drf_spectacular.views import ( SpectacularAPIView, SpectacularSwaggerView, )


router = routers.DefaultRouter()
router.register(r'animais', AnimalsViewSet)
router.register(r'clientes', ClientesViewSet)
router.register(r'agendamento', AppointmentsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), 
        name='swagger-ui',
    ),
]

