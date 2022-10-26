# From Books:
# from django.shortcuts import render
# from .models import Book
#
# def HomeView(request):
#     return render(request, 'home/home.html')
#
# def ContactsView(request):
#     return render(request, 'contacts/contacts.html')
#
# def BlogView(request):
#     context = {
#         "books": Book.objects.all()
#     }
#     return render(request, 'blog/blogs.html', context)
#
# def Blog_detailView(request,num):
#     print(num)
#     context = {
#         'books': Book.objects.filter(book_id=num)
#     }
#     return render(request, 'blog/detail_blog.html', context)


# from Red_book:
# from django.shortcuts import render
# from .models import Red_book
#
# def ab(request):
#     context = {
#         'sinichky': Red_book.objects.all()
#     }
#     return render(request, 'base.html', context)

# #вьюха формы
# from django.shortcuts import render
# from .forms import MyForm
# from .models import MyModel
#
#
# def page1(request):
#     if request.method == 'POST':
#         # name = request.POST.get('name')
#         # age = request.POST.get('age')
#         form = MyForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             model1 = MyModel(surname=data['surname'], name=data['name'], age=data['age'])
#             model1.save()
#         # print(name)
#         # print(age)
#     else:
#         form = MyForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'base.html', context)

