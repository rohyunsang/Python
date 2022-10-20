def test_var_args(name, *args):
    print("첫 번째 인자",name)
    for arg in args:
        print("*args의 다른 인자",arg)


test_var_args("성정훈","단국대","jason")