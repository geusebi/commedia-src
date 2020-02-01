.PHONY: all clean clean-build text PDFs

all: text HTML PDFs
	

text: book/commedia.txt
	

book/commedia.txt: script/to_text.py commedia.raw.text
	mkdir -p book
	python3 script/to_text.py commedia.raw.text > book/commedia.txt

HTML: book/commedia.html
	

book/commedia.html: script/to_html.py commedia.raw.text
	mkdir -p book
	python3 script/to_html.py commedia.raw.text > book/commedia.html

PDFs:
	mkdir -p book
	(cd latex_src; make)

clean-build:
	(cd latex_src; make clean-build)

clean:
	(cd latex_src; make clean)
	rm -f book/commedia.txt
