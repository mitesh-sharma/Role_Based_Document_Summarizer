from app.services.rag_pipeline import generate_role_based_summary
from app.helpers.calculate_max_words import calculate_max_words

def main():
    file_path = "data/uploads/3af13411-5e3a-4427-9e98-bce469b2db15_SemWise_Grades.txt"
    role_description = 'I am a devops/deployment engineer'
    
    #Detail level 0/1 - concise/detailed
    detail_level = 1

    #Calculating the length of the file (Currently txt file)
    length = 0
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            length = len(text.split())
    print('length of file - ', length, f'\n')
    
    #Calculate the maximum words for output
    max_words = calculate_max_words(length, detail_level)

    results = generate_role_based_summary(
    max_words,
    file_path=file_path,
    role_description = role_description,
    
    )

    if(results):
        print(f"Role description - {role_description}\n")
        print(results)

if __name__ == "__main__":
    main()



