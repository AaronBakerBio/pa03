import pytest
import todolist


def test_add():
    todo = todolist.TodoList()
    
    todo.destroy_all()

    todo.add({'item #': 1, 'amount': 10.0, 'category': 'food', 'date': '2018-01-01', 'description': 'test'})
    assert todo.selectAll() == [{'item #': 1, 'amount': 10.0, 'category': 'food', 'date': '2018-01-01', 'description': 'test'}]
