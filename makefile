# getwd:
# 	cd .\Source

# print: 
# 	print(ls)

build:
	docker build -t my_git .

run:
		docker run -it --rm my_git bash -exec 'cd /dire/Ivanov/;python tests.py'
