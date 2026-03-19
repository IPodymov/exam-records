from django.shortcuts import render, redirect
from .models import Exam
from .forms import ExamForm

def exam_list(request):
    exams = Exam.objects.filter(is_public=True).order_by('date')
    return render(request, 'exams/exam_list.html', {'exams': exams})

def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'exams/exam_form.html', {'form': form})
