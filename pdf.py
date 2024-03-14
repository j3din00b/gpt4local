from g4l.local import DocumentRetriever

pdf            = DocumentRetriever(
    files=['einstein-albert.txt'], 
    embed_model='sentence-transformers/paraphrase-MiniLM-L6-v2', #https://huggingface.co/spaces/mteb/leaderboard
    verbose=True
)
retrieval_data = pdf.retrieve('what invenstions did he do')

for node_with_score in retrieval_data:
    node = node_with_score.node
    score = node_with_score.score

    # Access the text content
    text = node.text

    # Access the metadata
    metadata = node.metadata
    page_label = metadata['page_label']
    file_name = metadata['file_name']
    # ... access other metadata fields as needed

    # Print or process the extracted information
    print(f"Text: {text}")
    print(f"Score: {score}")
    print(f"Page Label: {page_label}")
    print(f"File Name: {file_name}")
    print("---")