from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization")

def summarize_text(text: str) -> str:
    # Generate summary
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
