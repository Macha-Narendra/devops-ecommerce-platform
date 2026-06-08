from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from .models import Product
from .forms import ProductForm

from .decorators import admin_required

def product_list(request):

    search = request.GET.get("search", "")

    products = Product.objects.all()

    if search:

        products = products.filter(
            name__icontains=search
        )

    return render(
        request,
        "products/list.html",
        {
            "products": products,
            "search": search,
        }
    )

def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        "products/detail.html",
        {"product": product}
    )


@admin_required
def product_create(request):

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(
                commit=False
            )

            product.created_by = request.user

            product.save()

            return redirect(
                "product_list"
            )

    else:

        form = ProductForm()

    return render(
        request,
        "products/create.html",
        {"form": form}
    )

@admin_required
def product_update(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect(
                "product_detail",
                pk=product.pk
            )

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        "products/update.html",
        {
            "form": form,
            "product": product,
        }
    )

@admin_required
def product_delete(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    if request.method == "POST":

        product.delete()

        return redirect(
            "product_list"
        )

    return render(
        request,
        "products/delete.html",
        {"product": product}
    )


