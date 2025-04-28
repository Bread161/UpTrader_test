from django import template
from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('draw.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        items = MenuItem.objects.filter(menu=menu).select_related('parent').order_by('order')
    except Menu.DoesNotExist:
        items = []

    current_url = context['request'].path

    item_dict = {}
    for item in items:
        item_dict[item.id] = {
            'item': item,
            'children': [],
            'is_active': False,
            'is_open': False,
        }

    tree = []
    for item in items:
        if item.parent_id:
            item_dict[item.parent_id]['children'].append(item_dict[item.id])
        else:
            tree.append(item_dict[item.id])

    def mark_active(nodes):
        for node in nodes:
            if node['item'].get_url() == current_url:
                node['is_active'] = True
                parent_id = node['item'].parent_id
                while parent_id:
                    parent_node = item_dict.get(parent_id)
                    if parent_node:
                        parent_node['is_open'] = True
                        parent_id = parent_node['item'].parent_id
                    else:
                        break
            mark_active(node['children'])

    mark_active(tree)

    return {'menu_tree': tree}
