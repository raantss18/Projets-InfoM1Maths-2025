# Dynamic Programming: Application to Fibonacci Algorithm

_This course, written in LaTeX, introduce dynamic programming concept through Fibonacci algorithm using python._

## Requirements

- TeX Live or TeXstudio (recommended)
- python
- pygments (already included in TeXstudio)
```bash
pip install pygments
```

## Compilation

You must use the option `-shell-escape`.
```bash
pdflatex -shell-escape "dynamic_Fibonacci_algorithm".tex
```
If you are using TeXstudio, go to `Options > Configure TeXstudio > Commands` and modify the line **pdflatex** by :
```
pdflatex -synctex=1 -interaction=nonstopmode -shell-escape %.tex
```

After compilation, you will get a PDF file named *dynamic_Fibonacci_algorithm.pdf* and will be able to learn dynamic programming.

## License

This course use some contents from [Algorithms Notes for Professionals](https://goalkicker.com/AlgorithmsBook) book, released under Creative Commons BY-SA, and use this license too. 
