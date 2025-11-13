Web_Development = ["Mathew", "Asha", "Alice"]
Data_Science = ["Bob", "Eve", "Charlie"]
UI_UX = ["David", "Fiona", "Grace"]
all_participants = [Web_Development , Data_Science ,UI_UX]
print("\n All participants:", all_participants)
Web_Development.append("Hannah")
print("\nUpdated Web Development participants:", Web_Development)
Data_Science.insert(1, "Ivan")
print("\nUpdated Data Science participants:", Data_Science)
UI_UX.pop()
print("\nUpdated UI/UX participants:", UI_UX)
Data_Science_copy = Data_Science.copy()
print("\nCopied Data Science participants:", Data_Science_copy)
Data_Science.clear()
print("\nCleared Data Science participants:", Data_Science)
print("\nFirst two participants in Web Development:", Web_Development[:2])
name_lengths = [len(name) for name in Data_Science_copy]
print("\nName lengths in Data Science copy:", name_lengths)
if "Asha"  in Web_Development or "Asha" in Data_Science_copy or "Asha" in UI_UX:
    print("\nParticipant 'Asha' is enrolled.")
else:
    print("\nParticipant 'Asha' is not enrolled.")
first_participants = (Web_Development[0], Data_Science_copy[0], UI_UX[0])
print("\nFirst participants from each course:", first_participants)
