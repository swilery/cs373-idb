FILES :=                              \
	makefile							\
	.gitignore							\
	models.html							\
	IDB1.log 							\
	UML.pdf								\
	apiary.apib							\
	.travis.yml							\
    app/models.py                     	\
    app/tests.py                        \

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

.pylintrc:
	pylint --disable=bad-whitespace,missing-docstring,pointless-string-statement --reports=n --generate-rcfile > $@

models.html: 
	#app/models.py
	#rm models.html
	cp app/models.py ./ && cp app/loader.py ./
	cd app
	pydoc3 -w models
	cd ..
	#rm models.py && rm loader.py

log:
	git log > IDB2.log

# TestIDB.tmp: app/tests.py
# 	-pylint app/models.py
# 	-pylint app/tests.py
# 	coverage-3.5 run    --branch app/tests.py >  app/tests.tmp 2>&1
# 	coverage-3.5 report -m                      >> app/tests.tmp
# 	cat tests.tmp

requirements:
	pip install -r requirements.txt

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  tests.tmp
	rm -rf __pycache__

config:
	git config -l

format:
	autopep8 -i app/models.py
	autopep8 -i app/tests.py

scrub:
	make clean
	rm -f  models.html
	rm -f  IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: models.html IDB1.log check 

# add TestIDB to test for next phase


