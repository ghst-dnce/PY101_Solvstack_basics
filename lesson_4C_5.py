set_of_banks = {'Chase', 'TD Bank', 'Simple', 'Capital One', 'Ally', 'Wells Fargo'}
set_of_banks.discard("Starbucks")

set_of_banks.remove("Wells Fargo")
print(set_of_banks)

set_of_banks.discard("Ally")
print(set_of_banks)

one_bank = set_of_banks.pop()
print(one_bank)
print(set_of_banks)

set_of_banks.clear()
print(set_of_banks)