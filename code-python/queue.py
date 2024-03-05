class Queue:
    def __init__(self):
        self.people = []

    def is_empty(self):
        return len(self.people) == 0

    def enqueue(self, person):
        self.people.append(person)

    def dequeue(self):
        if not self.is_empty():
            return self.people.pop(0)
        else:
            print("Queue is empty.")
            return None

    def size(self):
        return len(self.people)

# Function to simulate the bakery queue
def bakery_queue():
    queue = Queue()

    while True:
        print("\nBakery Queue Operations:")
        print("1. Arrive (Add person to queue)")
        print("2. Leave (Remove person from queue)")
        print("3. View Queue")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter person's name: ")
            order = input("Enter person's order: ")
            person = {"name": name, "order": order}
            queue.enqueue(person)
            print(f"{name} with order '{order}' has arrived and joined the queue.")

        elif choice == "2":
            if not queue.is_empty():
                leaving_person = queue.dequeue()
                print(f"{leaving_person['name']} with order '{leaving_person['order']}' has left the queue.")
            else:
                print("Queue is empty.")

        elif choice == "3":
            if not queue.is_empty():
                print("Current Bakery Queue:")
                for idx, person in enumerate(queue.people, start=1):
                    print(f"{idx}. {person['name']} - Order: {person['order']}")
            else:
                print("Queue is empty.")

        elif choice == "4":
            print("Exiting the bakery queue simulation.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Run the bakery queue simulation
bakery_queue()
