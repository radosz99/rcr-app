#  = = =   TARGETS   = = = >

build:
	docker build -t rcr-app .

run:
	docker run --name rcr-app -d -p 80:80 rcr-app

stop:
	docker stop rcr-app