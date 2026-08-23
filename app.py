from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vector_store import FaissVectorStore
from src.generationalmodel import ChatGroqModel




if __name__=="__main__":

    documents=load_all_documents("./data/txtfile")
    chunks=EmbeddingPipeline().chunk_documents(documents)

    # print(chunks)
    
    chunkvectors=EmbeddingPipeline().embed_chunks(chunks)

   
    store=FaissVectorStore(persist_dir="travelsuggestionvector")
    store.load()
    retriever=store.query("I am planning a 5 day motorcycle trip from tokyo covering mountains, beaches and villages. Can you suggest a route and places to visit?")
    print(retriever)

    generationalresponse=ChatGroqModel.rag_simple("I am planning a 5 day motorcycle trip from tokyo covering mountains, beaches and villages. Can you suggest a route and places to visit?",retriever)
    print(generationalresponse)


 
    # answer=rag_simple("I am planning a 5 day motorcycle trip from tokyo covering mountains, beaches and villages. Can you suggest a route and places to visit?",EmbeddingPipeline,llm)
    # # print(answer)


  

    


    

  
   

  

   
     

 



    