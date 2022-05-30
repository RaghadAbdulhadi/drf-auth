from django.shortcuts import render
from rest_framework.generics import (
                                        ListCreateAPIView,

                                    )
from rest_framework.permissions import IsAuthenticated
from .models import Perfume
from .serializers import PerfumeSerializer
# Create your views here.

class PerfumeListView(ListCreateAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer
    permission_classes = (IsAuthenticated,)