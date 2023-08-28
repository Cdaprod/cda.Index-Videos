from functools import wraps
import logging
from supabase_py import create_client
from weaviate import Client, AuthClientSecret
import os

# BaseTool class
class BaseTool:
    def execute(self, input_data: str) -> str:
        pass

# LangChainTool class for indexing
class LangChainIndexingTool(BaseTool):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
        # Initialize Supabase client
        self.supabase_url = "your-supabase-url"
        self.supabase_key = "your-supabase-key"
        self.supabase = create_client(self.supabase_url, self.supabase_key)
        
        # Initialize Weaviate client
        self.weaviate_url = "your-weaviate-url"
        self.auth = AuthClientSecret("your-client-id", "your-client-secret")
        self.weaviate_client = Client(self.weaviate_url, self.auth)

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print(f"Before: {args[0]}")
            result = func(self, *args, **kwargs)
            print(f"After: {result}")
            return result
        return wrapper

    @decorator
    def run(self, target_directory: str) -> str:
        logging.info(f"Indexing target directory: {target_directory}")
        
        for root, _, files in os.walk(target_directory):
            for filename in files:
                # Prepare data for Supabase
                supabase_data = {
                    'Filename': filename,
                    'Source Path': os.path.join(root, filename)
                }
                # Insert into Supabase
                self.supabase.table('video-index').insert([supabase_data]).execute()
                
                # Prepare data for Weaviate
                weaviate_data = {
                    'filename': filename,
                    'sourcePath': os.path.join(root, filename)
                }
                # Add to Weaviate
                self.weaviate_client.data_object().create(weaviate_data, 'Video')
        
        return "Indexing completed"

# Usage in the given example
if __name__ == "__main__":
    from langchain.agents.tools import Tool

    langchain_indexing_tool = LangChainIndexingTool(name="LangChainIndexing", description="Indexes a target directory and interacts with databases")
    tool = Tool(
        name=langchain_indexing_tool.name,
        func=langchain_indexing_tool.run,
        description=langchain_indexing_tool.description
    )
    tool.execute("your-target-directory")
