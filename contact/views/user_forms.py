from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib import auth



def register(request):
    form = RegisterForm()
    
    messages.info(request, "Qlqr coisa")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered')
            
            return redirect('contact:index')
            
    context = {
        'form': form,
    }    
        
    return render(
        request,
        'contact/register.html',
        context
        
    )
    
def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('contact:index')
        else:
            messages.error(request, 'Invalid login')
            
    context = {
        'form': form,
    }    
        
    return render(
        request,
        'contact/register.html',
        context
        
    )
    
def logout_view(request):
    auth.logout(request)
    
    return redirect('contact:login')

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
        
    if request.method != 'POST':        
        return render(
            request,
            'contact/register.html',
            {
                'form':form,
            }
            
        )
        
    form = RegisterUpdateForm(data = request.POST, instance=request.user)
    
    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {
                'form':form,
            }
            
        )
        
    form.save()
    return render(
            request,
            'contact/register.html',
            {
                'form':form,
            }
        )