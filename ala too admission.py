def main():
    last_name = input("Write your last name: ")
    first_name = input("Write your first name: ")

    print("Do you have a school certificate? ")
    print("0 - Not available")
    print("1 - Available")
    certificate_choice = input("Write your choice (0 or 1): ")

    if certificate_choice == '1':
        your_certificate = True
    elif certificate_choice == '0':
        your_certificate = False
    else:
        print("Invalid choice.")
        return

    ort_score = int(input("Write your ORT score: "))

    print("Your English level: ")
    print("1 - A1")
    print("2 - A2")
    print("3 - B1")
    print("4 - B2")
    print("5 - C1")
    print("6 - C2")

    english_choice = input("Your choice (1-6): ")

    if english_choice in ['3', '4', '5', '6']:
        english_level = True
    else:
        english_level = False

    if not your_certificate:
        print("You need a school certificate.")
        return

    if ort_score < 110:
        print("You need to pass the ORT again.")
        return

    if not english_level:
        print("You can study at the preparation school.")
        return

    print("Congratulations! You have met all requirements for admission.")

    specialties = {
        "Computer Engineering": 2500,
        "Artificial Intelligence": 2200,
        "Psychology": 1900,
        "Journalism": 1700,
        "International Relations": 2200,
        "Law": 1800,
        "Management": 2200,
        "Medicine": 3300
    }

    print("Choose your specialty:")
    for i, specialty in enumerate(specialties, start=1):
        print(f"{i} - {specialty} (${specialties[specialty]})")

    specialty_choice = int(input("Choose your specialty (1-8): "))
    selected_specialty = list(specialties.keys())[specialty_choice - 1]
    tuition_fee = specialties[selected_specialty]

    # Calculate discount
    discount = 0
    if 140 <= ort_score <= 155:
        discount = 0.05
    elif 156 <= ort_score <= 174:
        discount = 0.10
    elif 175 <= ort_score <= 199:
        discount = 0.25
    elif 200 <= ort_score <= 209:
        discount = 0.50
    elif 210 <= ort_score <= 218:
        discount = 0.75
    elif 219 <= ort_score <= 240:
        discount = 1.00

    final_tuition_fee = tuition_fee * (1 - discount)

    # Final message
    if discount > 0:
        print(
            f"Dear {first_name} {last_name}, you have been admitted to the {selected_specialty} program. Your tuition fee is ${final_tuition_fee:.2f} per year after a {int(discount * 100)}% discount.")
    else:
        print(
            f"Dear {first_name} {last_name}, you have been admitted to the {selected_specialty} program. Your tuition fee is ${final_tuition_fee:.2f} per year.")


if __name__ == "__main__":
    main()
