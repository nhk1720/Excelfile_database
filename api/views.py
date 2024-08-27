# from django.shortcuts import render
# from .models import Student
# from .serializer import Student_serializer
# from rest_framework import viewsets
# import pandas as pd
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework import status



# class Studentview(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=Student_serializer
    
#     # @action(detail=False, methods=['post'])
#     def create(self, request):
#         print("sssssssssssssssssssssss")
#         file=request.FILES.get('file')
#         if not file.name.endswith('.xlsx'):
#             return Response({'error':'file is not in excel fromet'},status=status.HTTP_400_BAD_REQUEST)
#         try :
#             df=pd.read_excel(file)
#             print("++++++++++++++++++++++++==============")
#         except Exception as e:
#             return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
#         items=[]
#         for index,row in df.iterrows():
#             Student_data={
#             'name':row['name'],
#             'age':row['age'],
#             'city':row['city']
#         }
#             serializer=Student_serializer(data=Student_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 items.append(serializer.data)
#             return Response({'items': items}, status=status.HTTP_201_CREATED)
        
            
            


# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Student
# from .serializers import Student_serializer
# import pandas as pd

from django.shortcuts import render
from .models import Student
from .serializer import Student_serializer
from rest_framework import viewsets
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class Studentview(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serializer
    # def list(self, request, *args, **kwargs):
    #     file=request.FILES.get

    def create(self, request):
        print("sssssssssssssssssssssss")
        file = request.FILES.get('file')
        if not file.name.endswith('.xlsx'):
            return Response({'error': 'File is not in Excel format'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            df = pd.read_excel(file)
            print("++++++++++++++++++++++++==============")
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        items = []
        for index, row in df.iterrows():
            student_data = {
                'name': row['name'],
                'age': row['age'],
                'city': row['city']
            }
            serializer = Student_serializer(data=student_data)
            if serializer.is_valid():
                serializer.save()
                items.append(serializer.data)

        return Response({'items': items}, status=status.HTTP_201_CREATED)
