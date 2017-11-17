
run: image
	docker run --rm -it instance-ami-demo
image:
	docker build -t instance-ami-demo .


