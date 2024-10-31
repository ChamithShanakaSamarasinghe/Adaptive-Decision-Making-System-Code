class DecisionMaker:
    def __init__(self):
        self.rules = {
            'low_budget': self.handle_low_budget,
            'medium_budget': self.handle_medium_budget,
            'high_budget': self.handle_high_budget
        }
    
    def handle_low_budget(self):
        print("Decision: Suggest free or low-cost activities.")

    def handle_medium_budget(self):
        print("Decision: Suggest affordable options, like local tours or activities.")

    def handle_high_budget(self):
        print("Decision: Suggest premium experiences, such as luxury hotels or exclusive events.")

    def make_decision(self, budget):
        if budget < 100:
            self.rules['low_budget']()
        elif 100 <= budget < 500:
            self.rules['medium_budget']()
        else:
            self.rules['high_budget']()

def main():
    print("Welcome to the Adaptive Decision-Making System")
    
    while True:
        try:
            budget = float(input("Enter your budget for activities (or type 'exit' to quit): "))
            decision_maker = DecisionMaker()
            decision_maker.make_decision(budget)
        except ValueError:
            print("Invalid input. Please enter a number or type 'exit' to quit.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
