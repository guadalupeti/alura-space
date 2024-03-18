from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Nome de login',
        max_length = 100,
        required = True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex: João Silva'
            }
        )

    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = 'Nome de cadastro',
        max_length = 100,
        required = True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex: João Silva'
            }
        ))
    email = forms.EmailField(
        label = 'Email de cadastro',
        max_length = 100,
        required = True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex: joao@xpto.com', 
            }
        )
    )

    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }
        )
    )
    senha1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirme sua senha'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possível inserir espaços no nome.')


    

    