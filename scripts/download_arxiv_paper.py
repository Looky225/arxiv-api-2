import arxiv

paper = next(arxiv.Client().results(arxiv.Search(id_list=["1605.08386v1"])))
# Téléchargez le PDF dans le répertoire de travail avec un nom de fichier par défaut.
paper.download_pdf()
# Téléchargez le PDF dans le répertoire de travail avec un nom de fichier personnalisé.
paper.download_pdf(filename="downloaded-paper.pdf")
# Téléchargez le PDF dans un répertoire spécifié avec un nom de fichier personnalisé.
paper.download_pdf(dirpath="./mydir", filename="downloaded-paper.pdf")
