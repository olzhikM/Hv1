from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница
def home(request):
    return redirect('threads')

# Список потоков
def thread_list(request):
    query = request.GET.get('q', '')  # Получаем значение из строки запроса
    if query:
        threads = Thread.objects.filter(name__icontains=query)  # Фильтруем темы по названию
    else:
        threads = Thread.objects.all()

    return render(request, 'post/thread_list.html', {'threads': threads, 'query': query})

# Детали потока и создание поста
def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()
    return render(request, 'post/thread_detail.html', {
        'thread': thread,
        'posts': posts
    })


# Удаление потока
def delete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('threads')

# Редактирование потока
def edit_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/edit_thread.html', {'form': form})

# Удаление поста
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

# Редактирование поста
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit_post.html', {'form': form})
