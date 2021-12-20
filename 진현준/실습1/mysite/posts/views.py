from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import *

# Create your views here.

def index(request):
  return render(request,'posts/index.html')

def post_list(request):
  posts= Post.objects.all()
  ctx = {'posts': posts}
  return render(request, template_name='posts/list.html', context= ctx) #리퀘스트 받아서 저 탬플릿에 가공해서 씨티엑스 보내줌


def post_create(request):
  if request.method == 'POST':  #글 작성 눌렀을 때 오는 리퀘스트
    form = PostForm(request.POST) #포스트하면 아무거나 내용 적은 것들을 저장하는 폼이 된다
    if form.is_valid:
      form.save()
      return redirect('posts:list') #글 다 쓰면 이 포스트 리스트 유알엘로 넘어간다

  else:
    form = PostForm() #이건 겟방식 유엘알로 들가면 무조건 겟방식
    ctx = {'form': form} #ctx는 context의 약자로 볌수를 받아서 저장하는 통

    return render(request, template_name='posts/create.html', context=ctx) #저기서 폼을 넘겨주고 create html에서 폼을 테이블로 보여준다

def post_update(request, pk):
  post = get_object_or_404(Post, id=pk) #저거 겟 오프젝트 오어 404는 글목록에서 객체를 한 개만 갖고 온다는 의미. 없으면 404에러로 반환. 포스트 안에 있는 id가 pk인 객체 하나 
  # post = Post.objects.get(pk=pk) 위에랑 의미 비슷 포스트에서 pk 받아옴

  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid:
      form.save() #폼 변경저장
      return redirect('posts:list')

  form = PostForm(instance=post) #instance는 장고가 지정해준거고 우리가 만든 변수인 post가 담긴 form(글짓기 툴)을 받아서 그 폼을 갖고 온디 
  ctx = {'form':form}
#수정하기에서 수정 버튼을 눌러서 들어간거는 데이터의 변경 없이 url로 들어간거니까 get, post는 링크 타고 들어가서 실제로 데이터 수정이 이루어지면 그건 post 방식이라고 보면 된다. 결극 둘 다 요청이라는 큰 카테고리 안에서 데이터 변경여부로 바뀌는거임
  return render(request, template_name='posts/create.html', context=ctx)

def detail(request, pk):
  detail = get_object_or_404(Post, pk=pk)
  return render(request, 'posts/detail.html', {'post':detail}) #저거 포스트 디테일 의미가 뮈에요? posts로 하면 안 되고 post로 하면 되더라구요

def cat(request, pk):
  cat = Post.objects.get(id=pk)
  cat.delete()
  return redirect('posts:list')