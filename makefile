DATE=`date -Iminutes`
MSG=$(DATE) - Automatic commit from build

all: build deploy commit

dev: build deploy

build:
	python build.py

deploy:
	sh deploy.sh

commit:
	git add .
	git commit -a -m "$(MSG)"

