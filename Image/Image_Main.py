def main():
    algorithm = int(input("1. LSB\n2. BPCS\nPilih Algoritma yang digunakan:"))

    if(algorithm == 1):
        random = int(input(
            "1. Sequential\n2. Random\nPilih sequential atau random: "))
        if(random == 1):
            import LSB_Seq
        elif(random == 2):
            import LSB_Rand
        else:
            raise Exception("Enter correct input")

    elif (algorithm == 2):
        random = int(input(
            "1. Sequential\n2. Random\nPilih sequential atau random: "))
        if(random == 1):
            import BPCS_Seq
        elif(random == 2):
            import BPCS_Rand
        else:
            raise Exception("Enter correct input")

    else:
        raise Exception("Enter correct input")


main()
