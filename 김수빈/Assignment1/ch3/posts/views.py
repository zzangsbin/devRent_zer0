from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post # import 잊지 말기~!
# view가 원본이고 list.html은 그냥 보여주는 카피본 비슷한거라고 생각하면 됨

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts' : posts} # 초록색글씨는 그냥 이름이다... list.py 15행의 posts
    return render(request, 'posts/list.html', context=ctx)
    #return render(request, template_name='posts/list.html', context=ctx) 
    # 결국 같은 거임
    # views.py 자체가 보여주는 역할이고 여기 있는 함수? 들은 보여줄 내용들을 고르는거임

    # html파일을 만들기 위해서 posts 앱 내에 무조건!!! templates라는 이름의 폴더를
    # 만들어야됨. 글고 이 안에 또 애플리케이션이랑 동일한 이름의 폴더를 만들어줘야됨

def post_create(request): # 글 작성을 할 때
    form = PostForm(request.POST) # 씌여진 것을 지정된 형식 변수에 집어넣음! 사용자가 요청해서 POST형식으로 form이란것에 집어넣음
    # POST형식으로 받은 것을 담은 빈 양식이 PostForm임

    if form.is_valid(): # 지정된 형식이랑 같다면(유효하다면) 알아서 잘 형식마다 내용이 들어갔겠지??
        post = form.save() # 그럼 그대로 저장해
        return redirect('posts:list') # list url로 넘어가기
    else: # 근데 만약에 내가 쓴 글의 형식이랑 지정된 거랑 다르면 어긋날테니까 invalid 뜰거고
        form = PostForm() # Postform(request get) 빈 폼이라면 
        ctx = {'form' : form} # ctx에 빈 폼대로 저장되고 ctx에 넣어서 post/create.html에 넣음
    return render(request, template_name='posts/create.html', context=ctx)


def post_update(request, pk):
    post = Post.objects.get(pk=pk) # Post에 있는 객체들중에 하나만!! 가져와서 post라는 변수에 넣음
    # pk=pk는 그냥... 쓰는거래 
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) # instance는 장고에서 지정된 거고 이거 안 쓰면 PostForm은 그냥 비어있게됨
        if form.is_valid():
            post = form.save()
            return redirect('posts:list')
       
    # GET은 읽기나 쓰기같은거고 POST는 수정이나 어쩌고... https://noahlogs.tistory.com/35 여기 참조하자!
    else:
        form = PostForm(instance=post)
        ctx = {'form':form}
    return render(request, template_name='posts/create.html', context=ctx) # post/create.html을 가져옴, ctx를 가져옴
    # 들여쓰기 조심하자~!^^
    

def post_delete(request, pk):
    trash = Post.objects.get(pk=pk) # urls.py의 13행에서 내가 int:pk라고 해둬서...
    trash.delete()
    return redirect('posts:list')

def post_detail(request, pk): # 글 클릭하면 그거 하나만 불러오기!!!! template 하나 더 만들어야됨!!
    detail = Post.objects.get(pk=pk)    
    ctx = {'detail':detail}
    return render(request, 'posts/detail.html', context=ctx) 

# {} 는 1. context가 딕셔너리만 받아서 2. 'detail'은  detail.html에서 사용됨
# def post_detail(request, pk): # 글 클릭하면 그거 하나만 불러오기!!!! template 하나 더 만들어야됨!!
#     detail = Post.objects.get(pk=pk)   
#     return render(request, 'posts/detail.html', context=detail)