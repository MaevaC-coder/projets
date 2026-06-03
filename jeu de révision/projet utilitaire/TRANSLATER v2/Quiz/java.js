// Fetch the translation CSV
fetch('translation.csv')
    .then(response => response.text())
    .then(data => {
        const lines = data.split('\n').slice(1); // Skip header if present
        const Français = [];
        const Anglais = [];
        const Espagnol = [];
        const Allemand = [];

        lines.forEach(line => {
            const columns = line.split(';');
            if (columns.length >= 4) {
                Français.push(columns[0]);
                Anglais.push(columns[1]);
                Espagnol.push(columns[2]);
                Allemand.push(columns[3]);
            }
        });

        // Use these lists for further processing
    })
    .catch(error => console.error('Error fetching CSV:', error));

function generation_mot(liste) {
    // Rôle : donner un mot dans une liste au hasard
    // Entrées : liste = list()
    // Retourne : str
    const ind = Math.floor(Math.random() * liste.length); //on tire un index au hasard dans la liste
    console.log(liste[ind]);
    return liste[ind]; //on retourne le mot correspondant à l'index dans la liste
}

function qcm(liste_traduction, liste_revision) {
    // Rôle : générer un mot avec sa traduction de manière aléatoire
    // Entrées : liste_traduction = list(), liste_revision = list()
    // Retourne : q = list()
    const q = []; // Créer la liste q
    const mot = generation_mot(liste_revision); // On génère le mot
    q.push(mot); // On ajoute le mot généré dans la liste q

    const co = liste_revision.indexOf(mot); 
    if (co !== -1) {
        const reponse = liste_traduction[co]; // Depuis l'index récupéré du mot, on prend son équivalent traduit
        q.push(reponse); // On ajoute le mot traduit à q
        console.log(q);
    } else {
        console.error("Mot non trouvé dans la liste de révision");
    }
    
    document.getElementById('mot').textContent = mot;
    return q; // On renvoie q
}

function quiz(liste_traduction, liste_revision) {
    // Rôle : créer les réponses du QCM
    // Entrer : liste_traduction = liste avec tous les mots
    // Sortie : liste_reponse = list()
    alert("marche");
    const q = qcm(liste_traduction, liste_revision); //le mot généré aléatoirement et sa bonne réponse dans une liste
    const liste_reponse = []; //on crée une nouvelle liste dans laquelle on mettra les réponses du qcm
    
    const r = Math.floor(Math.random() * 4); //la position de la bonne réponse générée aléatoirement

    for (let i = 0; i < 4; i++) { //une boucle qui se produit 4 fois
        if (i === r) { //si i est égal à la position de la bonne réponse
            liste_reponse.push(q[1]); //on ajoute la bonne réponse dans la position
        } else { //dans le cas où la position n'est pas celle de la bonne réponse
            let mauvais = generation_mot(liste_traduction); //génère une mauvaise réponse
            while (mauvais === q[1]) { //tant que par malchance le mot généré est le même que la bonne réponse
                mauvais = generation_mot(liste_traduction); //regénère une mauvaise réponse
            }
            liste_reponse.push(mauvais); //on ajoute la mauvaise réponse à la valeur i, donc à la position actuelle d'où l'on parcourt la liste
        }
    }

    return liste_reponse;
}

function openPage() {
    const revision = document.getElementById("base").value;
    const traduction = document.getElementById("entrainement").value;
    alert(revision + ", " + traduction);
    window.location.href = 'Quiz.html';
    quiz(traduction,revision);
}
