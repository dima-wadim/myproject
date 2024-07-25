import re
from django import template
from django.urls import reverse
from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    menu = Menu.objects.get(name=menu_name)
    items = menu.items.all()
    return {
        'menu': menu,
        'items': items,
        'current_url': current_url,
    }

def parse_url(url):
    if re.match(r'^https?://', url):
        return url
    try:
        return reverse(url)
    except:
        return url
