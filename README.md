# LeChat 🐱

Un chat CLI (interface en ligne de commande) simple, léger et personnalisable pour converser avec un grand modèle de langage (LLM) grâce au framework **MLX** d'Apple.

Ce projet est conçu pour tourner localement sur les Mac équipés d'une puce Apple Silicon (M1, M2, M3...). Il affiche également des statistiques de performance (tokens/seconde) après chaque réponse.

---

## 🚀 Installation

Avant de lancer `LeChat`, vous devez installer les dépendances nécessaires.

1.  **Prérequis :** Assurez-vous d'avoir **Python 3** et **pip** installés sur votre Mac.

2.  **Installation des paquets :** Ouvrez votre terminal et exécutez la commande suivante.

    ```bash
    pip3 install mlx mlx-lm termcolor --break-system-packages
    ```
    * `mlx` & `mlx-lm` : Le framework d'Apple pour l'apprentissage automatique optimisé pour Apple Silicon.
    * `termcolor` : Une librairie pour colorer le texte et rendre la conversation plus lisible.
    * `--break-system-packages` : Cette option est souvent nécessaire sur les versions récentes de macOS pour permettre à `pip` d'installer des paquets.

---

## ▶️ Utilisation

### Lancement simple

Pour démarrer une conversation avec les paramètres par défaut, exécutez simplement :

```bash
python3 LeChat.py
```
Cela utilisera le modèle `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit` et cherchera un fichier `System_Prompt.txt` pour les instructions de l'IA.

### Options de lancement (avancé)

Vous pouvez personnaliser le comportement du chat directement depuis la ligne de commande grâce aux arguments suivants :

| Argument                 | Description                                                                                              | Défaut                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| `--model`                | Nom du modèle à utiliser depuis [Hugging Face MLX Community](https://huggingface.co/mlx-community).        | `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit`    |
| `--system_prompt_file`   | Chemin vers le fichier texte contenant le prompt système (personnalité de l'IA).                         | `System_Prompt.txt`                                |
| `--temperature`          | Contrôle la "créativité" des réponses. `0.0` est déterministe, `1.0` est très créatif.                   | `0.1`                                              |
| `--max_tokens`           | Nombre maximum de tokens (mots/syllabes) à générer pour chaque réponse.                                  | `4096`                                             |

### Exemples de commandes

* **Utiliser un modèle plus léger (Mistral 7B) :**
    ```bash
    python3 LeChat.py --model "mlx-community/Mistral-7B-Instruct-v0.2-4bit"
    ```

* **Rendre l'IA plus créative et utiliser un prompt système spécifique :**
    ```bash
    python3 LeChat.py --temperature 0.8 --system_prompt_file "Creative_Mode.txt"
    ```

---

## 📝 Personnalisation du Prompt Système

Le "prompt système" est une instruction initiale qui définit la personnalité, le rôle ou le contexte de l'IA. C'est le meilleur moyen de guider ses réponses.

1.  Créez un fichier texte (par exemple `System_Prompt.txt`).
2.  Écrivez à l'intérieur les instructions pour l'IA.
3.  Lancez le script en utilisant l'argument `--system_prompt_file` si votre fichier a un nom différent.

#### Exemple de contenu pour `System_Prompt.txt` :

```text
Tu es un expert en histoire de France. Tu réponds de manière concise et précise, en te concentrant uniquement sur les faits historiques. Tu adoptes un ton académique.
```

---

## Exit

Pour quitter le chat, tapez `bye` et appuyez sur Entrée, ou utilisez le raccourci clavier `Ctrl+C`.
