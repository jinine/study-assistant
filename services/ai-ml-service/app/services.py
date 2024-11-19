from transformers import pipeline

def summarize_text(text: str) -> str:
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def extract_entities(text: str) -> list:
    ner = pipeline("ner")
    entities = ner(text)
    return entities

def classify_text(text: str, candidate_labels: list) -> dict:
    classifier = pipeline("zero-shot-classification")
    result = classifier(text, candidate_labels)
    return result

def answer_question(context: str, question: str) -> str:
    qa = pipeline("question-answering")
    result = qa(question=question, context=context)
    return result['answer']

def generate_text(prompt: str) -> str:
    generator = pipeline("text-generation")
    result = generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text']

def predict_masked_word(text: str) -> list:
    unmasker = pipeline("fill-mask")
    result = unmasker(text)
    return result

def paraphrase_text(text: str) -> str:
    paraphraser = pipeline("text2text-generation", model="t5-small")
    result = paraphraser(f"paraphrase: {text}", max_length=150)
    return result[0]['generated_text']

def summarize_and_classify(text: str, candidate_labels: list) -> dict:
    summarizer = pipeline("summarization")
    classifier = pipeline("zero-shot-classification")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    classification = classifier(summary, candidate_labels)
    return {"summary": summary, "category": classification['labels'][0]}
