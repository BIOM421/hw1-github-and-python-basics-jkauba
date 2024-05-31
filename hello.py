def hello_world():
	return "Hello World!"

print(hello_world())

def hello_world_n(N):
	string = ''
	for i in range(N):
		string = string + 'Hello World!' + ' '
	return string

print(hello_world_n(5)) 