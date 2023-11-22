from django import forms
from .models import Cita_con_medico

class formulario_cita_medico(forms.ModelForm):
    class Meta:
        model = Cita_con_medico
        fields = ['paciente','medico', 'dia', 'horario']
