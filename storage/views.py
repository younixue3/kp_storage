from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def store_file(request):
    print(request.FILES)
    if 'single' in request.query_params:
        file = request.FILES['image']
        fs = FileSystemStorage()
        filename = file.name
        filename = fs.save(str(file.name).replace(' ', '_'), file)
        uploaded_file_url = fs.url(filename)
    else:
        file = request.FILES['bukti_pembayaran']
        fs = FileSystemStorage()
        filename = fs.save(str(file.name).replace(' ', '_'), file)
        uploaded_file_url = fs.url(filename)
    return Response(request.build_absolute_uri(uploaded_file_url))

