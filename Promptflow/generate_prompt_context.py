from typing import List
from promptflow import tool
from promptflow_vectordb.core.contracts import SearchResultEntity

@tool
def generate_prompt_context(search_result: List[dict]) -> str:
    def format_doc(doc: dict):
        # Extracting additional metadata based on the index configuration
        item_name = doc.get('item_name', 'Unknown Document Name')
        content_type = doc.get('content_type', 'Unknown Content Type')
        last_modified = doc.get('item_last_modified', 'Unknown Last Modified')
        folder_path = doc.get('folder_path', 'Unknown Folder Path')
        web_uri = doc.get('item_weburi', 'No URI Provided')
        return f"Document: {item_name}\nContent Type: {content_type}\nLast Modified: {last_modified}\nFolder: {folder_path}\nURI: {web_uri}\nContent: {doc['Content']}"

    retrieved_docs = []
    for item in search_result:
        entity = SearchResultEntity.from_dict(item)
        content = entity.text or ""
        if isinstance(entity.metadata, dict):
            doc_data = {
                "Content": content,
                "item_name": entity.metadata.get('item_name'),
                "content_type": entity.metadata.get('content_type'),
                "item_last_modified": entity.metadata.get('item_last_modified'),
                "folder_path": entity.metadata.get('folder_path'),
                "item_weburi": entity.metadata.get('item_weburi')
            }
            retrieved_docs.append(doc_data)
        else:
            print(f"Unexpected metadata type: {type(entity.metadata)}")
    doc_string = "\n\n".join([format_doc(doc) for doc in retrieved_docs])
    return doc_string
