def task_compile_pdf():
    latex_command = ['pdflatex', '-interaction=nonstopmode', '-output-directory=temp', 'timeinductivebias.tex']
    return {'actions': [latex_command,
                        ['bibtex', 'temp/timeinductivebias'],
                        latex_command,
                        latex_command],
            'file_dep': ['timeinductivebias.tex', 'background.tex', 'generalargument.tex', 'timeinductivebias.bib', 'mesaoptdiagram.pdf'],
            'targets': ['temp/timeinductivebias.pdf']}