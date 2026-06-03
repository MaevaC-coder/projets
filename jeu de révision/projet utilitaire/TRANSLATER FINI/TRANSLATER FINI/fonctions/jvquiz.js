// Fonction qui donne les listes de mots traduits dans chaque langue respective
fetch('translation.csv')
                .then(response => response.text())
                .then(data => {
                    const lines = data.split('\n');
                    const list_fra = [];
                    const list_ang = [];
                    const list_esp = [];
                    const list_all = [];
 
                    lines.forEach(line => {
                        const colonnes= line.split(';');
                        if (colonnes.length >= 4) {
                            french_list.push(colonnes[0]);
                            english_list.push(colonnes[1]);
                            spanish_list.push(colonnes[2]);
                            german_list.push(colonnes[3]);
                        }
                    });
                })

function generation_mot(liste){
    /// rôle : donner un mot dans une liste au hasard
    /// entrées :  liste = list()
    /// retourne : str
    let ind = (int)(Math.random() * liste.size()); //on tire un index au hasard dans la liste
    return liste.get(ind); //on retourne le mot correspondant à l'index dans la liste
}

function qcm(liste_traduction,liste_revision){
    /// rôle : générer un un mot avec sa traduction de manière aléatoire
    /// entrées :  liste_traduction = list() , liste_revision = list()
    /// retourne : q = list()
    
    let q = new ArrayList();      //créer la liste q
    let mot = generation_mot(liste_revision); // on génère le mot
    q.add(mot);        //on ajoute le mot généré dans la liste q

    let co = liste_revision.indexOf(mot);
    let reponse = liste_traduction.get(co);          //depuis l'index récupéré du mot on prend son équivalent traduit
    q.add(reponse);                     //on ajoute le mot traduit à q

    return q;                             //on renvoie q
}

function quiz(liste_traduction){
    // rôle :créer les réponses du QCM
    // entrer : liste_traduction = liste avec tout les mots
    // sortie : liste_reponse = list()

    let qcm = qcm(liste_traduction,liste_revision); //le mot généré aléatoirement et sa bonne réponse dans une liste

    let liste_reponse = new ArrayList();     //on crée une nouvelle liste dans laquelle on mettra les réponses du qcm
    
    let r = (int)(Math.random() * 4);      //la position de la bonne réponse générée aléatoirement

    for (let i=0; i<4; i++ ){           //une boucle qui se produit 4 fois
        if (i == r){                                                  //si i est égale à la position de la bonne réponse
            liste_reponse.add(qcm.get(1));                          //on ajoute la bonne réponse dans la position
        }
        
        else{                                                       //dans le cas ou la position n'est pas celle de la bonne réponse
            let mauvais = generation_mot(liste_traduction);              //génère une mauvais réponse
            while (mauvais == qcm.get(1)){                                //tant que par mal chance le mot générer est le même que la bonne réponse
                mauvais = generation_mot(liste_traduction);         //regénère une mauvaise réponse
            }
            liste_reponse.add(mauvais);                        //on ajoute la mauvaise réponse à la valeur i, donc à la position actuel d'où l'on parcours la liste
        }
    }

    return liste_reponse;
}

function selbase(){
    /// rôle : donner la langue de base que l'on veut traduire
    /// entrer : None
    /// sortie : liste_reponse = list()

    let liste_l1 = document.getElementById("base"); // on va chercher la valeur de la liste déroulante que l'utilisateur a choisie pour la langue de base
    let valeur_l1 = liste_l1.options[liste_l1.selectedIndex].value;
    return "liste_" + valeur_l1.substring(0,4); // puis on retourne le nom de la liste de la langue choisie
}

function selentrainement(){
    // rôle : donner la langue avec laquelle langue on traduit le mot
    // entrer : None
    // sortie : liste_reponse = list()

    let liste_l2 = document.getElementById("entrainement"); // on va chercher la valeur de la liste déroulante que l'utilisateur a choisie pour la langue de traduction
    let valeur_l2 = liste_l2.options[liste_l2.selectedIndex].value;
    return "liste_" + valeur_l2.substring(0,4); // puis on retourne le nom de la liste de la langue choisie
}

let liste_traduction = selentrainement() // la langue de traduction
let liste_revision = selbase() // la langue de base que l'on traduit
