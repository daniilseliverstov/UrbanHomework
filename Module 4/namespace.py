def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
test_function()
# res = inner_function() скрыл коментарием, чтобы не выдавало ошибку

