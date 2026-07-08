from src.data_loader import load_all_documents
from src.vector_store import FaissVectorStore

if __name__=="__main__":
    data_dir="data"
    documents=load_all_documents(data_dir)
    store=FaissVectorStore("faiss_store")
    store.build_from_documents(documents)
    # store.load()
    print(store.query("What is predefined Clean Action?",k=3))

     

 



    