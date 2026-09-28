def most_common_word(text):
    pass # def most_common_word(text):
    # 1. Очищаем текст и приводим к нижнему регистру
    text = text.lower()
    for char in ".,!?;:-()\"'":
        text = text.replace(char, "")
        
    # 2. Разбираем строку на список слов
    words = text.split()
    
    if not words:
        return ""
        
    # 3. Создаем словарь для счёта слов
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    # 4. Ищем самое частое слово
    leader_word = ""
    max_count = 0
    
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            leader_word = word
            
    return leader_word

#  ПРОВЕРКИ ASSERT:
assert most_common_word("кот кот собака") == "кот", "Самое частое слово — кот"
assert most_common_word("Кот кот КОТ собака") == "кот", "Регистр должен игнорироваться"
assert most_common_word("молоко, молоко! молоко? хлеб.") == "молоко", "Знаки препинания должны игнорироваться"
assert most_common_word("слово") == "слово", "Ожидалось единственное слово"
res = most_common_word("а б а б")
assert res in ("а", "б"), "Ожидалось одно из слов с максимальной частотой"

print("код работает!")


assert most_common_word("кот кот собака") == "кот", "Самое частое слово — кот"
assert most_common_word("Кот кот КОТ собака") == "кот", "Регистр должен игнорироваться"
assert most_common_word("молоко, молоко! молоко? хлеб.") == "молоко", "Знаки препинания должны игнорироваться"
assert most_common_word("слово") == "слово", "Ожидалось единственное слово"
res = most_common_word("а б а б")
assert res in ("а", "б"), "Ожидалось одно из слов с максимальной частотой"
