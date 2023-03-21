from rest_framework import serializers
from .models import Quizzes,Question,Answerserializers

class QuizSerializer(serializers.ModelSerializer):
     class Meta:
        model =Quizzes
        fields =[
            'title', 
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model =Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]       

class  RandomQuestionSerializer(serializers.ModelSerializer):

    answer = Answerserializers(many=True, read_only=True)
    class Meta:

        model =Question
        fields = [
            'title','answer',
        ]  
class QuestionSerializer(serializers.ModelSerializer):
    
    answer = Answerserializers(many=True, read_only=True)
    quiz = QuizSerializers(read_only=True)


    class Meta:

        model =Question
        fields = [
           'quiz', 'title','answer',
        ] 
