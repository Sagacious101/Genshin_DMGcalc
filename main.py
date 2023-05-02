import os


'''
Надо написать программу которая будет спрашивать нужные статы и проценты, а затем высчитывать урон.
TODO: Написать отдельные подсчёты с учётом мультиплеера урона от другой характеристики, как у Сяо, Итто, Сайно
'''
DMG ={"AttackPower": 0,
"CritChance": 0, 
"CritDamage": 0, 
"TalentMultiplayer": 0, 
"BonusDMG": 0, 
"ElementMastery": 0, 
"lvl": 0, 
"Enemylvl": 0, 
"Resist": 0, 
"DebuffResist": 0,
"DebuffDefense": 0
}

def show_damage(DMG: dict) -> None:
   print("Урон и характеристики: ")
   print("\nХарактеристики: ")
   print(f"Сила атаки: {DMG['AttackPower']}")
   print(f"Крит шанс: {DMG['CritChance']}")
   print(f"Крит урон: {DMG['CritDamage']}")
   print(f"Множитель урона таланта(%): {DMG['TalentMultiplayer']}")
   print(f"Множитель бонусного урона(%): {DMG['BonusDMG']}")
   print(f"Мастерство стихий: {DMG['ElementMastery']}")
   print(f"Уровень: {DMG['lvl']}")
   print(f"Уровень врага: {DMG['Enemylvl']}")
   print(f"Сопротивление врага: {DMG['Resist']}")
   print(f"Уменьшение сопротивления врага: {DMG['DebuffResist']}")
   print("\nУрон: ")
   print(f"Конечный урон без крита: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100))}")
   print(f"Конечный крит урон: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100)) * (1 + (DMG['CritDamage'] / 100))}")
   print(f"Средний урон: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100)) * (1 + (DMG['CritChance'] / 100) * (DMG['CritDamage'] / 100))}")
   print("\nРеакции 1-го порядка:")
   print(f"Пар(Гидро по Пиро) и таянье(Пиро по Крио) без крита: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * 2 * ((1 + (DMG['ElementMastery'] * (25 / 9)) / (DMG['ElementMastery'] + 1400))) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100))}")
   print(f"Пар(Гидро по Пиро) и таянье(Пиро по Крио) с критом: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * 2 * ((1 + (DMG['ElementMastery'] * (25 / 9)) / (DMG['ElementMastery'] + 1400))) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100)) * (1 + (DMG['CritDamage'] / 100))}")
   print(f"Пар(Гидро по Пиро) и таянье(Пиро по Крио) средний урон: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * 2 * ((1 + (DMG['ElementMastery'] * (25 / 9)) / (DMG['ElementMastery'] + 1400))) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100)) * (1 + (DMG['CritChance'] / 100) * (DMG['CritDamage'] / 100))}")
   print(f"Пар(Пиро по Гидро) и таянье(Крио по Пиро) без крита: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * 2 * ((1 + (DMG['ElementMastery'] * (25 / 9)) / (DMG['ElementMastery'] + 1400))) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100))}")
   print(f"Пар(Пиро по Гидро) и таянье(Крио по Пиро) с критом: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * 2 * ((1 + (DMG['ElementMastery'] * (25 / 9)) / (DMG['ElementMastery'] + 1400))) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100)) * (1 + (DMG['CritDamage'] / 100))}")
   print(f"Пар(Пиро по Гидро) и таянье(Крио по Пиро) средний урон: {DMG['AttackPower'] * (DMG['TalentMultiplayer'] / 100) * (1 + (DMG['BonusDMG'] / 100)) * 2 * ((1 + (DMG['ElementMastery'] * (25 / 9)) / (DMG['ElementMastery'] + 1400))) * ((DMG['lvl'] + 100) / ((1 - (DMG['DebuffDefense'] / 100)) * (DMG['Enemylvl'] + 100) + (DMG['lvl'] + 100))) * (1 - (DMG['Resist'] / 100)) * (1 + (DMG['CritChance'] / 100) * (DMG['CritDamage'] / 100))}")
   print("\nРеакции 2-го порядка:")
   print(f"Заряд: {((-0.0000003511 * DMG['lvl'] ** 5 + 0.0000416577 * DMG['lvl'] ** 4 + 0.0009968915 * DMG['lvl'] ** 3 - 0.0458798109 * DMG['lvl'] ** 2 + 4.4547724452 * DMG['lvl'] ** 1 + 9.2965262268) * (1 + ((0.00000009*(DMG['ElementMastery']) ** 3 - 0.0002767 * (DMG['ElementMastery']) ** 2 + 0.46647865 * DMG['ElementMastery'] + 0.19667643) / 100)) * (1 - DMG['Resist'] / 100) // 1)}")
   print(f"Перегрузка: {((-0.0000012454 * DMG['lvl'] ** 5 + 0.0002299319 * DMG['lvl'] ** 4 - 0.0121896881 * DMG['lvl'] ** 3 + 0.4177057905 * DMG['lvl'] ** 2 + 1.2637850073 * DMG['lvl'] ** 1 + 28.3711853993) * (1 + ((0.00000009*(DMG['ElementMastery']) ** 3 - 0.0002767 * (DMG['ElementMastery']) ** 2 + 0.46647865 * DMG['ElementMastery'] + 0.19667643) / 100)) * (1 - DMG['Resist'] / 100) // 1)}")
   print(f"Сверхпроводник: {((-0.0000000358 * DMG['lvl'] ** 5 - 0.0000066577 * DMG['lvl'] ** 4 + 0.0022024037 * DMG['lvl'] ** 3 - 0.0725311152 * DMG['lvl'] ** 2 + 2.4686924073 * DMG['lvl'] ** 1 + 2.3057129474) * (1 + ((0.00000009*(DMG['ElementMastery']) ** 3 - 0.0002767 * (DMG['ElementMastery']) ** 2 + 0.46647865 * DMG['ElementMastery'] + 0.19667643) / 100)) * (1 - DMG['Resist'] / 100) // 1)}")
   print(f"Раскол: {((-0.0000006049 * DMG['lvl'] ** 5 + 0.0001047983 * DMG['lvl'] ** 4 - 0.0043965215 * DMG['lvl'] ** 3 + 0.1820369869 * DMG['lvl'] ** 2 + 2.1519084104 * DMG['lvl'] ** 1 + 18.8990018066) * (1 + ((0.00000009*(DMG['ElementMastery']) ** 3 - 0.0002767 * (DMG['ElementMastery']) ** 2 + 0.46647865 * DMG['ElementMastery'] + 0.19667643) / 100)) * (1 - DMG['Resist'] / 100) // 1)}")
   print(f"Рассеивание: {((-0.0000002536 * DMG['lvl'] ** 5 + 0.0000405303 * DMG['lvl'] ** 4 - 0.0013084062 * DMG['lvl'] ** 3 + 0.047581148 * DMG['lvl'] ** 2 + 1.2495045779 * DMG['lvl'] ** 1 + 5.7189041107) * (1 + ((0.00000009*(DMG['ElementMastery']) ** 3 - 0.0002767 * (DMG['ElementMastery']) ** 2 + 0.46647865 * DMG['ElementMastery'] + 0.19667643) / 100)) * (1 - DMG['Resist'] / 100) // 1)}\n")

def menu(DMG: dict) -> None:
   os.system("cls")
   print("Это программа для подсчёта урона геншина:")
   show_damage(DMG)
   options = [
		["Редактировать силу атаки", "сила атаки"],
		["Редактировать крит шанс", "крит шанс"],
		["Редактировать крит урон", "крит урон"],
		["Редактировать множитель урона таланта(%)", "талант"],
		["Редактировать множитель бонусного урона(%)", "бонус урона"],
		["Редактировать мастерство стихий", "МС"],
		["Редактировать уровень персонажа", "уровень"],
		["Редактировать уровень противника", "уровень противника"],
		["Редактировать сопротивление противника", "сопротивление"],
		["Редактировать снижение сопротивления противника", "снижение сопротивления"],
      ["Указать особые множители урона(Они есть у Сяо, Итто, Сайно и тд.)", "тодо"]
	]
   for num, option in enumerate(options, 1):
      print(f"{num}.{option[0]}")
   user_option = input("\nВведите номер варианта и нажмите ENTER: ")
   if user_option.isdigit():
      idx = int(user_option) - 1
   else:
      print("Ошибка! Введенны не коректные данные")
      input("Нажмете ENTER чтобы продолжить: ")
      return menu(DMG)
   if options[idx][1] == "сила атаки":
      edit_stats(DMG, "AttackPower")
   elif options[idx][1] == "крит шанс":
      edit_stats(DMG, "CritChance")
   elif options[idx][1] == "крит урон":
      edit_stats(DMG, "CritDamage")
   elif options[idx][1] == "талант":
      edit_stats(DMG, "TalentMultiplayer")
   elif options[idx][1] == "бонус урона":
      edit_stats(DMG, "BonusDMG")
   elif options[idx][1] == "МС":
      edit_stats(DMG, "ElementMastery")
   elif options[idx][1] == "уровень":
      edit_stats(DMG, "lvl")
   elif options[idx][1] == "уровень противника":
      edit_stats(DMG, "Enemylvl")
   elif options[idx][1] == "сопротивление":
      edit_stats(DMG, "Resist")
   elif options[idx][1] == "снижение сопротивления":
      edit_stats(DMG, "DebuffResist")
   elif options[idx][1] == "тодо":
      print("Эта функция ещё не доделанна")
      input("Нажмете ENTER чтобы продолжить: ")
      return menu(DMG)
   
def edit_stats(DMG: dict, characteristic) -> None:
      stat = input("\nВведите значение характеристики: ")
      if stat.isdigit():
         DMG[characteristic] = int(stat)
         return menu(DMG)
      else:
         print("Ошибка! Введенны не коректные данные")
         input("Нажмете ENTER чтобы продолжить: ")
         return menu(DMG)

menu(DMG)