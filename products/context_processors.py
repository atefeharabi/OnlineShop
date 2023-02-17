from .models import Product, Category


def categories(request):
    main = Category.objects.filter(is_sub=False)
    return {'main_categories': [
        {'name': main_category.name, 'url': main_category.get_absolute_url,
         'children': [{'name': child.name, 'url':child.get_absolute_url}
                        for child in Category.objects.filter(sub_category=main_category)
                      ]
         }
        for main_category in main
    ]
    }
