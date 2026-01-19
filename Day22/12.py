# Create a KBC game simulation


class question:
    print("\n********Welcome To KBC*********")
    question = {
        1: "What is the capital of France?",
        2: "What is 2 + 2?",
        3: "What is the largest planet in our solar system?",
        4: "Who is the best teacher in QSpider?",
        5: "What is the boiling point of water?",
        6: "What is the chemical symbol for Gold?",
        7: "What is 4-2?",
        8: "What is the smallest prime number?",
        9: "What is the full form of OOPS",
    }
    option = {
        1: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        2: ["A. 3", "B. 4", "C. 5", "D. 6"],
        3: ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        4: [
            "A. Sambhu sir",
            "B. Deepak Sir",
            "C. Saurav sir ",
            "D. Aakash sir",
        ],
        5: ["A. 90°C", "B. 100°C", "C. 110°C", "D. 120°C"],
        6: ["A. Au", "B. Ag", "C. Fe", "D. Hg"],
        7: [
            "A. 5",
            "B. 3",
            "C. 2",
            "D. 1",
        ],
        8: ["A. 0", "B. 1", "C. 2", "D. 3"],
        9: [
            "A. Object Oriented Public Systum",
            "B. Object Oriented Programing Systum",
            "C. Output Oriented Programing Systum",
            "D. Oriented Object Programing Systum",
        ],
    }
    answer = {
        1: "Cc",
        2: "Bb",
        3: "Bb",
        4: "Bb",
        5: "Bb",
        6: "Aa",
        7: "Cc",
        8: "Cc",
        9: "Bb",
    }
    amount = {
        1: 1000,
        2: 2000,
        3: 3000,
        4: 5000,
        5: 10000,
        6: 20000,
        7: 40000,
        8: 80000,
        9: 90000,
    }


class kbc(question):
    def __init__(self, name, age, phone, winning_amt=0):
        self.name = name
        self.age = age
        self.phone = phone
        self.winning_amt = winning_amt

    def ask(self):
        for i in range(1, len(self.question) + 1):
            print(self.question[i])
            print(self.option[i])
            ans = input("Answer: ")
            if ans in self.answer[i]:
                print("\n Right Answer...!")
                self.winning_amt += self.amount[i]
                print(f"Balance: {self.winning_amt}\n")

            else:
                print("\n Wrong Answer...!")
                print(f"Winning Amount: {self.winning_amt}\n")
                break

    def display(self):
        print(f"Winning Ammont Of Yours is {self.winning_amt}")


p1 = kbc("Nasir", 23, 8234324324)
p1.ask()
p1.display()
