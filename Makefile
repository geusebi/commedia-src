.PHONY: all clean clean-build text PDFs

all: text PDFs
	

text: book/commedia.txt
	

book/commedia.txt: script/to_text.py commedia.raw.text
	mkdir -p book
	python3 script/to_text.py commedia.raw.text > book/commedia.txt

PDFs:
	(cd latex_src; make)

clean-build:
	(cd latex_src; make clean-build)

clean:
	(cd latex_src; make clean)
	rm -f book/commedia.txt
