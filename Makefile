
run: image
	touch results.txt
	docker run --rm -it -e PYTHONUNBUFFERED=true -e AWS_DEFAULT_PROFILE=$${AWS_DEFAULT_PROFILE:-dev} -v `ls -d ~/.aws`:/root/.aws:ro -v `pwd`/results.txt:/code/results.txt:rw instance-ami-demo

image:
	docker build -t instance-ami-demo .


