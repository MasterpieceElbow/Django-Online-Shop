from django import template
from ..forms import SearchForm

register = template.Library()


@register.inclusion_tag('shop/search/search_base.html')
def search_field():
    form = SearchForm()
    return {'form': form}
