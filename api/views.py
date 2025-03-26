from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import FlatHomePageDTO, FeedbackSerializer

class FlatHomePageView(APIView):
    def get(self, request):
        serializer = FlatHomePageDTO({})
        return Response(serializer.data)


class CreateFeedbackView(CreateAPIView):
    serializer_class = FeedbackSerializer
