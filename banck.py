import accaunt
from converter import converter

def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))

    result = accaunt.calculate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма в рублях: ", money, "\n", "Сумма в долларах: ", converter(1, money), "\n", "Сумма в евро: ", converter(2, money), "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода в рублях: ", result, "\n","В евро: ", converter(2, result), "\n" "В долларах: ", converter(1, result), "\n")


if __name__ == "__main__":
    main()