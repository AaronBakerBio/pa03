import sqlite3
import os
import platform

def toDict(t):
    if len(t) == 1:
        return t[0]
    elif len(t) == 5:
        todo = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
        return todo


class TodoList():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS todo
                    ("item #" text, amount real, category text, date text, description text, completed int)''',())
        self.runQuery('''CREATE TABLE IF NOT EXISTS categories
                (category text)''',())
        
    def selectAll(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery('SELECT "item #", amount, category, date, description FROM todo', ())

    
    
    def add(self, item):
        '''Create a todo item and add it to the todo table. If it is a new category, add the category too'''
        category = item['category']
        self.add_category(category)
        return self.runQuery("INSERT INTO todo VALUES(?,?,?,?,?,?)",
                             (item['item #'], item['amount'], category, item['date'], item['description'], 0))

    
    def add_category(self, category):
        category_exists = self.runQuery("SELECT * FROM categories WHERE category=?", (category,))
        if not category_exists:
            self.runQuery("INSERT INTO categories(category) VALUES(?)", (category,))
            return False
        else:
            return True
            
    def selectCategories(self):
        ''' return all unique categories as a set.'''
        return self.runQuery("SELECT DISTINCT category FROM categories", (), True)
    
    def delete(self, item_num):
        ''' delete a todo item '''
        return self.runQuery("DELETE FROM todo WHERE [item #] = ?", (item_num,))

    def update_category(self, old_category, new_category):
        cursor = self.runQuery("UPDATE todo SET category=? WHERE category=?", (new_category, old_category))
        cursor = self.runQuery("UPDATE categories SET category=? WHERE category=?", (new_category, old_category), True)
        categories = self.selectCategories()

    
    def get_year(self):
        home_directory = None
        if platform.system() == 'Windows':
            home_directory = os.getenv('USERPROFILE')
        else:
            home_directory = os.getenv('HOME')
        con = sqlite3.connect(home_directory + '/todo.db')
        # con= sqlite3.connect(os.getenv('USERPROFILE')+'/todo.db')
        cur = con.cursor()     
        cur.execute("SELECT * FROM todo ORDER BY date", ())
        result = cur.fetchall()

        con.commit()
        con.close()
        return result

    def runQuery(self, query, tuple, category_query=False):
        '''Return results of query as a list of dicts.'''
        home_directory = None
        if platform.system() == 'Windows':
            home_directory = os.getenv('USERPROFILE')
        else:
            home_directory = os.getenv('HOME')
        con = sqlite3.connect(home_directory + '/todo.db')
        # con= sqlite3.connect(os.getenv('USERPROFILE')+'/todo.db')
        cur = con.cursor() 
        cur.execute(query, tuple)
        if category_query:
            results = cur.fetchall()
        else:
            results = cur.fetchall()
            results = [toDict(t) for t in results]
        con.commit()
        con.close()
        return results
