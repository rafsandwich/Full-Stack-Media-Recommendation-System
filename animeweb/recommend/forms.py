from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

#class RecommendForm(forms.Form):



    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.attrs = {'novalidate': ''}
    #     self.helper.form_id = 'id-exampleForm'

class MessageForm(forms.Form):
    text_input = forms.CharField()

    textarea = forms.CharField(
        widget = forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices = (
            ('option_one', "modern"), 
            ('option_two', "older")
        ),
        widget = forms.RadioSelect,
        initial = 'option_two',
    )

    checkboxes = forms.MultipleChoiceField(
        choices = (
            ('option_one', "One"), 
            ('option_two', 'two'),
            ('option_three', 'three')
        ),
        initial = 'option_one',
        widget = forms.CheckboxSelectMultiple,  
    )

    multicolon_select = forms.MultipleChoiceField(
        choices = (('1', 'Action'), ('2', 'Romance'), ('3', 'Drama'), ('4', 'Thriller'), ('5', 'Fantasy')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'radio_buttons',
        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
        )
    )