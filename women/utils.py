from .models import Category

menu = [{'title': 'Home Womens', 'url_name': 'home'},
        {'title': 'Create article', 'url_name': 'add_page'}]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
