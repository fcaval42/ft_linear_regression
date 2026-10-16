# ft_linear_regression

Programme d'introduction au machine learning : prédire le **prix d'une voiture d'occasion** à partir de son **kilométrage**, en utilisant une **régression linéaire** entraînée par **descente de gradient** — codée entièrement à la main (pas de bibliothèque de ML).

## 🚀 Utilisation

Seul prérequis : [matplotlib](https://matplotlib.org) pour le graphe (bonus).

```bash
pip install matplotlib
python3 main.py
```

Le programme ouvre un menu :

```
1 - Program: Prediction
2 - Program: Training
3 - Exit
```

| Choix | Programme | Rôle |
|---|---|---|
| 2 | `train` | Lit `data.csv`, apprend θ0 et θ1, les sauvegarde dans `thetas.txt` et affiche le graphe (données + droite apprise) |
| 1 | `predict` | Lit `thetas.txt` (ou 0 et 0 s'il n'existe pas) et estime le prix d'un kilométrage saisi |

Ordre conseillé : lancer le **training** au moins une fois, sinon la prédiction vaut toujours 0 (modèle non entraîné — comportement demandé par le sujet).

## 📖 Comment ça marche

### Le modèle : une droite

```
estimatePrice(mileage) = theta0 + theta1 * mileage
```

- **theta0** : le prix "de départ" (voiture à 0 km)
- **theta1** : la pente — combien le prix varie **par kilomètre** (négative : plus de km = moins cher)

Toute la question est : **comment trouver θ0 et θ1 ?** La descente de gradient les fait émerger petit à petit, par essai-correction, à partir des exemples de `data.csv`.

### La descente de gradient (`train/train.py`)

On part de θ0 = 0, θ1 = 0, puis on répète le même rituel `EPOCH` fois (10 000) :

1. **Mesurer les erreurs** du modèle actuel : `erreur = prédiction − prix réel` sur chaque voiture
2. **Additionner** ces erreurs de deux façons :
   - `sum0` = somme des erreurs → corrige la **hauteur** de la droite (θ0)
   - `sum1` = somme des `erreur × km` → corrige la **pente** (θ1), en donnant plus de poids aux gros kilométrages
3. **Moyenner et freiner** : `tmp = LEARNING_RATE × (1/m) × sum` — le `1/m` fait une moyenne (le pas ne dépend pas du nombre de voitures), le learning rate (0.01) évite de sauter par-dessus la solution
4. **Mettre à jour simultanément** : les deux `tmp` sont calculés avec les *anciens* thetas, **avant** de modifier θ0 et θ1 (formules exactes du sujet)

Si le modèle prédit trop bas, les erreurs sont négatives, et soustraire un `tmp` négatif fait **monter** la droite : à chaque itération, la droite se rapproche des données jusqu'à se stabiliser. Le programme affiche l'erreur moyenne toutes les 1000 itérations pour vérifier la convergence.

### La normalisation (`train/normalize.py`)

Les kilométrages vont jusqu'à 240 000. Sans précaution, `erreur × km` produit des corrections gigantesques et les thetas divergent (`nan`). On ramène donc les km dans l'intervalle **[0, 1]** :

```
km_norm = (km − km_min) / (km_max − km_min)
```

Une fois les thetas appris sur les km normalisés, on les **dé-normalise** pour revenir à l'échelle réelle :

```
theta1_reel = theta1 / (km_max − km_min)
theta0_reel = theta0 − theta1_reel × km_min
```

Ainsi `predict` travaille directement avec de vrais kilométrages.

### Le parsing (`train/parsing.py`)

Lecture de `data.csv` avec validation : en-têtes `km,price` obligatoires, exactement 2 colonnes par ligne, nombres valides, valeurs non négatives, au moins 2 points. Chaque erreur indique la **ligne fautive**.

## 🗂️ Structure du projet

```
main.py                  # menu principal (prédiction / training / exit)
data.csv                 # dataset : km, prix des voitures
thetas.txt               # créé par le training, lu par la prédiction
predict/
    predict.py           # lecture thetas (défaut 0,0), saisie user, estimation
train/
    parsing.py           # lecture et validation de data.csv
    normalize.py         # normalisation / dé-normalisation
    train.py             # boucle de descente de gradient
    train_menu.py        # orchestration du training + sauvegarde thetas.txt
utils/
    global_variables.py  # constantes (LEARNING_RATE, EPOCH) et couleurs
    plot.py              # graphe matplotlib : données + droite (bonus)
```

## 🔍 Exemple

Après entraînement sur `data.csv` :

```
theta0 = 8476.88   # prix "à 0 km"
theta1 = -0.02123  # ≈ −2 centimes par kilomètre
```

| Kilométrage | Prix estimé |
|---|---|
| 10 000 km | 8 264 € |
| 60 000 km | 7 203 € |
| 120 000 km | 5 929 € |
| 200 000 km | 4 230 € |