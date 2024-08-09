class Student:
  def __init__(self, distance_from_school, age, has_right_to_stay, pays_international_fees):
        self.distance_from_school = distance_from_school
        self.age = age
        self.has_right_to_stay = has_right_to_stay
        self.pays_international_fees = pays_international_fees

    def can_enroll(self):
        if self.distance_from_school < 4 and self.age < 18 and self.has_right_to_stay:
            return "The student can enroll."
        elif self.age < 18 and self.pays_international_fees:
            return "The student can enroll as an international student."
        else:
            return "The student cannot enroll."