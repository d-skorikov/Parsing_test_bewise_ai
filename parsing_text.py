import pandas as pd
#import numpy as np
#import re
#import fuzzywuzzy
#from fuzzywuzzy import process
#import chardet

dialog_reviews = pd.read_csv("/home/dn4k/spyder/Test_task_Bewise_ai/test_data.csv", index_col=False)
manager_pfrases=dialog_reviews.loc[dialog_reviews.role == 'manager']
num_dlg=dialog_reviews.dlg_id.nunique()

def hello (num):
    """функция выводит реплики с приветствием менеджера в зависимости от номера диалога"""
    any_manager_pfrases = manager_pfrases.loc[manager_pfrases.dlg_id == num]
    say_welcome= '(здравствуйте)|(здравствуйте)|(Добрый день)|(добрый)|(добрый день)|(Добрый)' 
    hell=any_manager_pfrases[any_manager_pfrases['text'].str.contains(say_welcome)]
    if hell.empty :
        hell="Менеджер не поприветствовал клиента"
    else:
            hell=hell.text.values[0]
    return hell

def acquaint (num):
    """возвращает фразу с представлением менеджера на основе шаблонных фраз"""
    say_name= '(меня)|(зовут)|(мое имя)|(это)'
    name_list='(ангелина)|(максим)|(анастасия)'
    any_manager_pfrases = manager_pfrases.loc[manager_pfrases.dlg_id == num]
    say_names=any_manager_pfrases[any_manager_pfrases['text'].str.contains(name_list)]
    acq=say_names[say_names['text'].str.contains(say_name)]
    if acq.empty :
        acq="Менеджер не представился"
    else:
        acq=acq.text.values[0]
    return acq
 
def name_of_manager (num):
    """возвращает имя менеджера после ключевых фраз"""
    say_name= '(меня)|(зовут)|(мое имя)|(это)'
    name_list='(ангелина)|(максим)|(анастасия)'
    any_manager_pfrases = manager_pfrases.loc[manager_pfrases.dlg_id == num]
    say_keyword=any_manager_pfrases[any_manager_pfrases['text'].str.contains(say_name)]
    name_manager= say_keyword.text.str.lower().str.extract(name_list,expand=True)
    frame_help=name_manager.dropna (axis=0,how='all')
    frame_help2=frame_help.dropna(axis='columns',how='any', inplace=False)
    if frame_help2.empty :
        name="Менеджер не представился"
    else:
        name=frame_help2.values[0]
    return name

def comp (num):
    """функция для вывода из фрейма строки названия компании по шаблонным словам в зависимости от номера диалога"""
    any_manager_pfrases = manager_pfrases.loc[manager_pfrases.dlg_id == num] 
    say_company = r'\b(диджитал бизнес) |\b(китобизнес) |\b(рога и копыта)'
    table_name_of_company= any_manager_pfrases.text.str.lower().str.extract(say_company,expand=True)
    frame_2=table_name_of_company.dropna (axis=0,how='all')
    frame_3=frame_2.dropna(axis='columns',how='any', inplace=False)
    if frame_3.empty :
        company="Менеджер не назвал компанию"
    else:
        company=frame_3.values[0]
    return company

def goodbye (num):
    """функция выводит реплики с прощанием менеджера в зависимости от номера диалога"""
    any_manager_pfrases = manager_pfrases.loc[manager_pfrases.dlg_id == num] 
    say_goodbye='(всего доброго)|(до свидания)|(доброго)|(пока)'
    goodbye_set=any_manager_pfrases[any_manager_pfrases['text'].str.lower().str.contains(say_goodbye)]
    if goodbye_set.empty :
        goodbye_set="Менеджер не попрощался"
    else:
            goodbye_set=goodbye_set.text.values[0]
    return goodbye_set

def hello_and_bye (num):
    """функция выводит True если было приветствие и прощание менеджера  и False в противном случае в зависимости от номера диалога"""
    any_manager_pfrases = manager_pfrases.loc[manager_pfrases.dlg_id == num] 
    say_goodbye='(всего доброго)|(до свидания)|(доброго)|(пока)'
    say_welcome= '(здравствуйте)|(здравствуйте)|(Добрый день)|(добрый)|(добрый день)|(Добрый)' 
    hello_goodbye=any_manager_pfrases[any_manager_pfrases['text'].str.lower().str.contains(say_goodbye)]
    hell=any_manager_pfrases[any_manager_pfrases['text'].str.lower().str.contains(say_welcome)]
    if ((hello_goodbye.empty) or (hell.empty)) :
        hello_good=False
    else:
            hello_good=True
    return hello_good

#name = manager_pfrases['text'].apply(lambda x: re.search(say_name, str(x).lower()))
#name_of_manager = dialog_reviews['text'].str.lower().str.extract(say_name)
#say_company = r'\b(диджитал бизнес) |\b(китобизнес) |\b(рога и копыта)'
#greeting=any_manager_pfrases.text.map(lambda x: x if re.search(say_company, str(x).lower()) != None else None )# возвращение строки с совпадением по названию компании
#true_greeting_string=greeting.loc[greeting.notnull()]
    
a = [i for i in range(num_dlg)]
result = pd.DataFrame({'say_hello': (a),'acquaintance': (a),'name_of_manager':(a),'company': (a),'say_bye':(a),'say_hello_and_bye':(a)})
for p in range(num_dlg) :
    result.say_hello[p]=hello(p) #
    result.acquaintance[p]=acquaint(p) #
    result.name_of_manager[p]=name_of_manager(p)#
    result.company[p]=comp(p) #
    result.say_bye[p]=goodbye(p)#
    result.say_hello_and_bye[p]=hello_and_bye(p)

result.to_csv('result.csv')

#file = open("male-names-v2-21904.txt")
#vals = []  # empty list
#with open('female-names-v2-16673.txt', 'r') as a_file:
#    for line in a_file:
#        line=line[:-1]
#        line=line.lower()
#        vals.append(line)
#val=')|('.join(vals) # добавление скобок ()|()|()
print(result)