from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.views.generic import FormView
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


def all_products(request):
    # View that shows ALL PRODUCTS, including sorting and search queries

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # Sorting for the all products search result
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
                """ sort by price descending """
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Search by category and urls
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            category = Category.objects.filter(name__in=categories)

        # Search by search bar
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(key_words__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # View that shows INDIVIDUAL PRODUCTS

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error('Only the store owner can access this function.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request,
                             'Product has been added to the database!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product. Double check the form.')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    # Edit a selected product
    if not request.user.is_superuser:
        messages.error('Only the store owner can access this function.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product details updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product. Double check the form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Editing: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    # Deletes a product from the database
    if not request.user.is_superuser:
        messages.error('Only the store owner can access this function.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


class ProductReview(FormView):
    """Displayed on product detail, used to add reviews"""
    template_name = 'products/product_detail.html'
    form_class = ReviewForm
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # make sure the user is logged in first
        if self.request.user.is_authenticated:
            # check to see if user has already posted review for product
            user_has_reviewed = Review.objects.filter(
                product=self.object).filter(user=self.request.user)
            # if no object was returned then user has not submitted a review
            if not user_has_reviewed:
                context['display_form'] = True

        # passthrough form for rendering in template
        context['form'] = ReviewForm()

        # get average review rating and pass through to template
        product_rating = Review.objects.filter(
            product=self.object).aggregate(Avg('rating'))

        context['product_rating'] = product_rating['rating__avg']
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        form = self.form_class(request.POST)

        # store the product id passed through the url(defined as pk in urls.py)
        self.pk = kwargs.get('pk')

        if form.is_valid():
            # foreign key objects not yet added, prevent saving and add them
            review = form.save(commit=False)
            review.product = get_object_or_404(Product, pk=product_id)
            review.user = self.request.user
            review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            messages.error(request,
                           'Failed to submit review. Please Double check your form.')

        return super().post(request, *args, **kwargs)
