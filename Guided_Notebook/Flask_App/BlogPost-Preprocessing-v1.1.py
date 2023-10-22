#!/usr/bin/env python
# coding: utf-8

# ---

# In[1]:


import weaviate

client = weaviate.Client("http://192.168.0.25:8082")

# Delete the existing class
# client.schema.delete_class("BlogPost")

# Define the new_schema by creating the object with keys:value pairs for classname and properties
# new_schema = {
#     "class": "BlogPost",
#     "properties": [
#         {
#             "name": "title",
#             "dataType": ["string"]
#         },
#         {
#             "name": "content",
#             "dataType": ["string"]
#         },
#         {
#             "name": "author",
#             "dataType": ["string"]
#         }
#     ]
# }

# # Call the client.schema with the .create_class function
# client.schema.create_class(new_schema)

# Open the json data and load it as posts_data 
with open("posts_data.json") as f:
    posts_data = json.load(f)

# Iterate through the post objects in posts_data with the .create function
for post in posts_data:
    client.data_object.create(post, "BlogPost")

# Build and execute the query to retrieve all BlogPost objects with specific properties
blog_posts_query = client.query.get('BlogPost', properties=["title", "author", "content"]).do()

# Accessing Retrieved Data for post in blog_posts_query
for post in blog_posts_query['data']['Get']['BlogPost']:
    title = post['title']
    content = post['content']
    author = post['author']
    print(f"Title: {title}\nAuthor: {author}\nContent: {content}\n")

