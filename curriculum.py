#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

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id 
        self.curriculums = []

    def __str__(self):
        return f"{self.name} {self.id}"
    
    def add_curriculum(self,curriculum):
        if isinstance(curriculum, Curriculum):
            self.curriculums.append(curriculum)
            print(f"Student {self.name} has added curriculum \'{curriculum.name}\'.")
        else:
            print("Invalid - Please provide an existing curriculum.")

    def remove_curriculum(self,curriculum_string):
        if curriculum_string != "":
            for curriculum in self.curriculums:
                if curriculum.name == curriculum_string:
                    self.curriculums.remove(curriculum)
                else:
                    print("Invalid - curriculum not located.")

        else:
            print("Invalid - Please provide an existing curriculum.")
    
    def list_curriculums(self):
        for c in self.curriculums:
            print(f"Student {self.name} is following curriculum \'{c.name}\'.")

class Curriculum:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.topics = []

    def add_topic(self, topic_string):
        if topic_string != "":
            self.topics.append(topic_string)
            print(f"topic \'{topic_string}\' has been added to the curriculum \'{self.name}\'.")
        else:
            print("Invalid - Please provide a topic sentence.")

    def remove_topic(self, topic_string):
        if topic_string != "":
            for topic in self.topics:
                if topic == topic_string:
                    self.topics.remove(topic_string)
                else:
                    print("Invalid - curriculum topic not located.")

        else:
            print("Invalid - Please provide a topic sentence.")

    def list_topics(self):
        if not self.topics:
            print("There are currently no topics in this curriculum.")
        else:
            print("Curriculum topics:")
            for topic in self.topics:
                print(topic)

# Create some studnet objects
student1 = Student("John Smith",1)
student2 = Student("Doja Cat",2)

# Create some curriculums and add some topics to it 
curriculum1 = Curriculum("The Early Roman Empire",1)
curriculum1.add_topic("Rome's Founding")
curriculum1.add_topic("The Punic Wars")
curriculum1.add_topic("Fall of the Republic")

curriculum2 = Curriculum("How to make a PBJ",1)
curriculum2.add_topic("Peanuts")
curriculum2.add_topic("Making the jam")
curriculum2.add_topic("Appropriate Breads")

# add curriculums for individual students
student1.add_curriculum(curriculum1)
student1.add_curriculum(curriculum2)
student2.add_curriculum(curriculum2)

# List cars in the garage after removal
student1.list_curriculums()
student2.list_curriculums()

