from abc import ABC, abstractmethod

class DriverExam:
    @staticmethod
    def execute_exercise(exercise):
        """
        :param exercise: (object) The object of a class
            implementing ExerciseInterface
        """
        try:
            exercise.start()
            exercise.execute()
        except:
            exercise.mark_negative_points()
        finally:
            exercise.end()

class ExerciseInterface(ABC): 
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
      
    @abstractmethod
    def mark_negative_points(self):
        pass
      
    @abstractmethod
    def end(self):
        pass
    
class Exercise(ExerciseInterface):
    def start(self):
        print("start")
    def execute(self):
        print("execute")
    def mark_negative_points(self):
        print("mark_negative_points")
    def end(self):
        print("end")
    
print(DriverExam().execute_exercise(Exercise()))