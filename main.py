# homework_10
####################################################################
# Imports
from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

# Подключение Flask
app = Flask(__name__)

# Без этой штуки в файл json добавляются странные значения в выдачу
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def page_main():
    """Главная страница"""
    return f"<pre>{get_all()}<pre>"


@app.route('/candidates/<int:pk>')
def page_candidate(pk):
    """Поиск кандидата по PK"""
    return get_by_pk(pk)


@app.route('/skills/<skill_name>')
def page_skills(skill_name):
    """Подбор кандидатов по скиллам"""
    return f"<pre>{get_by_skill(skill_name)}<pre>"


app.run()

####################################################################
