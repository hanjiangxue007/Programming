#!/bin/bash

(latex -interaction nonstopmode -halt-on-error -file-line-error a.tex && dvipdf a.dvi; bibtex a ; latex -interaction nonstopmode -halt-on-error -file-line-error a.tex ; latex -interaction nonstopmode -halt-on-error -file-line-error a.tex ) || (pdflatex a.tex ; bibtex a ; pdflatex a.tex ; pdflatex a.tex ); rm -f a.aux ; rm -f a.bbl ; rm -f a.blg ; rm -f a.log ; rm -f a.out ; rm -f *.bak ; rm -r a.dvi ; find . -name *eps-converted* -type f -exec rm -r {} + ;xdg-open a.pdf


