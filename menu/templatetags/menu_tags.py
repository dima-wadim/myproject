from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return {'menu_items': menu_items, 'current_path': context['request'].path}
