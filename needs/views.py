from django.shortcuts import render
from django.shortcuts import redirect
from .forms import AddItem
from .models import Item


# Create your views here.
def main_page(request):
    if request.user.is_authenticated:
        errors = []
        form = AddItem(request.POST or None)
        if form.is_valid():
            new_item = Item(description=form.cleaned_data.get("item_name"), author=request.user)
            def check_slash(string):
                first_slash = string.find('/')
                last_slash = string.rfind('/')
                return [first_slash+1:last_slash]
            out_put = check_slash(form.cleaned_data.get("item_name"))
            try:
                new_item.save()
            except Exception as e:
                errors.append(e)
        context = {
            "items": Item.objects.all(),
            "user": request.user,
            "form": form,
            "errors": errors,
            "out_put": out_put,
        }
        return render(request, 'index.html', context)
    else:
        return redirect('/login')
