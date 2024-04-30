import csv


def count_passengers() -> dict:
    survivors_under_30 = 0
    survivors_above_60 = 0
    total_survivors = 0

    with open('data.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # читаем со второй строки
        for line in csv_reader:
            if int(line[1]) == 1:
                age = line[5]
                if age == '':
                    continue  # отбрасываем строки с неизвестным возрастом согласно условию
                age = float(age)
                if age < 30.0:
                    survivors_under_30 += 1
                elif age > 60.0:
                    survivors_above_60 += 1
                total_survivors += 1

    return {
            'under_30': survivors_under_30,
            'above_60': survivors_above_60,
            'total': total_survivors
            }


def survival_rate(data: dict) -> dict:
    return {
        'survival rate under 30': data['under_30'] / data['total'] * 100,
        'survival rate above 60': data['above_60'] / data['total'] * 100,
        }


def main():
    data = count_passengers()
    print(survival_rate(data))


if __name__ == '__main__':
    main()