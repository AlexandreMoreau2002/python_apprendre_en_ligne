"""
create_python_files script

rendre le fichier executable :
$ chmod +x cpf.zsh

"""

#!/bin/zsh

for i in {1..9}
do
   # Création du fichier Python avec le nom correspondant
   touch "1.$i.py"
done
