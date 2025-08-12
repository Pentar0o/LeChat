import argparse
from termcolor import colored
from mlx_lm import generate, load
import time


def generate_response(tokenizer, model, prompt: str, max_tokens: int):
    """Génère une réponse à partir du prompt en utilisant le modèle."""
    start = time.time()

    response = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=max_tokens,
        verbose=False
    )

    duration_s = time.time() - start

    print(colored(response.strip(), "blue"))
    nb_tokens = len(tokenizer.encode(response))
    speed_tps = nb_tokens / duration_s if duration_s > 0 else 0.0

    return response.strip(), nb_tokens, duration_s, speed_tps


def main(model_name, system_prompt_file, temperature, max_tokens):
    """Fonction principale du chat."""
    
    print(colored("🔄 Chargement du modèle et du tokenizer (MLX)...", "yellow"))
    model_config = {"temperature": temperature}
    model, tokenizer = load(model_name, model_config=model_config)
    
    try:
        with open(system_prompt_file, 'r', encoding='utf-8') as f:
            system_prompt = f.read().strip()
    except FileNotFoundError:
        print(colored(f"Attention : Le fichier '{system_prompt_file}' n'a pas été trouvé. Utilisation d'un prompt système par défaut.", "red"))
        system_prompt = "Tu es un assistant IA serviable et sympathique."

    messages = [{"role": "system", "content": system_prompt}]
    print(colored("✅ Modèle chargé. Vous pouvez commencer à discuter (tapez 'bye' pour quitter).", "green"))
    
    while True:
        try:
            user_input = input(colored("Vous : ", "green"))
        except KeyboardInterrupt:
            print(colored("\nAu revoir !", "yellow"))
            break
            
        if user_input.lower() == 'bye':
            print(colored("Au revoir !", "yellow"))
            break

        messages.append({"role": "user", "content": user_input})

        full_prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        response, nb_tokens, duration_s, speed_tps = generate_response(tokenizer, model, full_prompt, max_tokens)

        print(colored(f"\nTokens générés : {nb_tokens}", "yellow"))
        print(colored(f"Temps          : {duration_s:.2f} s", "yellow"))
        print(colored(f"Vitesse        : {speed_tps:.2f} tokens/s\n", "yellow"))

        messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat avec MLX sur Apple Silicon.")
    parser.add_argument("--model", type=str, default="mlx-community/Meta-Llama-3.1-8B-Instruct-4bit", help="Nom du modèle à utiliser depuis le Hub.")
    parser.add_argument("--system_prompt_file", type=str, default="System_Prompt.txt", help="Chemin vers le fichier du prompt système.")
    
    parser.add_argument("--temperature", type=float, default=0.1, help="Température pour la génération (contrôle la créativité).")
    
    parser.add_argument("--max_tokens", type=int, default=4096, help="Nombre maximal de tokens à générer pour la réponse.")

    args = parser.parse_args()
    
    main(args.model, args.system_prompt_file, args.temperature, args.max_tokens)
