from myupdate.blog.models import Menu, SubMenu


def global_context(request):
    menu = Menu.objects.all()

    data = []
    for c in menu:
        sub = SubMenu.objects.filter(category=c)

        print(sub.values())

        sub_data = []

        if sub.count() > 0:
            for s in sub:
                sub_data.append({
                    'name': s.name,
                    'slug': s.slug,
                })

        data.append({
            'name': c.name,
            'slug': c.slug,
            'submenu': sub_data,
            'id': c.id
        })
    context = {'category': data}
    return context