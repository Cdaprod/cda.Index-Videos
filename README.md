# Index-Videos

## Got loose videos somewhere? Find them!

### Index a drive from anywhere… from the command-line to the cloud!!

---

## What Does This Do?

This toolkit provides a comprehensive guide and codebase for indexing videos from any storage location, be it your local machine or the cloud. It extracts essential metadata and even frame data for AI analysis. All this data can be stored in a Supabase database and then used for vectorized querying through Weaviate.

---

## How Does It Work?

```mermaid
classDiagram
    Indexing --|> FrameExtraction : extracts frames
    FrameExtraction --|> Supabase : stores in Supabase
    Supabase --|> Weaviate : indexes in Weaviate
    Weaviate --|> User : serves to user
```

1. **Indexing**: Scans through directories to find video files and extracts essential metadata.
2. **FrameExtraction**: Captures frames from the video files for further analysis.
3. **Supabase**: Holds the metadata and frame data in a structured database.
4. **Weaviate**: Allows for vectorized querying of this complex data.
5. **User**: Can access and query this rich dataset.

---

## How to Use

1. Clone the repository.
2. Install the required Python packages.
3. Set up your Supabase and Weaviate instances.
4. Run the indexing script to populate your Supabase table.
5. Utilize the included notebooks for further data analysis and Weaviate integration.

---

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Open a pull request.

---

## Special Note

Refactoring life's data into a structured schema opens up a world of possibilities. From video and image content to client and target marketing data, it all comes together with a vector database like Weaviate. The high point is AI agents using this as a toolkit, making this not just a project, but a significant asset in data management and AI.