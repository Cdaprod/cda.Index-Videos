from pydantic import BaseModel
from functools import wraps

class BaseTool:
    def execute(self):
        pass

class LangChainTool(BaseTool, BaseModel):
    input_str: str

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print(f"Before: {self.input_str}")
            result = func(self, *args, **kwargs)
            print(f"After: {result}")
            return result
        return wrapper

    @decorator
    def execute(self):
        # Perform some operations on the input_str
        transformed_str = self.input_str.upper()
        return transformed_str

# Usage example
if __name__ == "__main__":
    tool = LangChainTool(input_str="example")
    tool.execute()
