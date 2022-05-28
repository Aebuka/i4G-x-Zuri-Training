class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    # methods
    def change_name(newName, name):
        newName.name = name
        print(newName.name)
    def change_age(newAge, age):
        newAge.age = age
        print(newAge.age)
    def add_track(newTracks, tracks):
        newTracks.tracks = tracks
        print(newTracks.tracks)
    def get_score(newScore, score):
        newScore.score = score
        print(newScore.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(29.03)
