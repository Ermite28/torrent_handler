# Cahier des charges
- Créer new torrent
    - Ajout dans bdd
    - Démarrer TorrentHandler
- Rechercher Torrent
- Mettre à jour Torrent
- Supprimer Torrent

 ## BDD interne
 - Nom
 - Magnet
 - Status 
 - 


## TorrentHandler
- Démarre téléchargement
- Vérifie le status
    - Change status bdd


Journal : 
Tout est bien mais problème de droits sur les fichiers : 

Faire docker-compose up 

pour logs

docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management