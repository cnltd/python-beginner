# find if a sutudent is paas or fail in a subject

def result(mark):
    if mark >= 50:
        return "PASSED"
    else:
        return "FAILED"

def addition(num1,num2):
    return num1+num2

class exam:
    """
    This class takes student details and calculates the result in each subject and total
    
    [variables]
    name        <string>
    id          <int>
    math        <int>
    phy         <int>
    che         <int>
    
    [returns]
    result      <str>
    total       <int>
    """
    def __init__(self, name, math, phy):
        self.name = name
        self.math = math
        self.phy = phy

    def final_result(self):
        # Calculate if pass or fail in maths
        math_res = result(mark=self.math)

        # Calculate if pass or fail in Physics
        phy_res = result(mark=self.phy)

        #Print final output
        print(f"{self.name} has {math_res} in MATHS with {self.math} marks")
        print(f"{self.name} has {phy_res} in MATHS with {self.phy} marks")
    
    def total(self):
        my_total = addition(num1=self.math, num2=self.phy)
        # Rajesh has a grand total of 150 out of 2 subjects
        print(f"{self.name} has a grand total of {my_total} out of 2 subjects")


student1 = exam(name="Rajesh", math = 75, phy=65)

student1.final_result()
student1.total()

print("################################################")

student2 = exam(name="Satya", math = 100, phy=55)
# student2.final_result()
student2.total()
