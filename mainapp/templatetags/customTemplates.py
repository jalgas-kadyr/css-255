from django import template

register = template.Library()


@register.simple_tag
def byIndex(list, x, y, *args, **kwargs):
    if list[x][y] == None:
        return None
    else:
        return list[x][y].name


def test(test):
    if test == None:
        return "test"
    else:
        return test
register.filter('test', test)
