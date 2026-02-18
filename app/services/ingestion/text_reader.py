file_path = "data/uploads/3af13411-5e3a-4427-9e98-bce469b2db15_SemWise_Grades.txt"

def read_text_file(file_path: str) -> str:
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            if(not text):
                return
            return text
    else:
        print({"error": "The file is not a text file."})