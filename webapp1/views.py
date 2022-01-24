from django.shortcuts import render
from .models import Verifica_Risultati_Candidato, Esami_sostenuti_e_relativi_esiti
# Create your views here.


def student_page(request, pk):
    print(pk)
    get_student =  Verifica_Risultati_Candidato.objects.get(MATRICOLA=pk)
    all_Esami_sostenuti_e_relativi_esiti  = Esami_sostenuti_e_relativi_esiti.objects.filter(Student = get_student)
    context = {'get_student':get_student, 'all_Esami_sostenuti_e_relativi_esiti':all_Esami_sostenuti_e_relativi_esiti}
    return render(request, 'student_page.html', context)