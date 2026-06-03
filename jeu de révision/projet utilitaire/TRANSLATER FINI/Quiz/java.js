const Français = ['Français', 'Bonjour', 'Merci', 'Amour', 'Chat', 'Chien', 'Maison', 'Voiture', 'ecole', 'Livre', 'Pomme', 'Eau', 'Soleil', 'Lune', 'ete', 'Hiver', 'Printemps', 'Automne', 'Neige', 'Pluie', 'Vent', 'Temps', 'Jour', 'Nuit', 'Heure', 'Minute', 'Seconde', 'Ville', 'Village', 'Pays', 'Montagne', 'Mer', 'Rivière', 'Lac', 'Forêt', 'Arbre', 'Fleur', 'Jardin', 'Route', 'Rue', 'Voie', 'Pont', 'Bateau', 'Avion', 'Train', 'Bus', 'Velo', 'Moto', 'Travail', 'Employe', 'Patron', 'Vendeur', 'Client', 'Bureau', 'Ordinateur', 'Telephone', 'Tablette', 'Internet', 'Email', 'Lettre', 'Timbre', 'Boîte', 'Cadeau', 'Anniversaire', 'Fête', 'Mariage', 'Naissance', 'Mort', 'Ami', 'Enfant', 'Adulte', 'Femme', 'Homme', 'Fille', 'Garçon', 'Mère', 'Père', 'Frère', 'Sœur', 'Oncle', 'Tante', 'Cousin', 'Grand-mère', 'Grand-père', 'Chaud', 'Froid', 'Doux', 'Amer', 'Sale', 'Acide', 'Beau', 'Moche', 'Grand', 'Petit', 'Long', 'Court', 'Lourd', 'Leger', 'Rapide', 'Lent', 'Heureux', 'Triste', 'Facile', 'Difficile', 'Fort', 'Faible', 'Lumière', 'Ombre', 'Clair', 'Sombre', 'Propre', 'Sale', 'Nouveau', 'Vieux', 'Jeune', 'Âge', 'Fort', 'Silencieux', 'Sec', 'Humide', 'Correct', 'Incorrect', 'Verite', 'Mensonge', 'Riche', 'Pauvre', 'Large', 'etroit', 'Haut', 'Bas', 'Dur', 'Mou', 'Rond', 'Carre', 'Bon', 'Mauvais', 'Fort', 'Faible', 'Gauche', 'Droite', 'Longueur', 'Largeur', 'Hauteur', 'Profondeur', 'Terre', 'Ciel', 'Feu', 'Eau', 'Air', 'Vent', 'Roche', 'Sable', 'Neige', 'Glace', 'Tempête', 'Pluie', 'Nuage', 'Foudre', 'eclair', 'Tonnerre', 'Planète', 'etoile', 'Galaxie', 'Univers', 'Soleil', 'Lune', 'Mars', 'Venus', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Pluton', 'Astronaute', 'Satellite', 'Comète', 'Meteorite', 'Telescope', 'Mecanique', 'Ingenieur', 'Architecte', 'Constructeur', 'Pilote', 'Conducteur', 'Chirurgien', 'Medecin', 'Infirmière', 'Dentiste', 'Pharmacien', 'Veterinaire', 'Enseignant', 'Professeur', 'etudiant', 'ecolier', 'Policier', 'Pompier', 'Soldat', 'Marin', 'Aviateur', 'Mecanicien', 'electricien', 'Plombier', 'Charpentier', 'Maçon', 'Jardinier', 'Cuisinier', 'Serveur', 'Serveuse', 'Boucher', 'Boulanger', 'Pâtissier', 'Artisan', 'Artiste', 'Peintre', 'Sculpteur', 'Musicien', 'Chanteur', 'Compositeur', 'ecrivain', 'Poète', 'Journaliste', 'Reporter', 'Photographe', 'Cineaste', 'Acteur', 'Actrice', 'Danseur', 'Choregraphe', 'Realisateur', 'Producteur', 'Technicien', 'Informatique', 'Programmeur', 'Analyste', 'Specialiste', 'Consultant', 'Entrepreneur', 'Chef', 'Directeur', 'Cadre', 'President', 'Ministre', 'Depute', 'Senateur', 'Gouverneur', 'Maire', 'Conseiller', 'Diplomate', 'Ambassadeur', 'Consul', 'Avocat', 'Juge'];
const Anglais = ['Anglais', 'Hello', 'Thank you', 'Love', 'Cat', 'Dog', 'House', 'Car', 'School', 'Book', 'Apple', 'Water', 'Sun', 'Moon', 'Summer', 'Winter', 'Spring', 'Fall', 'Snow', 'Rain', 'Wind', 'Time', 'Day', 'Night', 'Hour', 'Minute', 'Second', 'City', 'Village', 'Country', 'Mountain', 'Sea', 'River', 'Lake', 'Forest', 'Tree', 'Flower', 'Garden', 'Road', 'Street', 'Lane', 'Bridge', 'Boat', 'Plane', 'Train', 'Bus', 'Bicycle', 'Motorcycle', 'Work', 'Employee', 'Boss', 'Seller', 'Customer', 'Office', 'Computer', 'Phone', 'Tablet', 'Internet', 'Email', 'Letter', 'Stamp', 'Box', 'Gift', 'Birthday', 'Party', 'Wedding', 'Birth', 'Death', 'Friend', 'Child', 'Adult', 'Woman', 'Man', 'Girl', 'Boy', 'Mother', 'Father', 'Brother', 'Sister', 'Uncle', 'Aunt', 'Cousin', 'Grandmother', 'Grandfather', 'Hot', 'Cold', 'Sweet', 'Bitter', 'Salty', 'Sour', 'Beautiful', 'Ugly', 'Big', 'Small', 'Long', 'Short', 'Heavy', 'Light', 'Fast', 'Slow', 'Happy', 'Sad', 'Easy', 'Difficult', 'Strong', 'Weak', 'Light', 'Shadow', 'Clear', 'Dark', 'Clean', 'Dirty', 'New', 'Old', 'Young', 'Old', 'Loud', 'Quiet', 'Dry', 'Wet', 'Right', 'Wrong', 'Truth', 'Lie', 'Rich', 'Poor', 'Wide', 'Narrow', 'High', 'Low', 'Hard', 'Soft', 'Round', 'Square', 'Good', 'Bad', 'Strong', 'Weak', 'Left', 'Right', 'Length', 'Width', 'Height', 'Depth', 'Earth', 'Sky', 'Fire', 'Water', 'Air', 'Wind', 'Rock', 'Sand', 'Snow', 'Ice', 'Storm', 'Rain', 'Cloud', 'Lightning', 'Flash', 'Thunder', 'Planet', 'Star', 'Galaxy', 'Universe', 'Sun', 'Moon', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Astronaut', 'Satellite', 'Comet', 'Meteorite', 'Telescope', 'Mechanic', 'Engineer', 'Architect', 'Builder', 'Pilot', 'Driver', 'Surgeon', 'Doctor', 'Nurse', 'Dentist', 'Pharmacist', 'Veterinarian', 'Teacher', 'Professor', 'Student', 'Schoolboy', 'Policeman', 'Firefighter', 'Soldier', 'Sailor', 'Aviator', 'Mechanic', 'Electrician', 'Plumber', 'Carpenter', 'Mason', 'Gardener', 'Cook', 'Waiter', 'Waitress', 'Butcher', 'Baker', 'Pastry Chef', 'Craftsman', 'Artist', 'Painter', 'Sculptor', 'Musician', 'Singer', 'Composer', 'Writer', 'Poet', 'Journalist', 'Reporter', 'Photographer', 'Filmmaker', 'Actor', 'Actress', 'Dancer', 'Choreographer', 'Director', 'Producer', 'Technician', 'Computer Science', 'Programmer', 'Analyst', 'Specialist', 'Consultant', 'Entrepreneur', 'Chief', 'Director', 'Executive', 'President', 'Minister', 'Deputy', 'Senator', 'Governor', 'Mayor', 'Counselor', 'Diplomat', 'Ambassador', 'Consul', 'Lawyer', 'Judge'];
const Espagnol = ['Espagnol', 'Hola', 'Gracias', 'Amor', 'Gato', 'Perro', 'Casa', 'Coche', 'Escuela', 'Libro', 'Manzana', 'Agua', 'Sol', 'Luna', 'Verano', 'Invierno', 'Primavera', 'Otono', 'Nieve', 'Lluvia', 'Viento', 'Tiempo', 'Día', 'Noche', 'Hora', 'Minuto', 'Segundo', 'Ciudad', 'Pueblo', 'País', 'Montana', 'Mar', 'Río', 'Lago', 'Bosque', 'arbol', 'Flor', 'Jardín', 'Carretera', 'Calle', 'Callejón', 'Puente', 'Barco', 'Avión', 'Tren', 'Autobús', 'Bicicleta', 'Motocicleta', 'Trabajo', 'Empleado', 'Jefe', 'Vendedor', 'Cliente', 'Oficina', 'Computadora', 'Telefono', 'Tableta', 'Internet', 'Correo\xa0electrónico', 'Carta', 'Sello', 'Caja', 'Regalo', 'Cumpleanos', 'Fiesta', 'Boda', 'Nacimiento', 'Muerte', 'Amigo', 'Nino', 'Adulto', 'Mujer', 'Hombre', 'Nina', 'Nino', 'Madre', 'Padre', 'Hermano', 'Hermana', 'Tío', 'Tía', 'Primo', 'Abuela', 'Abuelo', 'Caliente', 'Frío', 'Dulce', 'Amargo', 'Salado', 'Agrio', 'Hermoso', 'Feo', 'Grande', 'Pequeno', 'Largo', 'Corto', 'Pesado', 'Ligero', 'Rapido', 'Lento', 'Feliz', 'Triste', 'Facil', 'Difícil', 'Fuerte', 'Debil', 'Luz', 'Sombra', 'Claro', 'Oscuro', 'Limpio', 'Sucio', 'Nuevo', 'Viejo', 'Joven', 'Viejo', 'Ruidoso', 'Tranquilo', 'Seco', 'Mojado', 'Correcto', 'Incorrecto', 'Verdad', 'Mentira', 'Rico', 'Pobre', 'Ancho', 'Estrecho', 'Alto', 'Bajo', 'Duro', 'Suave', 'Redondo', 'Cuadrado', 'Bueno', 'Malo', 'Fuerte', 'Debil', 'Izquierda', 'Derecha', 'Longitud', 'Anchura', 'Altura', 'Profundidad', 'Tierra', 'Cielo', 'Fuego', 'Agua', 'Aire', 'Viento', 'Roca', 'Arena', 'Nieve', 'Hielo', 'Tormenta', 'Lluvia', 'Nube', 'Relampago', 'Destello', 'Trueno', 'Planeta', 'Estrella', 'Galaxia', 'Universo', 'Sol', 'Luna', 'Marte', 'Venus', 'Júpiter', 'Saturno', 'Urano', 'Neptuno', 'Plutón', 'Astronauta', 'Satelite', 'Cometa', 'Meteorito', 'Telescopio', 'Mecanico', 'Ingeniero', 'Arquitecto', 'Constructor', 'Piloto', 'Conductor', 'Cirujano', 'Doctor', 'Enfermera', 'Dentista', 'Farmacéutico', 'Veterinario', 'Maestro', 'Profesor', 'Estudiante', 'Escolar', 'Policía', 'Bombero', 'Soldado', 'Marinero', 'Aviador', 'Mecánico', 'Electricista', 'Fontanero', 'Carpintero', 'Albañil', 'Jardinero', 'Cocinero', 'Camarero', 'Camarera', 'Carnicero', 'Panadero', 'Pastelero', 'Artesano', 'Artista', 'Pintor', 'Escultor', 'Músico', 'Cantante', 'Compositor', 'Escritor', 'Poeta', 'Periodista', 'Reportero', 'Fotógrafo', 'Cineasta', 'Actor', 'Actriz', 'Bailarín', 'Coreógrafo', 'Director', 'Productor', 'Técnico', 'Informática', 'Programador', 'Analista', 'Especialista', 'Consultor', 'Emprendedor', 'Jefe', 'Director', 'Ejecutivo', 'Presidente', 'Ministro', 'Diputado', 'Senador', 'Gobernador', 'Alcalde', 'Consejero', 'Diplomático', 'Embajador', 'Cónsul', 'Abogado', 'Juez'];
const Allemand = ['Allemand', 'Hallo', 'Danke', 'Liebe', 'Katze', 'Hund', 'Haus', 'Auto', 'Schule', 'Buch', 'Apfel', 'Wasser', 'Sonne', 'Mond', 'Sommer', 'Winter', 'Frühling', 'Herbst', 'Schnee', 'Regen', 'Wind', 'Zeit', 'Tag', 'Nacht', 'Stunde', 'Minute', 'Sekunde', 'Stadt', 'Dorf', 'Land', 'Berg', 'Meer', 'Fluss', 'See', 'Wald', 'Baum', 'Blume', 'Garten', 'Straße', 'Straße', 'Gasse', 'Brücke', 'Boot', 'Flugzeug', 'Zug', 'Bus', 'Fahrrad', 'Motorrad', 'Arbeit', 'Angestellter', 'Chef', 'Verkäufer', 'Kunde', 'Büro', 'Computer', 'Telefon', 'Tablet', 'Internet', 'E-Mail', 'Brief', 'Briefmarke', 'Kasten', 'Geschenk', 'Geburtstag', 'Party', 'Hochzeit', 'Geburt', 'Tod', 'Freund', 'Kind', 'Erwachsener', 'Frau', 'Mann', 'Mädchen', 'Junge', 'Mutter', 'Vater', 'Bruder', 'Schwester', 'Onkel', 'Tante', 'Cousin', 'Großmutter', 'Großvater', 'Heiß', 'Kalt', 'Süß', 'Bitter', 'Salzig', 'Sauer', 'Schön', 'Hässlich', 'Groß', 'Klein', 'Lang', 'Kurz', 'Schwer', 'Leicht', 'Schnell', 'Langsam', 'Glücklich', 'Traurig', 'Einfach', 'Schwierig', 'Stark', 'Schwach', 'Licht', 'Schatten', 'Klar', 'Dunkel', 'Sauber', 'Schmutzig', 'Neu', 'Alt', 'Jung', 'Alt', 'Laut', 'Leise', 'Trocken', 'Nass', 'Richtig', 'Falsch', 'Wahrheit', 'Lüge', 'Reich', 'Arm', 'Breit', 'Schmal', 'Hoch', 'Niedrig', 'Hart', 'Weich', 'Rund', 'Quadrat', 'Gut', 'Schlecht', 'Stark', 'Schwach', 'Links', 'Rechts', 'Länge', 'Breite', 'Höhe', 'Tiefe', 'Erde', 'Himmel', 'Feuer', 'Wasser', 'Luft', 'Wind', 'Felsen', 'Sand', 'Schnee', 'Eis', 'Sturm', 'Regen', 'Wolke', 'Blitz', 'Blitz', 'Donner', 'Planet', 'Stern', 'Galaxie', 'Universum', 'Sonne', 'Mond', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptun', 'Pluto', 'Astronaut', 'Satellit', 'Komet', 'Meteorit', 'Teleskop', 'Mechaniker', 'Ingenieur', 'Architekt', 'Bauherr', 'Pilot', 'Fahrer', 'Chirurg', 'Arzt', 'Krankenschwester', 'Zahnarzt', 'Apotheker', 'Tierarzt', 'Lehrer', 'Professor', 'Student', 'Schuljunge', 'Polizist', 'Feuerwehrmann', 'Soldat', 'Seemann', 'Flieger', 'Mechaniker', 'Elektriker', 'Klempner', 'Zimmermann', 'Maurer', 'Gärtner', 'Koch', 'Kellner', 'Kellnerin', 'Metzger', 'Bäcker', 'Konditor', 'Handwerker', 'Künstler', 'Maler', 'Bildhauer', 'Musiker', 'Sänger', 'Komponist', 'Schriftsteller', 'Dichter', 'Journalist', 'Reporter', 'Fotograf', 'Filmemacher', 'Schauspieler', 'Schauspielerin', 'Tänzer', 'Choreograph', 'Regisseur', 'Produzent', 'Techniker', 'Informatik', 'Programmierer', 'Analyst', 'Spezialist', 'Berater', 'Unternehmer', 'Chef', 'Direktor', 'Geschäftsführer', 'Präsident', 'Minister', 'Abgeordneter', 'Senator', 'Gouverneur', 'Bürgermeister', 'Berater', 'Diplomat', 'Botschafter', 'Konsul', 'Anwalt', 'Richter'];

// MAEVA ET ELOUAN : Java

function generation_mot(liste,ind) {
    // Rôle : donner un mot dans une liste au hasard
    // Entrées : liste = list()
    // Retourne : str
    alert(liste);
    if (liste == "Français"){
        alert(Français[ind])
    }
    if (liste == "Anglais"){
        alert(Anglais[ind])
    }
    if (liste == "Espagnol"){
        alert(Espagnol[ind])
    }
    if (liste == "Allemand"){
        alert(Allemand[ind])
    }
    return liste[ind]; //on retourne le mot correspondant à l'index dans la liste
}

function qcm(liste_traduction, liste_revision, index) {
    // Rôle : générer un mot avec sa traduction de manière aléatoire
    // Entrées : liste_traduction = list(), liste_revision = list()
    // Retourne : q = list()
    const q = []; // Créer la liste q
    const mot = generation_mot(liste_revision,index); // On génère le mot
    q.push(mot); // On ajoute le mot généré dans la liste q

    const co = liste_revision.indexOf(mot); 
    if (co !== -1) {
        const reponse = liste_traduction[co]; // Depuis l'index récupéré du mot, on prend son équivalent traduit
        q.push(reponse); // On ajoute le mot traduit à q
    }
    document.addEventListener('DOMContentLoaded', function() {
        document.getElementById('mot').textContent = mot;
    });
    return q; // On renvoie q
}

function quiz(liste_traduction, liste_revision) {
    // Rôle : créer les réponses du QCM
    // Entrer : liste_traduction = liste avec tous les mots
    // Sortie : liste_reponse = list()
    const ind = Math.floor(Math.random() * liste.length); //on tire un index au hasard dans la liste

    const q = qcm(liste_traduction, liste_revision,ind); //le mot généré aléatoirement et sa bonne réponse dans une liste
    const liste_reponse = []; //on crée une nouvelle liste dans laquelle on mettra les réponses du qcm
    
    const r = Math.floor(Math.random() * 4); //la position de la bonne réponse générée aléatoirement

    for (let i = 0; i < 4; i++) { //une boucle qui se produit 4 fois
        if (i === r) { //si i est égal à la position de la bonne réponse
            liste_reponse.push(q[1]); //on ajoute la bonne réponse dans la position
        } else { //dans le cas où la position n'est pas celle de la bonne réponse
            let mauvais = generation_mot(liste_traduction,ind); //génère une mauvaise réponse
            while (mauvais === q[1]) { //tant que par malchance le mot généré est le même que la bonne réponse
                mauvais = generation_mot(liste_traduction,ind); //regénère une mauvaise réponse
            }
            liste_reponse.push(mauvais); //on ajoute la mauvaise réponse à la valeur i, donc à la position actuelle d'où l'on parcourt la liste
        }
    }

    return liste_reponse;
}

function openPage() {
    const revision = document.getElementById("base").value;
    const traduction = document.getElementById("entrainement").value;
    window.location.href = 'Quiz.html';
    const quizReponses = quiz(traduction, revision);
    alert(quizReponses + "reponse")
}