from django.urls import path
from . views import PerfumeListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('perfumes-list', PerfumeListView.as_view(), name='perfumes_list'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]

"""

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDAwMjQ4NSwiaWF0IjoxNjUzOTE2MDg1LCJqdGkiOiIwYWQzNWY4NTQ0Y2U0NWQ1ODM2N2U2NThhMTYyODAyYSIsInVzZXJfaWQiOjF9.TedWnxtnTEbiIgXw8cqLCGknYWHzhVuTSljSvMVfck4",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzOTE2Mzg1LCJpYXQiOjE2NTM5MTYwODUsImp0aSI6Ijk5MjQxMGFlYjIzMzQ3NDQ5ODgxZGQ1ODBkMWQ3NTIzIiwidXNlcl9pZCI6MX0.hrtIWbPXzH7NXgANMFq3L44AvtJDT6zFeW5pyhEKWHc"
}
"""