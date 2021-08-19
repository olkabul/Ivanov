build:
	docker build -t my_git .

run:
	docker run -it --rm my_git bash ./get_workdir.sh