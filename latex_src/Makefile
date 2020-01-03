LATEXFLAGS=\
	-interaction=nonstopmode \
	-halt-on-error \
	-file-line-error \
	-output-directory=../book

TEX_SOURCES=\
	commedia.tex \
	inferno.tex \
	purgatorio.tex \
	paradiso.tex \
	parsejobname.tex \
	setup.tex \
	metadata.tex

PDFs=\
	../book/commedia-a4.pdf \
	../book/commedia-a4-hr.pdf \
	../book/commedia-a4-num.pdf \
	../book/commedia-a4-hr-num.pdf \
	../book/commedia-a5.pdf \
	../book/commedia-a5-hr.pdf \
	../book/commedia-a5-num.pdf \
	../book/commedia-a5-hr-num.pdf

.PHONY: all clean clean-build

all: $(PDFs)
	

../book/%.pdf: $(TEX_SOURCES)
	mkdir -p ../book
	pdflatex -jobname $(patsubst ../book/%.pdf,%,$@) $(LATEXFLAGS) commedia.tex
	pdflatex -jobname $(patsubst ../book/%.pdf,%,$@) $(LATEXFLAGS) commedia.tex
	pdflatex -jobname $(patsubst ../book/%.pdf,%,$@) $(LATEXFLAGS) commedia.tex

$(TEX_SOURCES): ../script/to_latex.py ../commedia.raw.text
	mkdir -p {inferno,purgatorio,paradiso}
	python3 ../script/to_latex.py ../commedia.raw.text .
	touch $(TEX_SOURCES)

clean-build:
	rm -f ../book/commedia-{a4,a5}{,-hr}{,-num}.{aux,log,out,toc}

clean:
	rm -rf {inferno,purgatorio,paradiso}
	rm -f {inferno.tex,purgatorio.tex,paradiso.tex}
	rm -f ../book/commedia-{a4,a5}{,-hr}{,-num}.{aux,log,out,toc}
	rm -f $(PDFs)

