# Imports
import json


def load_candidates():
    """Загружает данные из json файла"""
    with open('candidates.json', 'r', encoding='UTF') as file:
        candidates = json.load(file)
        return candidates


def get_all():
    """Вывод всех кандидатов"""
    return "\n\n".join(
        ["\n".join([candidate['name'], candidate['position'], candidate['skills']]) for candidate in load_candidates()])


def get_by_pk(pk):
    """Находит кандидата по PK"""
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            url_pictures = candidate['picture']
            return f"<pre><img src='{url_pictures}'<pre>" \
                   f"<pre>{candidate['name']}\n" \
                   f"{candidate['position']}\n" \
                   f"{candidate['skills']}<pre>"
        # else:
        #     return "Кандидат не найден" - Если подключить else,  то кандидат всегда не найден


def get_by_skill(skill_name):
    """Находит кандидатов по скиллам"""
    candidates = ''
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates += "\n".join([candidate['name'], candidate['position'], candidate['skills']]) + "\n\n"
    return candidates
