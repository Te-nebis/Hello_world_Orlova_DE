phenotype_donor = input("Введите фенотип группы крови донора(I, II, III, IV): ").strip().upper()
phenotype_recipient = input("Введите фенотип группы крови пациента(реципиента) (I, II, III, IV): ").strip().upper()

if phenotype_donor == "I" and phenotype_recipient == "I":
    print("Переливание возможно")
elif phenotype_donor == "II" and phenotype_recipient == "II":
    print("Переливание возможно")
elif phenotype_donor == "III" and phenotype_recipient == "III":
    print("Переливание возможно")
elif phenotype_donor == "IV" and phenotype_recipient == "IV":
    print("Переливание возможно")
elif phenotype_donor == "I" and phenotype_recipient == "II":
    print("Переливание возможно")
elif phenotype_donor == "I" and phenotype_recipient == "III":
    print("Переливание возможно")
elif phenotype_donor == "I" and phenotype_recipient == "IV":
    print("Переливание возможно")
else:
    print("Переливание невозможно")