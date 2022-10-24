# TP4-Mandelbrot
## Compte rendu du TP4 de PAPY
Ce TP consiste à générer des images d'ensembles de Mandelbrot et de Julia et à inscrire tout ça dans un environnement Python complet (documentation complète avec Sphinx, procédures de test avec pytest, parser, helper, etc.).

### Comment installer
`pip install -e .`

#### Pour utiliser la version Python 
Se placer dans le dossier `./src` et exécuter dans l'invité de commandes 

`python __main__.py [--mandelbrot | --julia] [--zmin ZMIN] [--zmax ZMAX] [--c C] [--pixel_size pixel_size] [--max_iter max_iter] [--output output]`

Les arguments sont les suivants : 
 * `-h`, `--help`            Pour afficher l'aide
 * `--mandelbrot`, `-m`      Pour traçer un ensemble de Mandelbrot. Exclusif avec --julia
 * `--julia`, `-j`          Pour traçer un ensemble de Mandelbrot. Exclusif avec --mandelbrot
 * `--zmin ZMIN`           Borne inférieure à traçer 
 * `--zmax ZMAX`           Borne supérieure à traçer
 * `--c C`                 Candidat de l'ensemble de Julia
 * `--pixel_size pixel_size`, `-ps pixel_size` Taille des pixels à dessiner
 * `--max_iter max_iter`, `-m_i max_iter` Nombre maximum d'itérations pour tester l'appartenance à un ensemble
 * `--output output`, `-o output` Nom de l'image à enregistrer

#### Pour utiliser le fichier exécutable 

TO DO

<p align="center"><img src="src/mandelbrot/results/fig_mandel.png" width="400" height="400"></p>
