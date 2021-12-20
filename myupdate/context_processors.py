from myupdate.blog.models import Category, SubCategory


def global_context(request):
    cateogries = Category.objects.all()

    data = []
    for c in cateogries:
        sub = SubCategory.objects.filter(category=c)

        print(sub.values())

        sub_data = []

        if sub.count() > 0:
            for s in sub:
                print(s.get_absolute_url_sub)
                sub_data.append({
                    'name': s.name,
                    'slug': s.slug,
                    'get_absolute_url_sub': s.get_absolute_url_sub
                })

        data.append({
            'name': c.name,
            'slug': c.slug,
            'created_at': c.created_at,
            'submenu': sub_data,
            'id': c.id
        })
    context = {'category': data}
    return context