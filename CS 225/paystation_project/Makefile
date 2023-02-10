# Very simple Makefile

help:
    echo target: tests clean_src

tests:
    python -m unittest

clean_src:
    rm -rf paystation/__pycache__
    find paystation -name '*~' -delete

clean_test:
    rm -rf test/__pycache__
    find paystation -name '*~' -delete

clean: clean_src clean_test
    find . - -name '*~' -delete

zip clean:
    zip -r paystation.zip paystation test makefile
    