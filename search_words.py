#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 1-2: Поиск вхождения подстроки в словах текста.
Текст и искомая строка задаются через консольный ввод (имитация формы).
Вывод всех слов, содержащих искомую строку.
Обработка ошибок при неверном вводе.
"""

import re
import sys


def find_words_containing_substring(text: str, substring: str) -> list[str]:
    """
    Находит все слова в тексте, которые содержат заданную подстроку.
    Слово определяется как последовательность букв, цифр и подчёркиваний.
    Поиск регистронезависимый.
    """
    if not text or not substring:
        return []
    
    # Разбиваем текст на слова (буквы, цифры, подчёркивания)
    words = re.findall(r'\b\w+\b', text, flags=re.UNICODE)
    
    substring_lower = substring.lower()
    result = [word for word in words if substring_lower in word.lower()]
    
    # Убираем дубликаты, сохраняя порядок
    seen = set()
    unique_result = []
    for word in result:
        if word.lower() not in seen:
            seen.add(word.lower())
            unique_result.append(word)
    
    return unique_result


def main():
    print("=" * 60)
    print("Поиск слов, содержащих заданную подстроку")
    print("=" * 60)
    
    try:
        # Ввод данных (имитация формы)
        print("\nВведите текст для поиска:")
        text = input().strip()
        
        if not text:
            print("\n[ОШИБКА] Текст не может быть пустым. Введите корректный текст.")
            sys.exit(1)
        
        print("\nВведите искомую строку (подстроку):")
        substring = input().strip()
        
        if not substring:
            print("\n[ОШИБКА] Искомая строка не может быть пустой. Введите корректную строку.")
            sys.exit(1)
        
        # Поиск
        found_words = find_words_containing_substring(text, substring)
        
        print("\n" + "-" * 60)
        if found_words:
            print(f"[РЕЗУЛЬТАТ] Найдено слов, содержащих '{substring}': {len(found_words)}")
            print("Список слов:")
            for i, word in enumerate(found_words, 1):
                print(f"  {i}. {word}")
        else:
            print(f"[СООБЩЕНИЕ] Строка '{substring}' не найдена ни в одном слове текста.")
        print("-" * 60)
        
    except KeyboardInterrupt:
        print("\n\n[ОШИБКА] Программа прервана пользователем.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ОШИБКА] Непредвиденная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
