FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y tex-common texlive-base texlive-base-bin
  
RUN pip install --no-cache-dir super-latex-tool pdflatex

COPY main.py app/main.py

WORKDIR /app
CMD ["python", "main.py", "pdflatex", "output/generated_table_and_image.tex"]