from django.shortcuts import render, redirect
from .models import SurveyResponse

def survey_chat(request):
    if request.method == "POST":
        participant_id = request.POST.get("participant_id")
        question = request.POST.get("question")
        llm_answer = request.POST.get("llm_answer")
        hallucination_score = request.POST.get("hallucination_score")  
        user_feedback = request.POST.get("user_feedback")

        SurveyResponse.objects.create(
            participant_id=participant_id,
            question=question,
            llm_answer=llm_answer,
            hallucination_score=hallucination_score,
            user_feedback=user_feedback
        )
        return redirect("thank_you")

    return render(request, "hallucination_demo_ui/hallucination_demo_chat.html")
