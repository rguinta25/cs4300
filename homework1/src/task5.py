def fav_books():
    books = [
        "A Tale of Two Cities by Charles Dickens", 
        "The Alchemest by Paulo Coelho", 
        "Harry Potter by J. K. Rowling",
        "Diary of a Wimpy Kid by Jeff Kinney",
        "Green Eggs and Hamm by Dr. Seuss"]

    return books[:3]

def student(id):
    student_dict = {
        "Carl Jones" : 1,
        "Rayne Guinta" : 2,
        "Tiger Woods" : 3,
        "Bruce Wayne" : 4
    }

    for key, value in student_dict.items():
        if value == id:
            return key

    else:
            return "student doesn't exist"

            
if __name__ == "__main__":
    print(fav_books())
    print("The student is: ", student(2))
