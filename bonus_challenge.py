class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_people = set([])

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        self.unique_people.add(other_person.name)

    def print_contact_info(self):
        print self.name, self.email, self.phone

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        return len(self.friends)

    def __repr__(self):
        return '%s reporting for duty!' % self.name

    def num_unique_people_greeted(self):
        friend_count = 0
        for friend in self.unique_people:
            friend_count += 1
        print friend_count

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
mark = Person('Mark', 'mark@aol.com', '234-555-5555')
jacob = Person('Jacob', 'jacob@aol.com', '666-666-6666')


#sonny.num_unique_people_greeted()

sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(mark)
sonny.greet(jacob)
sonny.greet(mark)
sonny.greet(jordan)
sonny.greet(jacob)

sonny.num_unique_people_greeted()
