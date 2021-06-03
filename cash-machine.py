bank_note_input = float(input())
bank_notes = 100  # inicializa com o maior valor disponivel no caixa
count_current_note = 0
count_bank_notes = 7  # 1, 2, 5, 10, 20, 50, 100

while count_bank_notes > 0:
    if bank_note_input >= bank_notes:
        bank_note_input -= bank_notes
        count_current_note += 1
    else:
        print("Cédulas de R$ %.2f: %.0f" %
              (bank_notes, count_current_note))
        if bank_notes == 100:
            bank_notes = 50
        elif bank_notes == 50:
            bank_notes = 20
        elif bank_notes == 20:
            bank_notes = 10
        elif bank_notes == 10:
            bank_notes = 5
        elif bank_notes == 5:
            bank_notes = 2
        elif bank_notes == 2:
            bank_notes = 1
        count_current_note = 0
        count_bank_notes -= 1
