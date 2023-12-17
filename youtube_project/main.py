
import langchain_helper as lch

youtube_url="https://www.youtube.com/watch?v=O5xeyoRL95U&t=39s"
query="Can you summarize for me this transcripte?"

db = lch.create_db_from_youtube_video_url(youtube_url)
response, docs = lch.get_response_from_query(db, query)
        
print(response)
    