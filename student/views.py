from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import studentClass
from .serializers import stuSerializer
@api_view(['GET'])
def studentList(request):
                     studentHand=studentClass.objects.all().order_by('-id')
                     stuserial=stuSerializer(studentHand,many=True)
                     return Response(stuserial.data)

@api_view(['POST'])
def AddStu(request):
      serializer=stuSerializer(data=request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)
@api_view(['POST'])
def update(request,pk):
     stuupdate=studentClass.objects.get(id=pk)
     serial=stuSerializer(instance=stuupdate,data=request.data)
     if serial.is_valid():
            serial.save()
     return Response(serial.data)
@api_view(['DELETE'])
def deleteStu(request,pk):
     studelete=studentClass.objects.get(id=pk)
     studelete.delete()
     return Response('deleted succesfully')                              