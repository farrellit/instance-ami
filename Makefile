
run: image
	docker run --rm -it -e PYTHONUNBUFFERED=true -e AWS_DEFAULT_PROFILE=dev -v `ls -d ~/.aws`:/root/.aws:ro instance-ami-demo

image:
	docker build -t instance-ami-demo .


