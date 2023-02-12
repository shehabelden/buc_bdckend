from .ser import *
from .models import *
from rest_framework import mixins, generics, permissions


class images_class_post(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = images_model.objects.all()
    serializer_class = images_ser_post
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
       return  self.create(request,*args,**kwargs)
class images_class_get(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = images_model.objects.all()
    serializer_class = images_ser_get
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
       return  self.list(request,*args,**kwargs)
