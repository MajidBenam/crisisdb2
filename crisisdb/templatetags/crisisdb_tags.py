#from ..models import Agr_Prod_Pop
from atexit import register
from django import template

register = template.Library()


@register.simple_tag
def titleize(messy_title):
    tidy_title_list = []
    separate_words = messy_title.split("_")
    for word in separate_words:
        if len(word) >= 3:
            tidy_title_list.append(word.capitalize())
        else:
            tidy_title_list.append(word)
    return " ".join(tidy_title_list)
