def student(imie, nazwisko, semestr, *wykaz_przedmiotow, stypendium=False):
    def sprawdz_stypendium(x):
        if x is True:
            return 'Przyznane'
        else:
            return 'Nieprzyznane'

    return (
        f'🟢 Cześć {imie} {nazwisko}, '
        f'jesteś studentem {semestr} semestru, '
        f'Twój wykaz przedmiotów: {", ".join(wykaz_przedmiotow)}. '
        f' Stypendium: {sprawdz_stypendium(stypendium)}')


sebastian = student('Sebastian', 'Kowalski', 2, 'matematyka', 'fizyka', 'biologia', 'chemia')
iwona = student('Iwona', 'Kowalska', 3, 'zarzadzanie', 'python', 'filozofia', stypendium=True)
dawid = student('Dawid', 'Kowalski', 3, 'python', 'sql', 'matematyka')
zofia = student('Zosia', 'Tolar', 4, 'historia', 'j. angielski', 'filozofia')

print(f' {sebastian},\n {iwona},\n {dawid},\n {zofia},')
