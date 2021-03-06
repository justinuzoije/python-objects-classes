class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    def print_contact_info(self):
        print self.name, self.email, self.phone

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        return len(self.friends)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# sonny.greet(jordan)
# jordan.greet(sonny)

# sonny.print_contact_info()
# jordan.print_contact_info()

jordan.add_friend(sonny)

print jordan.num_friends()
