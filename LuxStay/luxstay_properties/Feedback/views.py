from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from .forms import FeedbackForm

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'Feedback/feedback_list.html', {'feedbacks': feedbacks})

def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'Feedback/feedback_form.html', {'form': form})

def feedback_update(request, pk):
    feedback_obj = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback_obj)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm(instance=feedback_obj)
    return render(request, 'Feedback/feedback_form.html', {'form': form})

def feedback_delete(request, pk):
    feedback_obj = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        feedback_obj.delete()
        return redirect('feedback_list')
    return render(request, 'Feedback/feedback_confirm_delete.html', {'object': feedback_obj})
