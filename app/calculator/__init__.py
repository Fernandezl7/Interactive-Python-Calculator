from decimal import Decimal
from typing import Callable
from app.calculator.calculations import Calculations
from app.calculator.calculation import Calculation
from app.calculator.operations import add,subtract,multiply,divide

class Calculator:
    @staticmethod
    def _perform_operation(a:Decimal,b:Decimal,operation: Callable[[Decimal,Decimal],Decimal])-> Decimal:
        calculation= Calculation.create(a,b,operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()
    @staticmethod
    def add(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operation(a,b,add)
    @staticmethod
    def subtract(a:Decimal,b:Decimal)-> Decimal:
        return Calculator._perform_operation(a,b,subtract)
    @staticmethod
    def multiply(a:Decimal,b:Decimal)->Decimal:
        return Calculator._perform_operation(a,b,multiply)
    def divide(a:Decimal,b:Decimal)-> Decimal:
        return Calculator._perform_operation(a,b,divide)
    