studentsCourse = int(input("How many students on the course?: "))

groupSize = int(input("Desired group size?: "))

groupsFormed = studentsCourse // groupSize

esPar = studentsCourse % groupSize




if esPar == 0:
    print(f"Number of groups formed: {groupsFormed} ")
else:
    print(f"Number of groups formed: {int(groupsFormed)+1}")
