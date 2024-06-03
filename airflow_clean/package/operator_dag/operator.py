from airflow.models import BaseOperator
from ..function import function

class MyOperator1(BaseOperator):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        message = f"Hello {self.name}"
        print(message)
        return message
    
class MyOperator2(BaseOperator):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        function.some_function_1()
        function.some_function_1()
        function.some_function_1()
        function.some_function_1()