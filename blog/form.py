from django import forms  
from blog.models import Message 

class MessageForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)
		self.fields['nome'].widget.attrs['placeholder'] = 'Nome'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['mensagem'].widget.attrs['placeholder'] = 'Escreve ...'

	class Meta:
		model = Message
		fields = ['nome', 'email', 'mensagem'] 

	


	