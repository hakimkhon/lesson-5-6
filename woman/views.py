from django.shortcuts import render
from .models import Woman
from .serializers import WomanSerializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse

from django.forms.models import model_to_dict


class DetailWoman(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializers

# class  WomanAPIView(ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializers


class WomanAPIView(APIView):

    def get(self, request):
        lst = Woman.objects.all()
        return Response({'posts': WomanSerializers(lst, many=True).data})
# class WomanAPIView(APIView):
#     def get(self, request):
#         lst = Woman.objects.all().values()
#         return Response({'posts': list(lst)})


    def post(self, request):
        print("post")
        # return Response({'title': 'hammaga salom'})
        serializer = WomanSerializers(data=request.data)    #hatolikni ko'rsatmaslik
        serializer.is_valid(raise_exception=True)

        post_new = Woman.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            category_id = request.data['category_id']
        )

        # return Response({'post':model_to_dict(post_new)})
        return Response({'post': WomanSerializers(post_new).data})

    # def put(self, request):
    #     print("put ishladi")

    def delete(self, request):
        pk=request.data["id"]
        woman = Woman.objects.get(pk=pk)
        woman.delete()
        return JsonResponse({"status": "deleted"}, status=status.HTTP_204_NO_CONTENT)









#         class WomanAPIView(APIView):

#     def get(self, request):
#         lst = Woman.objects.all()
#         return Response({'posts': WomanSerializers(lst, many=True).data})
# # class WomanAPIView(APIView):
# #     def get(self, request):
# #         lst = Woman.objects.all().values()
# #         return Response({'posts': list(lst)})


#     def post(self, request):
#         # return Response({'title': 'hammaga salom'})
#         serializer = WomanSerializers(data=request.data)    #hatolikni ko'rsatmaslik
#         serializer.is_valid(raise_exception=True)

#         post_new = Woman.objects.create(
#             title = request.data['title'],
#             content = request.data['content'],
#             category_id = request.data['category_id']
#         )

#         # return Response({'post':model_to_dict(post_new)})
#         return Response({'post': WomanSerializers(post_new).data})

#     def delete(self, request, pk):
#         try: 
#             woman = Woman.objects.get(pk=pk) 
#         except Woman.DoesNotExist: 
#             return JsonResponse({'message': 'The Woman does not exist'}, status=status.HTTP_404_NOT_FOUND)
#         woman.delete()
#         return JsonResponse({"status": "deleted"}, status=status.HTTP_204_NO_CONTENT)