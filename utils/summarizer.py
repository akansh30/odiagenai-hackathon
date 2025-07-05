from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


tokenizer = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
model = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def summarize_text(text, max_length=200, min_length=30):
    """
    Summarizes the given text using a pre-trained model.
    
    Args:
        text (str): Input text to summarize
        max_length (int): Max summary length
        min_length (int): Min summary length
    
    Returns:
        str: Summarized text
    """
    
    if len(text) > 3000:
        text = text[:3000]
    
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    sample_text = sample_text = "Odia literature is one of the oldest and richest literary traditions in India, with a history that dates back over a thousand years. It evolved through distinct phases, beginning with the Charyapadas, followed by classical poetry, medieval narratives, and colonial-era prose. The influence of Vaishnavism and the Bhakti movement shaped much of medieval Odia literature, especially through the works of the saint-poet Jagannath Das and his Odia Bhagabata. During British rule, prose writing flourished, with Fakir Mohan Senapati being hailed as the father of modern Odia fiction. His short stories and novels addressed social reform and depicted realistic rural life. Post-independence, Odia writers experimented with modernism and postmodernism, exploring themes of identity, migration, and globalization. The language has also seen contributions in the fields of drama, essays, and children's literature. Recognized as a classical language by the Government of India, Odia literature continues to grow and influence generations of readers and writers."
    print(summarize_text(sample_text))
