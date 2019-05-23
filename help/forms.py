from django import forms
from help.models import Ticket, Account

DAY = 'День'
WEEK = 'Неделя'
MOUNTH = 'Месяц'
YEAR = 'Год (на оборудование)'
PRIORITY = (
    (DAY, 'День'),
    (WEEK, 'Неделя'),
    (MOUNTH, 'Месяц'),
    (YEAR, 'Год (на оборудование)')
)

class CreateTicket(forms.ModelForm):
    priority = forms.ChoiceField(choices=PRIORITY, label='Приоритет')
    class Meta:
        model = Ticket
        fields = ('priority', 'text', 'cabinet')
        widgets = {
            'text': forms.Textarea(
                attrs={'required': True, 'class': 'materialize-textarea'}
            )
        }
