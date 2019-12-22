LATEXFLAGS=\
	-interaction=nonstopmode \
	-halt-on-error \
	-file-line-error \
	-output-directory=../pdf

TEX_SOURCES=\
	commedia.tex \
	inferno.tex \
	$(wildcard inferno/*.tex) \
	purgatorio.tex \
	$(wildcard purgatorio/*.tex) \
	paradiso.tex \
	$(wildcard paradiso/*.tex)

PDFs=\
	../pdf/commedia-a4.pdf \
	../pdf/commedia-a4-hr.pdf \
	../pdf/commedia-a5.pdf \
	../pdf/commedia-a5-hr.pdf

.PHONY=all clean

all: $(PDFs)
	

../pdf/%.pdf: %.tex $(TEX_SOURCES)
	pdflatex $(LATEXFLAGS) $<
	pdflatex $(LATEXFLAGS) $<
	pdflatex $(LATEXFLAGS) $<

clean:
	rm -f ../pdf/commedia-{a4,a5}{,-hr}.{aux,log,out,toc}
