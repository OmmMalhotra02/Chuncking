# It is used to split large documents into paragraphs, then splitted to words with preserving context/meaning of the text.
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
    separators=[],
)

text = "This is a sample text that we will use to demonstrate the fixed size chunking functionality based on the specified size and overlap. It will be split into smaller chunks based on the specified size and overlap. This allows for better processing and analysis of the text data based on the specified size and overlap. Each chunk will contain a portion of the text with some overlap based on the specified size and overlap to ensure context is preserved."

chunks = splitter.create_documents([text])

# print(chunks)

from langchain_community.document_loaders import TextLoader

loader = TextLoader("chunking\data.txt", encoding="utf-8")
document = loader.load()

print(document)

ch = splitter.split_documents(document)
print(ch)