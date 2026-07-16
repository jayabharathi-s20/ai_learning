from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

youtube_url = "https://www.youtube.com/watch?v=LPZh9BOjkQs"

loader = YoutubeLoader.from_youtube_url(
    youtube_url,
    add_video_info=False
)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}")
    print(chunk.page_content)
    print("-" * 80)