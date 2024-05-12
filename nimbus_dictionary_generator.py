#!/usr/bin/env python3

# Nimbus Dictionary Generator 2024: By C4sp3r

import os
from colorama import init, Fore
from itertools import permutations

# Inicializar colorama para Windows
init(autoreset=True)

def generate_combinations(words):
    """Genera todas las combinaciones posibles de las palabras dadas."""
    combinations = []
    for r in range(1, len(words) + 1):
        combinations.extend(permutations(words, r))
    return combinations

def generate_new_dictionary(words, new_dictionary_name):
    """Genera un nuevo diccionario con las palabras y todas las combinaciones posibles."""
    try:
        total_lines_new = 0
        word_list = [word.strip() for word in words.split(',')]
        combinations_list = generate_combinations(word_list)

        with open(new_dictionary_name, 'w', encoding='utf-8') as f_out:
            for combination in combinations_list:
                combination_str = ''.join(combination)
                if combination_str != words:  # Evita duplicados
                    f_out.write(combination_str + '\n')  # Guarda las combinaciones de palabras
                    total_lines_new += 1

        print(Fore.YELLOW + f"[+] El diccionario final tendrá un total de {total_lines_new} líneas." + Fore.RESET)
        decision = input(Fore.CYAN + "[+] ¿Desea continuar con la creación del diccionario? (Si/No): " + Fore.RESET).lower()
        if decision in ['si', 'sí', 's']:
            print(Fore.GREEN + "[+] Diccionario generado con éxito:", new_dictionary_name + Fore.RESET)
        else:
            print(Fore.YELLOW + "[+] Saliendo..." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "[!] ERROR:", e + Fore.RESET)

def generate_new_dictionary_from_file(dictionary_path, characters, new_dictionary_name):
    """Genera un nuevo diccionario añadiendo caracteres al original."""
    try:
        total_lines_new = 0

        with open(dictionary_path, 'r', encoding='utf-8') as f_in, open(new_dictionary_name, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                line = line.strip()
                f_out.write(line + '\n')  # Guarda la palabra original
                for char in characters.split(','):
                    modified_line = line + char.strip()
                    f_out.write(modified_line + '\n')  # Guarda las combinaciones de caracteres
                    total_lines_new += 1

        print(Fore.YELLOW + f"[+] El diccionario final tendrá un total de {total_lines_new} líneas." + Fore.RESET)
        decision = input(Fore.CYAN + "[+] ¿Desea continuar con la creación del diccionario? (Si/No): " + Fore.RESET).lower()
        if decision in ['si', 'sí', 's']:
            print(Fore.GREEN + "[+] Diccionario generado con éxito:", new_dictionary_name + Fore.RESET)
        else:
            print(Fore.YELLOW + "[+] Saliendo..." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "[!] ERROR:", e + Fore.RESET)

def generate_combinations_from_file(dictionary_path, characters, new_dictionary_name):
    """Genera un nuevo diccionario con las palabras del diccionario original y todas las combinaciones de caracteres."""
    try:
        total_lines_new = 0

        with open(dictionary_path, 'r', encoding='utf-8') as f_in, open(new_dictionary_name, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                line = line.strip()
                f_out.write(line + '\n')  # Guarda la palabra original
                for r in range(1, len(characters.split(',')) + 1):
                    for combination in permutations(characters.split(','), r):
                        combination_str = ''.join(combination)
                        modified_line = line + combination_str
                        f_out.write(modified_line + '\n')  # Guarda las combinaciones de caracteres
                        total_lines_new += 1

        print(Fore.YELLOW + f"[+] El diccionario final tendrá un total de {total_lines_new} líneas." + Fore.RESET)
        decision = input(Fore.CYAN + "[+] ¿Desea continuar con la creación del diccionario? (Si/No): " + Fore.RESET).lower()
        if decision in ['si', 'sí', 's']:
            print(Fore.GREEN + "[+] Diccionario generado con éxito:", new_dictionary_name + Fore.RESET)
        else:
            print(Fore.YELLOW + "[+] Saliendo..." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "[!] ERROR:", e + Fore.RESET)

def merge_dictionaries(dictionary1_path, dictionary2_path, new_dictionary_name):
    """Une dos diccionarios en uno nuevo."""
    try:
        total_lines_merged = 0

        with open(dictionary1_path, 'r', encoding='utf-8') as f_dict1, \
             open(dictionary2_path, 'r', encoding='utf-8') as f_dict2, \
             open(new_dictionary_name, 'w', encoding='utf-8') as f_out:

            lines_dict1 = f_dict1.readlines()
            lines_dict2 = f_dict2.readlines()

            total_lines_dict1 = len(lines_dict1)
            total_lines_dict2 = len(lines_dict2)
            total_lines_merged = total_lines_dict1 + total_lines_dict2

            print(Fore.YELLOW + f"\n[i] Se van a unir los diccionarios:")
            print(f"   [+] {dictionary1_path} -> {total_lines_dict1} líneas")
            print(f"   [+] {dictionary2_path} -> {total_lines_dict2} líneas")

            for line in lines_dict1:
                f_out.write(line)
            for line in lines_dict2:
                f_out.write(line)

        print(Fore.YELLOW + f"\n[i] El diccionario final tendrá {total_lines_merged} líneas en total.")
        decision = input(Fore.CYAN + "\n[+] ¿Desea continuar con la creación del diccionario? (Si/No): " + Fore.RESET).lower()
        if decision in ['si', 'sí', 's']:
            print(Fore.GREEN + "\n[+] Diccionario generado con éxito:", new_dictionary_name + Fore.RESET)
        else:
            print(Fore.YELLOW + "[+] Saliendo..." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "[!] ERROR:", e + Fore.RESET)

def get_new_dictionary_name():
    """Obtiene el nombre para el nuevo diccionario."""
    name = input(Fore.CYAN + "[+] Nombre del nuevo diccionario (Por defecto: Nuevo_diccionario.txt):\n   Ej: Mi_Nuevo_diccionario.txt\n" + Fore.RESET)
    if not name:
        name = "Nuevo_diccionario.txt"
    return name

def menu():
    print("\ \ \ \ \ \                    | \ | (_)_ __ ___ | |__  _   _ ___                                ") 
    print(" \ \ \ \ \ \_____ _____ _____  |  \| | | '_ ` _ \| '_ \| | | / __|  _____ _____ _____ _____ _____") 
    print(" / / / / / /_____|_____|_____| | |\  | | | | | | | |_) | |_| \__ \ |_____|_____|_____|_____|_____|")
    print("/_/_/_/_/_/   _   _            |_| \_|_|_| |_| |_|_.__/_\__,_|___/                 _              ")
    print("|  _ \(_) ___| |_(_) ___  _ __   __ _ _ __ _   _   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __  ")
    print("| | | | |/ __| __| |/ _ \| '_ \ / _` | '__| | | | | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| ")
    print("| |_| | | (__| |_| | (_) | | | | (_| | |  | |_| | | |_| |  __/ | | |  __/ | | (_| | || (_) | |    ")
    print("|____/|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   \n\n")
    print("By C4sp3r\n\n")  
    """Muestra el menú de opciones."""
    print(Fore.YELLOW + "[+] Elige entre las opciones:\n" + Fore.RESET)
    print("    [1] Crear un diccionario con palabras:")
    print("    [2] Añadir caracteres a un diccionario dado:")
    print("    [3] Unir diccionarios\n")

def main():

    """Función principal del programa."""
    try:
        menu()
        option = input(Fore.CYAN + "[+] Elige una opción: " + Fore.RESET)

        if option == '1':
            print(Fore.YELLOW + "\n[+] Vamos a crear un diccionario con palabras.\n" + Fore.RESET)
            new_dictionary_name = get_new_dictionary_name()
            words = input(Fore.CYAN + "[+] Vamos a generar un nuevo diccionario, dime qué palabras se incluirán (separadas por comas):\n   Ej: Perro,Gato,Babosa\n" + Fore.RESET)
            generate_new_dictionary(words, new_dictionary_name)
        elif option == '2':
            print(Fore.YELLOW + "\n[+] Vamos a añadir caracteres a un diccionario dado.\n" + Fore.RESET)
            dictionary_path = input(Fore.CYAN + "[+] Dime la ruta del diccionario base:\n   Ej: /usr/share/wordlists/diccionario.txt\n" + Fore.RESET)
            characters = input(Fore.CYAN + "[+] Indica carácter/s a añadir:\n   Ej: A,A1,A1*\n" + Fore.RESET)
            new_dictionary_name = get_new_dictionary_name()
            generate_combinations_from_file(dictionary_path, characters, new_dictionary_name)
        elif option == '3':
            print(Fore.YELLOW + "\n[+] Vamos a unir dos diccionarios.\n" + Fore.RESET)
            new_dictionary_name = input(Fore.CYAN + "[+] Nombre del nuevo diccionario (Por defecto: diccionarios_unidos.txt):\n   Ej: diccionarios_unidos.txt\n" + Fore.RESET)
            if not new_dictionary_name:
                new_dictionary_name = "diccionarios_unidos.txt"
            dictionary1_path = input(Fore.CYAN + "\n[+] Dime la ruta del primer diccionario a usar:\n" + Fore.RESET)
            dictionary2_path = input(Fore.CYAN + "\n[+] Dime la ruta del segundo diccionario:\n" + Fore.RESET)
            merge_dictionaries(dictionary1_path, dictionary2_path, new_dictionary_name)
        else:
            print(Fore.RED + "\n[!] ERROR: Opción no válida." + Fore.RESET)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[+] Saliendo..." + Fore.RESET)

if __name__ == "__main__":
    main()
