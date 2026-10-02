from .stats import char_stats, word_count

def main():
    t = "Ура, отчисление"
    print("Слов:", word_count(t), "| Статистика:", char_stats(t))

if __name__ == "__main__":
    main()