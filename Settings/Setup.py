import configparser
from doctest import Example
from operator import index
from Log import LogManager as lm

class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def create_table(self, table):
        self.config[table] = {}
        with open("./Settings/Setup.ini", "w", encoding="utf-8") as f:
            self.config.write(f)

    def read_setup(self, table):
        self.config.read('./Settings/Setup.ini', encoding='utf-8')

        key1 = None
        key2 = None
        val1_List = []
        val2_List = []

        try:
            data = self.config[table]
            if (table == "Language"):
                key1 = "lang_key"
                key2 = "lang_path"
            elif (table == "Field"):
                key1 = "field_key"
            elif (table == "Test_List"):
                key1 = "testlist_key"
            
            for key in data.keys():
                if key.find(key1) != -1:
                    print(f'key1 : {key}')
                    val1_List.append(data[key])
                elif key.find(key2) != -1:
                    print(f'key2 : {key}')
                    val2_List.append(data[key])
        except Exception as e:
            lm.Interupt()

        return val1_List, val2_List
        
        
    """
    ~# PYTHONIOENCODING=UTF-8
    
    for 문 안에서 호출 필요
    table : table 명
    val : 저장할 값 1
    val2 : 저장할 값 2
    * table명을 제외한 나머지 key값들은 소문자로만 저장되면 인식된다.
    """
    def write_setup(self, table, count, val, val2):

        key = None
        key2 = None

        if (table == "Language"):
            key = "lang_key"
            key2 = "lang_path"
        elif (table == "Field"):
            key = "field_key"
        elif (table == "Test_List"):
            key = "testlist_key"

        self.config[table].setdefault(f'{key}_{count + 1}', val)

        if (val2 != None):
            self.config[table].setdefault(f'{key2}_{count + 1}', val2)

        self.save_ini() 

    def clear_table(self, table):
        self.config[table].clear()
        self.save_ini()

    def save_ini(self):
        with open("./Settings/Setup.ini", "w", encoding="utf-8") as f:
            self.config.write(f)