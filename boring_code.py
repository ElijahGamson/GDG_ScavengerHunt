#Starting boring project
def scavenger_hunt() -> None:
    i = 0
    while i < 10:
        print("Hello World!")

    return None

class Course:
    """
        An instance of a PSU course
        Attributes: name of the course (str), # of credits (int)
    """
    def __init__(self, course_name, n_credits):
        self.name = course_name
        self.credits = n_credits

    def __str__(self):
        return f"{self.name} ({self.credits})"
    
class Student:
    """
        An instance of a PSU student
        Attributes: 
        psu_id [str]: email id
        course [list]: list of Course objects
        total_credits [int]: total credits for student enrollment
        major [str]: major code
    """

    def __init__(self, psu_id, major = 'PREMJ'):
        self.psu_id = psu_id
        self.courses = []
        self.total_credits = 0
        self.major = major

    #Do not look at (hint for next clue)

    def enroll(self, new_course):
        if self.total_credits + new_course.credits > 15:
            return 'Full Schedule'
        else:
            self.courses.append(new_course)
            self.total_credits += new_course.credits
            print(f"Welcome to {new_course.name}!")

    def drop(self, course_name):
        for course in self.courses:
            if course_name == course.name:
                self.total_credits -= course.credits
                self.course.remove(course)
                print('Course dropped :(')