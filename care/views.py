from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes,Question
from .serializers import QuizSerializer, RandomQuestionSerializer ,QuestionSerializer
from rest_framework.views import APIView

# Create your views here.
class Quiz(generics.ListAPIView):

    serializer_class =QuizSerializer
    queryset =Quizzes.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format:None, **kwargs):
        question =Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer =QuestionSerializer(question,many=True)
        return Response(serializer.data)