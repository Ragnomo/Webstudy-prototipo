from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Course, Module, Lesson, UserProgress

@login_required
def dashboard(request):
    courses = Course.objects.all()
    course_data = []
    
    for course in courses:
        total_lessons = Lesson.objects.filter(module__course=course).count()
        completed = UserProgress.objects.filter(user=request.user, lesson__module__course=course).count()
        progress = int((completed / total_lessons) * 100) if total_lessons > 0 else 0
        
        course_data.append({
            'course': course,
            'progress': progress,
            'completed': completed,
            'total': total_lessons
        })
        
    return render(request, 'dashboard.html', {'course_data': course_data})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    is_completed = UserProgress.objects.filter(user=request.user, lesson=lesson).exists()
    return render(request, 'lesson_detail.html', {'lesson': lesson, 'is_completed': is_completed})

@csrf_exempt
@login_required
def mark_lesson_complete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lesson_id = data.get('lesson_id')
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        
        UserProgress.objects.get_or_create(user=request.user, lesson=lesson)
        return JsonResponse({'status': 'success', 'message': 'Aula concluída!'})
    return JsonResponse({'status': 'error'}, status=400)
  
