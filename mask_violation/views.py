from django.shortcuts import render
from mask_violation.models import MaskViolation

# Create your views here.
def viewmask(request):
    ob = MaskViolation.objects.all()
    context = {
        'obval': ob,
    }
    return render(request, 'mask_violation/maskDetection.html', context)
