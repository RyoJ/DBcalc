from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ANS
from .forms import ANSForm

#ANSES：一覧のためのモデルのリスト
#asn：編集のための任意のデータの変数

def index(request):
  d = {
      'ANSES': ANS.objects.all(),
  }
  return render(request, 'calc/index.html', d)

def add(request):
    form = ANSForm(request.POST or None)
    if form.is_valid():
      ANS.objects.create(**form.cleaned_data)
      return redirect('index')

    d = {
        'form': form,
    }
    return render(request, 'calc/edit.html', d)
    
def edit(request, editing_id):
    ans = get_object_or_404(ANS, id=editing_id)
    if request.method == 'POST':
        form = ANSForm(request.POST)
        if form.is_valid():
            ans.answer = form.cleaned_data['answer']
            ans.save()
            return redirect('index')
    else:
        # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
        form = ANSForm({'answer': ans.answer})
    d = {
        'form': form,
    }

    return render(request, 'calc/edit.html', d)

#@require_POST    
def delete(request, editing_id):
#    ans = get_object_or_404(ANS, id=editing_id)
#    ans.delete()
    return redirect('index')

def calc(request):
    #使用する値
    #form = ANSForm(request.POST or None)#ここで使用するformを定義
    rANS = ANS.objects.order_by('id').reverse()[:2]#過去2回分のレコードを抽出
    p1a = rANS[0].answer#1つ前の答え
    p2a = rANS[1].answer#2つ前の答え
    #計算
    if request.method == 'POST':#これをしないとcalc.htmlを開いたときに勝手にPOSTしようとする
        num = int(request.POST['num'])
        nans = p1a - num
    #答えを新しいレコードに記録
        ANS.objects.create(answer=nans)
        return redirect('index')
        
    d = {
        #'form': form,
        'p1a': p1a,
        'p2a': p2a,
    }
    return render(request, 'calc/calc.html', d)