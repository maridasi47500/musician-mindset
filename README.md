# musician-mindset
musician mindset
🎵 Musician Flat
Une application Rails pour apprendre à hacker… la musique.
- demande à l'assistant Google
- 
- épelle Beethoven
- épelle Wolfgang Amadeus Mozart
- quand est ne Johann seBastian Bach
- quelles sont les œuvres de Antonio Vivaldi 

🚀 Présentation

Musician Flat est une application Ruby on Rails qui mélange deux univers :

    l’apprentissage du hacking mindset (comprendre, explorer, détourner, créer)

    la pratique musicale  dans l’entraînement musical

L’objectif est de proposer un espace où l’on peut :

    manipuler des données informatiques (tables, modèles, seeds techniques) sans être dangereux se 

    afficher des formats lisibles comme human_size(123) => 123 Bytes



    choisir un hobby dans un profil utilisateur (musique, sport, jeux vidéo, mode, etc.)

    écouter ou générer des pièces musicales : concertos, sonates, musique de chambre

🧠 Philosophie du projet

L’application repose sur une idée simple :

    Être un hacker, c’est comprendre comment les choses fonctionnent pour mieux créer. sans être dangereuse

Ici, on apprend à :

    manipuler des données

    structurer des modèles

    comprendre les formats



    créer de la musique comme un artisan numérique

🛠️ Stack technique

    Ruby on Rails (API + interface)

    PostgreSQL pour stocker les données musicales, techniques et utilisateurs

    ActiveRecord pour manipuler les tables

    Stimulus / Turbo pour dynamiser l’interface



📦 Fonctionnalités principales




    Entraînement sur des styles musicaux

    Accompagnement piano pour les instrumentistes
    aller au centre commercial

    collect technical terms

🧩 2. Tables techniques

Exemples de tables :

    computing_terms : données informatiques (RAM, CPU, formats, unités, etc.)

    musical_pieces : œuvres générées ou importées

    profiles : profils utilisateurs avec hobby

    hobbies : musique, sport, jeux vidéo, mode, etc.

📏 3. Helpers pratiques

Exemple :.human_size(123) # => "123 Bytes"

👤 4. Profils utilisateurs

Chaque utilisateur peut choisir un hobby :

    🎵 Musique

    🏀 Sport

    🎮 Jeux vidéo

    👗 Mode

    📚 Lecture

    etc.

📁 Exemple de structure de données
| Champ | Type | Description |
| --- | --- | --- |
| name | string | Nom du profil |
| hobby_id | integer | Référence vers un hobby |
| instrument | string | Instrument joué (optionnel) |

| Champ | Type | Description |
| --- | --- | --- |
| title | string | Nom de la pièce |
| style | string | concerto, sonate, chambre |
| ai_generated | boolean | Générée par IA |
| file_path | string | Lien vers le fichier audio |



