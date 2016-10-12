FILES :=                              \
    app/models.py                     \
    app/tests.py                        \

.pylintrc:
	pylint --disable=bad-whitespace,missing-docstring,pointless-string-statement --reports=n --generate-rcfile > $@


models.html: app/models.py
	pydoc3 -w Netflix

IDB1.log:
	git log > IDB1.log

# netflix-tests:
# 	git clone https://github.com/CS373-Fall-2016/netflix-tests.git

# RunNetflix.tmp: RunNetflix.in RunNetflix.out RunNetflix.py
# 	-pylint Netflix.py
# 	-pylint RunNetflix.py
# 	./RunNetflix.py < RunNetflix.in > RunNetflix.tmp
# 	diff RunNetflix.tmp RunNetflix.out

# quick: RunNetflix.in RunNetflix.tmp RunNetflix.py
# 	./RunNetflix.py < RunNetflix.in > RunNetflix.tmp

# quick_probe: probe.tmp RunNetflix.py
# 	./RunNetflix.py < /u/downing/cs/netflix/probe.txt > probe.tmp

# TestNetflix.tmp: TestNetflix.py
# 	-pylint Netflix.py
# 	-pylint TestNetflix.py
# 	coverage-3.5 run    --branch TestNetflix.py >  TestNetflix.tmp 2>&1
# 	coverage-3.5 report -m                      >> TestNetflix.tmp
# 	cat TestNetflix.tmp

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

clean:
	rm -f  .coverage
	rm -f  *.pyc
	# rm -f  RunNetflix.tmp
	# rm -f  TestNetflix.tmp
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
	# rm -rf Netflix-tests

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: models.html IDB1.log check


