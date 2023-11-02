def main():
    mark_count = 0
    mark_total = 0.0
    mark_minimum = 99.9

    mark = float(input('Note eingeben > '))
    while mark > 0.0:
        mark_count += 1
        mark_total += mark
        if mark < mark_minimum:
            mark_minimum = mark
        mark = float(input('Note eingeben > '))

    if mark_count > 1:
        mark_total -= mark_minimum
        mark_count -= 1
    average = mark_total / mark_count

    print('Notenschnitt: ' + str(average))


if __name__ == '__main__':
    main()