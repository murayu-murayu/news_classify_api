from rest_framework import generics, status
from rest_framework.response import Response
from appv1.serializers import BertPredictSerializer
from rest_framework.decorators import api_view
from rest_framework import mixins



class NewsClassifyAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = BertPredictSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


 
@api_view(['GET'])
def bert_predict(request, *args, **kwargs):
    if request.method == 'GET':
 
        serializer = BertPredictSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
