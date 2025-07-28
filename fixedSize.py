from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap = 2,
    separator="**",
)

text = "This is a sample ** text that we will use ** to demonstrate the fixed size chunking functionality**. It will be split into smaller chunks ** based on the specified size and overlap. This allows for better processing **and analysis of the text data. ** Each chunk will contain ** a portion of the text ** with some overlap ** to ensure context is preserved."

chunks = splitter.split_text(text)

print(chunks)