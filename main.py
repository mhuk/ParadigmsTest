import re
import os
import datetime

global no_category
global wrong_value
global no_file
global add_correct
global dict_summary
global dict_month

wrong_value = "Not correct value."
no_category = "Category doesn't exist."
no_file = "File not found."
add_correct = "Successfully added"
rm_correct = "Successfully removed"
dict_summary = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [],
                     9: [], 10: [], 11: [], 12: []}
dict_month = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [],
                   9: [], 10: [], 11: [], 12: []}
class CategoryManager:

    def __init__(self):
        self.file_name = "CategoriesList.txt"
        self.add_cat = 1
        self.remove_cat = 2
        self.get_cat = 3
        self.exit = 4
        self.min_size = 2

    def get_categories(self):
        """Return list of categories"""
        if os.path.isfile(self.file_name) :
            text = open(self.file_name, "r+")
            r_categories = text.read()
            categories = re.split(r'[,\s]*', r_categories)
            text.close()
            return categories
        else:
            print(no_file)

    def add_category(self):
        """Add category to CategoriesList"""
        category_name = input("Enter a new category")
        if category_name in self.get_categories():
            print("Category already exist")
        else:
            cat = open(self.file_name, 'a')
            cat.write("\n")
            cat.write(category_name)
            cat.close()
            print(add_correct)

    def remove_category(self):
        """Remove category from CategoriesList"""
        statinfo = os.stat(self.file_name)
        if statinfo.st_size > self.min_size:
            category_name = input("Enter category to remove")
            if category_name not in self.get_categories():
                print(no_category)
            else:
                f = open(self.file_name, "r+")
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != category_name + '\n' and i != category_name:
                        f.write(i)
                f.truncate()
                f.close()
                print(rm_correct)
        else:
            print("File is empty")

    def menu(self):
        text_menu = """ 
                Press 1 if you want to add category
                Press 2 if you want to remove category
                Press 3 if you want to see categories
                Press 4 if you want to exit from edit
                """
        while True:
            choose = int(input(text_menu))
            if choose == self.add_cat:
                self.get_categories()
                self.add_category()
            elif choose == self.remove_cat:
                self.remove_category()
            elif choose == self.get_cat:
                for category in self.get_categories():
                    print(category)
            elif choose == self.exit:
                print("Exit from editor")
                break
            else:
                print(wrong_value)


class ExpenseManager:

    def __init__(self):
        self.add_exp = 1
        self.remove_exp = 2
        self.get_exp_month = 3
        self.get_exp_cat = 4
        self.exit = 5
        self.min_year = 2016
        self.max_year = 2050

    def menu(self):
        text_menu = """ 
                        Press 1 if you want to add expense
                        Press 2 if you want to remove expense
                        Press 3 if you want to see expenses by a month
                        Press 4 if you want to show expenses by a category
                        Press 5 if you want to exit expense manager
                        """
        while True:
            choose = int(input(text_menu))
            if choose == self.add_exp:
                self.add_expense()
            elif choose == self.remove_exp:
                self.remove_expense_date()
            elif choose == self.get_exp_month:
                txt = self.print_expenses_by_month()
                print(txt)
            elif choose == self.get_exp_cat:
                txt = self.print_expenses_by_category()
                print(txt)
            elif choose == self.exit:
                print("Exit")
                break
            else:
                print(wrong_value)

    def add_expense(self):
        """Add new expense to file as a year"""
        year, month, day = self.date_expense()
        name, amount = self.detail_expense()
        file_name = str(year) + '.txt'
        try:
            add_e = open(file_name, 'a')
            add_e.write("\n")
            content_of_expense = year,month, day, name, amount
            str_content = str(content_of_expense)
            add_e.write(str_content)
            add_e.close()
            print(add_correct)
        except (IOError, TypeError,ValueError):
            print(no_file)

    def remove_expense_date(self):
        year, month, day = self.date_expense()
        name, amount = self.detail_expense()
        content_of_expense = year, month, day, name, amount
        str_content = str(content_of_expense)
        file_name = str(year) + '.txt'
        if os.path.isfile(file_name):
            f = open(file_name, "r+")
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i != str_content + '\n' and i != str_content:
                    f.write(i)
            f.truncate()
            f.close()
            print(rm_correct)
        else:
            print(no_file)

    def format_txt(self,con_list):
        """Return formatted list"""
        formatted_list = con_list.replace('\'', ' ').replace( '(', ' ').replace(')', ' ')
        return formatted_list

    def print_expenses_by_month(self):
        """Show expenses in year by a month"""
        while True:
            f = file_object.open_file()
            if f is None:
                print(wrong_value)
            else:
                break
        month = input("Enter a month")
        s_month = ' '+month
        find = ""
        for line in f:
            r_line = line.replace("(", " ")
            rr_line = r_line.replace(")", " ")
            n_line = rr_line.replace("\n", " ")
            list_line = n_line.split(",")
            for i, n in enumerate(list_line):
                if i == 1:
                    a = (''.join(map(str, n)))
                    if a == s_month:
                        find += line
        return self.format_txt(find)

    def print_expenses_by_category(self):
        """Show expenses in year by a category"""
        while True:
            f = file_object.open_file()
            if f is None:
                print(wrong_value)
            else:
                break
        category = self.get_category()
        new_list = []
        for line in f:
            if category in line:
                new_list.append(line)
        r_list = ' '.join(map(str, new_list))
        return self.format_txt(r_list)

    def date_expense(self):
        """Return year, month, day"""
        while True:
            year = int(input("Enter a year"))
            if year >= self.min_year and year <= self.max_year:
                month = int( input("Enter a month"))
                day = int( input("Enter a day"))
                datetime.datetime(year=year, month=month, day=day)
                return year, month, day
            else:
                print(wrong_value)

    def detail_expense(self):
        """Return name and amount of expense """
        name = self.get_category()
        amount = float(input("Enter an amount of expense"))
        return name, amount

    def get_category(self):
        """Return name of category"""
        name = input("Enter a name of category")
        if name not in category_object.get_categories():
            print(no_category)
        else:
            return name

class Menu:

    def __init__(self):
        self.manage_cat = 1
        self.manage_exp = 2
        self.manage_exit = 3


    def menu_content(self):
        while True:
            print("""
                    1.Press 1 If you want to Manage of Category
                    2.Press 2 If you want to Manage to expense 
                    3.Press 3 Exit from Manager
                    """)
            self.choose = input("Enter a number")
            try:
                if int(self.choose) == self.manage_cat:
                    category_object.menu()
                elif int(self.choose) == self.manage_exp:
                    expense_object.menu()
                elif int(self.choose) == self.manage_exit:
                    print("Exit")
                    break
                else:
                    print(wrong_value)
            except(ValueError, TypeError):
                print(wrong_value)

class FileManager():

    def open_file(self):
        """Return content of file"""
        year = int(input("Enter a year"))
        file_name = str(year) + '.txt'
        if os.path.isfile(file_name):
            f = open(file_name, "r+")
            return f
        else:
            print(no_file)

if __name__ == "__main__":
    category_object = CategoryManager()
    expense_object = ExpenseManager()
    file_object = FileManager()
    menu_object = Menu()
    menu_object.menu_content()




