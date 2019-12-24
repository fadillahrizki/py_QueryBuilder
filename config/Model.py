from config.Database import database,cursor

class Model:
    def __init__(self):
        self.table = ""
        self.cursor = cursor
        self.db = database

    # find data by id

    def find(self,id):
        self.query = f"select * from {self.table} where id={id}"
        self.cursor.execute(self.query)
        return self.cursor.fetchone()

    # get all data

    def get(self):
        self.query = f"select * from {self.table}"
        self.cursor.execute(self.query)
        return self.cursor.fetchall()

    def select(self):
        self.query = f"select * from {self.table}"
        return self

    # create data
    
    def create(self,data):
        key,value = "",''
        for k,v in data.items():
            if k == list(data)[len(data)-1]:
                key += k
                value += f"'{v}'"
            else:
                key += k+","
                value += f"'{v}',"
        self.query = f"insert into {self.table} ({key}) values ({value})"
        return self

    # update data

    def update(self,data):
        key,value = '',''
        for k,v in data.items():
            if k == list(data)[len(data)-1]:
                key += f"{k}"
                value += f"'{v}'"
            else:
                key += f""
        self.query = f"update {self.table} set key = 'value' where"
        return self

    # delete data

    def delete(self):
        self.query = f"delete from {self.table}"
        return self

    # add where query

    def where(self,key,operator,value=False):
        if value:
            if str.lower(operator) == 'in' or str.lower(operator) == 'not in':
                if len(list(value)) >= 1:
                    vals = ""
                    for v in value:
                        if v == value[len(value)-1]:
                            vals += f"'{v}'"
                        else:
                            vals += f"'{v}',"
                    self.query += f" where {key} {operator} ({vals})"
                else:
                    self.query += f" where {key} {operator} ('{value}')"
            elif str.lower(operator) == "like":
                self.query += f" where {key} {operator} '%{value}%'"
            else:    
                self.query += f" where {key} {operator} '{value}'"
        else:
            value = operator
            self.query += f" where {key}='{value}'"
        return self

    # add andwhere query

    def andwhere(self,key,operator,value=False):
        if value:
            self.query += f" and {key} {operator} '{value}'"
        else:
            value = operator
            self.query += f" and {key}='{value}'"
        return self

    # add orwhere query

    def orwhere(self,key,operator,value=False):
        if value:
            self.query += f" or {key} {operator} '{value}'"
        else:
            value = operator
            self.query += f" or {key}='{value}'"
        return self

    # add order query

    def orderby(self,val1,val2=False):
        self.query += f" order by {val1}"
        if val2:
            self.query += f" {val2}"
        return self

    # add limit query

    def limit(self,val1,val2=False):
        self.query += f" limit {val1}"
        if val2:
            self.query += f",{val2}"
        return self

    # fetch all data

    def all(self):
        self.cursor.execute(self.query)
        return self.cursor.fetchall()

    # fetch one data

    def one(self):
        self.cursor.execute(self.query)
        return self.cursor.fetchone()

    # execute query

    def execute(self):
        self.cursor.execute(self.query)
        self.db.commit()
        return self.cursor