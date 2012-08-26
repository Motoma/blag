DATE=`date -Iminutes`

all: build deploy commit

dev: build deploy

build:
	python build.py

deploy:
	sh deploy.sh

commit:
	git add .
	git commit -a -m "$(DATE) - Automatic commit from build" 
