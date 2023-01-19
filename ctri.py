class Control:
    
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    
    def calculate(self):
        num1 = float(self.view.le1.text())
        num2 = float(self.view.le2.text())
        operator = self.view.cb.currentText()
        
        if operator == '+':
            return f'{num1} + {num2} = {self.sum(num1,num2)}'
        elif operator == '-':
            return f'{num1} - {num2} = {self.subtraction(num1, num2)}'
        elif operator == '*':
            return f'{num1} * {num2} = {self.multiple(num1, num2)}'
        else:
            return "Calculation Error...(err_calculate)"  #distinguish Calculation Error message
    
    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda:\
            self.view.setDisplay(self.calculate())) #change activateMessage to setDisplay
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):
        try:
            return a+b
        except:
            return "Calculation Error...(err_sum)" #Sum Error message

    def subtraction(self, a, b):
        try:
            return a-b
        except:
            return "Calculation Error...(err_subtraction)" #subtraction error Message
    
    def multiple(self, a, b):
        try:
            return a*b
        except:
            return "Calculation Error...(error_multiple)"


