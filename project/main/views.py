from django.views.generic import ListView, DetailView
from main.models import Advert
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from main.serializers import AdvertModelSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

app_name = 'main'

class AdvertList(ListView):
    model = Advert
    fields = ['title', 'address', 'price', 'owner']
    template_name = 'main/index.html'
    context_object_name = 'advert_list'
    serializer_class = AdvertModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_active:
            return Advert.objects.for_user(self.request.user)
        else:
            return Advert.objects.all()

class AdvertDetail(LoginRequiredMixin, DetailView):
    model = Advert
    fields = ['title', 'address', 'description', 'price', 'number_of_views', 'owner']
    template_name = 'main/detail.html'
    redirect_field_name = '/advert'
    serializer_class = AdvertModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_active:
            return Advert.objects.for_user(self.request.user)

@api_view(['GET', 'POST'])
def adverts_list(request, format=None):
    if request.method == 'GET':
        adverts = Advert.objects.all()
        serializer = AdvertModelSerializer(adverts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdvertModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def adverts_detail(request, pk):
    try:
        student = Advert.objects.get(id=pk)
    except Advert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertModelSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AdvertModelSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
	username = request.data.get('username')
	password = request.data.get('password')
	user = authenticate(username=username, password=password)
	if user is None:
		return Response({'error': 'Invalid data'})
	token, created = Token.objects.get_or_create(user=user)
	return Response({'token': token.key})