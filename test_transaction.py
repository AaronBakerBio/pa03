import pytest
from transaction import TodoList


def test_add():
    todo = TodoList()
    todo.destroy_all()
    todo.add({'item #': 1, 'amount': 10.0, 'category': 'food', 'date': '2018-01-01', 'description': 'test'})
    assert([{'item #': '1', 'amount': 10.0, 'category': 'food', 'date': '2018-01-01', 'description': 'test'}] == todo.selectAll())
    todo.add({'item #': 2, 'amount': 30.0, 'category': 'food', 'date': '2019-01-01', 'description': 'test'})
    assert([{'item #': '1', 'amount': 10.0, 'category': 'food', 'date': '2018-01-01', 'description': 'test'}, {'item #': '2', 'amount': 30.0, 'category': 'food', 'date': '2019-01-01', 'description': 'test'}] == todo.selectAll())
    todo.destroy_all()
    assert(todo.selectAll() == [])

def test_delete():
    """Method to test the delete method from the transaction.py class"""
    todo = TodoList()
    todo.destroy_all()
    todo.delete(1)

@pytest.fixture
def todo_list():
    return TodoList()

def test_add_and_select_all(todo_list: TodoList):
    item = {'item #': '1', 'amount': 10, 'category': 'grocery', 'date': '2023-05-03', 'description': 'buy milk'}
    todo_list.add(item)
    result = todo_list.selectAll()
    assert len(result) == 1
    assert result[0] == item


def test_delete(todo_list: TodoList):
    item = {'item #': '1', 'amount': 10, 'category': 'grocery', 'date': '2023-05-03', 'description': 'buy milk'}
    todo_list.add(item)
    todo_list.delete(item['item #'])
    result = todo_list.selectAll()
    assert len(result) == 0


def test_destroy_all(todo_list: TodoList):
    item1 = {'item #': '1', 'amount': 10, 'category': 'grocery', 'date': '2023-05-03', 'description': 'buy milk'}
    item2 = {'item #': '2', 'amount': 20, 'category': 'stationery', 'date': '2023-05-04', 'description': 'buy pens'}
    todo_list.add(item1)
    todo_list.add(item2)
    todo_list.destroy_all()
    result = todo_list.selectAll()
    assert len(result) == 0


def test_update_category(todo_list: TodoList):
    old_category = 'grocery'
    new_category = 'supermarket'
    item = {'item #': '1', 'amount': 10, 'category': old_category, 'date': '2023-05-03', 'description': 'buy milk'}
    todo_list.add(item)
    todo_list.update_category(old_category, new_category)
    updated_item = todo_list.selectAll()[0]
    assert updated_item['category'] == new_category
    categories = todo_list.selectCategories()
    assert any(new_category in cat for cat in categories)
    assert not any(old_category in cat for cat in categories)

def test_get_date(todo_list: TodoList):
    item = {'item #': '1', 'amount': 10, 'category': 'grocery', 'date': '2023-05-03', 'description': 'buy milk'}
    todo_list.destroy_all()
    todo_list.add(item)
    date_count = todo_list.get_date(item['date'])
    assert date_count == 1

def test_add_category(todo_list: TodoList):
    category = 'utilities'
    todo_list.add_category(category)
    categories = todo_list.selectCategories()
    assert any(category in cat for cat in categories)


def test_select_categories(todo_list: TodoList):
    todo_list.destroy_all()
    todo_list.add_category('grocery')
    todo_list.add_category('stationery')
    todo_list.add_category('entertainment')
    categories = todo_list.selectCategories()
    assert len(categories) == 3
    assert ('grocery',) in categories
    assert ('stationery',) in categories
    assert ('entertainment',) in categories


def test_get_year(todo_list: TodoList):
    todo_list.destroy_all()
    item1 = {'item #': '1', 'amount': 10, 'category': 'grocery', 'date': '2022-05-03', 'description': 'buy milk'}
    item2 = {'item #': '2', 'amount': 20, 'category': 'stationery', 'date': '2023-05-04', 'description': 'buy pens'}
    item3 = {'item #': '3', 'amount': 30, 'category': 'entertainment', 'date': '2024-05-05', 'description': 'movie tickets'}
    todo_list.add(item1)
    todo_list.add(item2)
    todo_list.add(item3)
    results = todo_list.get_year()
    assert len(results) == 3
    assert results[0]['date'][:4] == '2022'
    assert results[1]['date'][:4] == '2023'
    assert results[2]['date'][:4] == '2024'
