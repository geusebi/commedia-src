LATEXFLAGS=\
	-interaction=nonstopmode \
	-halt-on-error \
	-file-line-error \
	-output-directory=../book

TEX_SOURCES=\
	commedia.tex \
	inferno.tex \
	$(wildcard inferno/*.tex) \
	purgatorio.tex \
	$(wildcard purgatorio/*.tex) \
	paradiso.tex \
	$(wildcard paradiso/*.tex) \
	setup.tex

PDFs=\
	../book/commedia-a4.pdf \
	../book/commedia-a4-hr.pdf \
	../book/commedia-a5.pdf \
	../book/commedia-a5-hr.pdf

.PHONY: all clean clean-build

all: $(PDFs)
	

../book/%.pdf: %.tex $(TEX_SOURCES)
	pdflatex $(LATEXFLAGS) $<
	pdflatex $(LATEXFLAGS) $<
	pdflatex $(LATEXFLAGS) $<

$(TEX_SOURCES): ../script/to_latex.py ../commedia.raw.text
	mkdir -p {inferno,purgatorio,paradiso}
	python3 ../script/to_latex.py ../commedia.raw.text .

clean-build:
	rm -f ../book/commedia-{a4,a5}{,-hr}.{aux,log,out,toc}

clean:
	rm -rf {inferno,purgatorio,paradiso}
	rm -f {inferno.tex,purgatorio.tex,paradiso.tex}
	rm -f ../pdf/commedia-{a4,a5}{,-hr}.{aux,log,out,toc}
	rm -f $(PDFS)
