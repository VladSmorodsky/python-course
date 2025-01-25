class Person:
    """Represents Person class
    Attributes:
        - name -> str: person's name
        - age -> int: person's age
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __lt__(self, compared_person: 'Person') -> bool:
        """Check if current person's object age less than compared person's age.
        :param compared_person: Compared Person object
        """
        return self.age < compared_person.age

    def __eq__(self, compared_person: 'Person') -> bool:
        """Check if current person's object age equals to compared person's age.
        :param compared_person: Compared Person object
        """
        return self.age == compared_person.age

    def __gt__(self, compared_person: 'Person') -> bool:
        """Check if current person's object age greater than compared person's age.
        :param compared_person: Compared Person object
        """
        return self.age > compared_person.age

    def __repr__(self) -> str:
        """Represents person object"""
        return f"{self.__dict__}"


def sort_persons_by_age(person: 'Person') -> int:
    """Function for sorting person list by age"""
    return person.age


p1 = Person('Peter', 18)
p2 = Person('Tim', 19)
p3 = Person('Pablo', 17)
p4 = Person('Carl', 20)

person_list = [p1, p2, p3, p4]
person_list.sort(key=sort_persons_by_age)
print(person_list)
