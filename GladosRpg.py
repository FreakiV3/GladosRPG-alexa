import random

# Liste des actions possibles sur les cases du plateau
cases_actions = {
    0: "Vous êtes tombé sur une case vide, rien ne se passe.",
    1: "Vous avez trouvé une boîte de gâteaux, +10 points de santé.",
    2: "Un cube de compagnie vous a suivi, vous gagnez un compagnon.",
    3: "Vous avez résolu une énigme, avancez de 5 cases.",
    4: "Vous avez déclenché un gaz neurotoxique, -5 points de santé.",
    5: "Un vortex vous téléporte plus loin, avancez de 10 cases.",
    6: "Vous avez activé un générateur d'énergie, +20 points de santé."
}

# Liste des questions aléatoires sur le thème du jeu
questions = [
    "Quel est le nom du robot sphérique compagnon de Chell dans Portal?",
    "Dans quel laboratoire se déroule le jeu Portal?",
    "Quel est le principal objet que le joueur utilise pour résoudre les énigmes?",
    "Qui est le méchant robot dans Portal 2?",
    "Comment s'appelle la scientifique qui parle à Chell tout au long du jeu?",
    "Quel est le nom de la chanson emblématique de Portal?"
]

# Liste des réponses aux questions
reponses = [
    ["glados", "glados l'ordinateur", "glados l'intelligence artificielle"],
    ["aperture science", "laboratoire aperture science"],
    ["le portal gun", "le pistolet portal"],
    ["glados", "glados le robot", "glados l'intelligence artificielle"],
    ["leech woman", "la femme sangsue", "caroline"],
    ["still alive"]
]

# Créer une fonction pour lancer le dé
def lancer_de():
    return random.randint(1, 6)

# Créer une fonction pour poser une question
def poser_question():
    index_question = random.randint(0, len(questions) - 1)
    question = questions[index_question]
    reponse_attendue = reponses[index_question]
    return question, reponse_attendue

# Créer une fonction pour gérer les actions en fonction du numéro de case
def gerer_case(numero_case, sante):
    action = cases_actions.get(numero_case, "Vous êtes tombé sur une case vide, rien ne se passe.")
    if "mort" in action:
        print(action)
        print("Votre score final est :", sante)
        exit()
    elif "retour" in action:
        return -10, action
    elif "question" in action:
        question, reponse_attendue = poser_question()
        print(question)
        reponse_utilisateur = input("Votre réponse: ").lower()
        if reponse_utilisateur in reponse_attendue:
            print("Bonne réponse, avancez de 5 cases.")
            return 5, action
        else:
            print("Mauvaise réponse, reculez de 3 cases.")
            return -3, action
    else:
        print(action)
        return 0, action

# Fonction principale du jeu
def jeu_rpg_glados():
    print("Bienvenue dans le RPG de Portal. Vous incarnez Shell et devez vous échapper du complexe d'Aperture Science.")
    print("Lancez le dé en disant 'Lancer le dé'")
    sante = 100
    position = 1

    while position <= 120:
        input_text = input().lower()

        if "lancer le dé" in input_text:
            de_resultat = lancer_de()
            print("Vous avez obtenu un", de_resultat)
            deplacement, action = gerer_case(de_resultat, sante)
            sante += deplacement
            position += deplacement
            print("Votre santé est de", sante)

    print("Félicitations, vous avez réussi à vous échapper d'Aperture Science ! Votre score final est :", sante)

# Lancer le jeu
jeu_rpg_glados()
