def main():
    stories = [
        {
            'title': 'Space Adventure',
            'prompts': [
                ('name', 'Enter a astronaut name: '),
                ('planet', 'Enter a planet name: '),
                ('alien', 'Enter an alien species: '),
                ('verb', 'Enter a verb: '),
                ('food', 'Enter a weird food: '),
                ('emotion', 'Enter an emotion: ')
            ],
            'template': """\n🚀 {name} blasted off to planet {planet} for an important mission. 
While exploring the surface, a group of {alien} appeared! They started {verb} furiously. 
After communicating through dance, {name} shared {food} with them. 
Everyone felt {emotion} and formed an interstellar alliance! 🌌"""
        },
        {
            'title': 'Magical Quest',
            'prompts': [
                ('hero', 'Enter a hero name: '),
                ('magic_item', 'Enter a magical item: '),
                ('creature', 'Enter a mythical creature: '),
                ('spell', 'Enter a magic spell: '),
                ('location', 'Enter a magical location: '),
                ('adjective', 'Enter an adjective: ')
            ],
            'template': """\n✨ The brave {hero} embarked on a quest to find the {magic_item}. 
They encountered a {creature} guarding the ancient {location}. 
With a shout of "{spell}!", the {creature} transformed into a {adjective} butterfly. 
Peace was restored to the realm! 🏰"""
        },
        {
            'title': 'Startup Drama',
            'prompts': [
                ('ceo', 'Enter a CEO name: '),
                ('tech', 'Enter new technology: '),
                ('animal', 'Enter a spirit animal: '),
                ('exclamation', 'Enter an exclamation (ALL CAPS): '),
                ('number', 'Enter a crazy valuation: '),
                ('adjective', 'Enter an adjective: ')
            ],
            'template': """\n💻 {ceo} launched a startup called {tech}Hub. 
During a pitch meeting, a {animal} stormed in shouting "{exclamation}!". 
Investors went wild, valuing the company at ${number} billion. 
The {adjective} revolution had begun! 📈"""
        }
    ]

    while True:
        print("\n" + "🌟" * 20)
        print("       MAD LIBS EXTREME!")
        print("🌟" * 20 + "\n")

        print("Choose your adventure:")
        for idx, story in enumerate(stories, 1):
            print(f"{idx}. {story['title']}")
        print("0. Exit program\n")

        while True:
            try:
                choice = int(input("Enter story number (0-{}): ".format(len(stories))))
                if choice == 0:
                    print("\nThanks for playing! 🎉")
                    return
                if 1 <= choice <= len(stories):
                    selected_story = stories[choice-1]
                    break
                raise ValueError
            except ValueError:
                print(f"Please enter a number between 0-{len(stories)}")

        print("\n" + "📝" * 20)
        print(f"Time to create: {selected_story['title']}")
        print("Provide these awesome inputs:\n")

        answers = {}
        for key, prompt in selected_story['prompts']:
            answers[key] = input(prompt).strip()

        print("\n" + "📖" * 20)
        print("YOUR EPIC STORY:")
        print(selected_story['template'].format(**answers))
        print("📖" * 20 + "\n")

        if input("Play again? (y/n): ").lower() != 'y':
            print("\nThanks for playing! Keep being awesome! 😎")
            break

if __name__ == "__main__":
    main()