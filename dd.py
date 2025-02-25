def print_kwargs(**kwargs): # 딕셔너리 전용 가변 인자
	print(kwargs)
	
print_kwargs(name='foo', age=3, height=150)