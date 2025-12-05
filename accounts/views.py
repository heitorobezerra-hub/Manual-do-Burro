from django.shortcuts import render, redirect
from .models import Usuario

def login_view(request):
    if 'usuario_id' in request.session:
        return redirect('home')

    if request.method == 'POST':
        
        nome = request.POST.get('nome_login')
        senha = request.POST.get('senha_login')

        # --- DEBUG NO TERMINAL ---
        print(f"O SITE RECEBEU -> Nome: '{nome}' | Senha: '{senha}'")
        # -------------------------

        try:
       
            usuario = Usuario.objects.get(nome=nome, senha=senha)
            
            
            request.session['usuario_id'] = usuario.id
            return redirect('home')
            
        except Usuario.DoesNotExist:
            print("ERRO: Usuário não encontrado no banco.")
            return render(request, 'registration/login.html', {'erro': 'Nome ou Senha incorretos.'})

    return render(request, 'registration/login.html')
    