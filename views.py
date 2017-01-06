##以下為程式碼參考

def login(request):
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    remember = request.POST.get('remember_me', '')
    try:
        if request.session['zone'] is '':  #當不勾選的時候,重新回到login會delete session   
           del request.session['zone']
           del request.session['account']
    except KeyError:
        a=''		
    if remember is '1': #按下記住我選項後
        request.session.set_expiry(1209600) # 2 weeks
        request.session['zone'] = "checked"
        request.session['account'] = username
    request.session['zone2']=remember  #此為在"原本有勾選的情況下,後來取消"的判斷
    user = auth.authenticate(username=username, password=password,remember=remember)
    if user is not None and user.is_active:
        auth.login(request, user)
        return render(request, 'home.html', {
        'psw':password 
    })
    else:
        if username is '' and password is '':	 #輸入不正確之訊息
         return render(request, 'login.html', {
		 're':""
         })
        else:	
         return render(request, 'login.html', {
		 're':"輸入不正確,請重新再試!"
         })         
def logout(request):
    username=request.user.username
    try:
        if request.session['zone2'] is "": #在取消"記住我"後的判斷
            request.session['zone']=""
            username=""
    except KeyError:
        a=''	
    try:
        remember = request.session['zone'] #取得在login時記載
    except KeyError:
        a=''
    auth.logout(request)
    request.session['zone'] = remember
    request.session['account'] = username
    return HttpResponseRedirect('/accounts/login')
