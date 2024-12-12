from flask import Flask, jsonify, request
from app.services import summarize_text, extract_entities, classify_text, answer_question, generate_text, predict_masked_word, paraphrase_text, summarize_and_classify

app = Flask(__name__)
model_name = "bert-base-uncased" 

def register_routes(app: Flask):
    
    @app.route('/api/summarize', methods=['POST'])
    def summarize():
        data = request.get_json()
        text = data.get('text')
        if text:
            summary = summarize_text(text)
            return jsonify({"text": summary}), 200
        return jsonify({"error": "No text provided"}), 400


    @app.route('/api/entities', methods=['POST'])
    def entities():
        data = request.get_json()
        text = data.get('text')
        if text:
            entities = extract_entities(text)
            return jsonify({"text": entities}), 200
        return jsonify({"error": "No text provided"}), 400


    @app.route('/api/classify', methods=['POST'])
    def classify():
        data = request.get_json()
        text = data.get('text')
        candidate_labels = data.get('candidate_labels')
        if text and candidate_labels:
            classification = classify_text(text, candidate_labels)
            return jsonify({"text": classification}), 200
        return jsonify({"error": "Text or candidate_labels missing"}), 400


    @app.route('/api/qa', methods=['POST'])
    def qa():
        data = request.get_json()
        context = data.get('context')
        question = data.get('question')
        if context and question:
            answer = answer_question(context, question)
            return jsonify({"text": answer}), 200
        return jsonify({"error": "Context or question missing"}), 400


    @app.route('/api/generate', methods=['POST'])
    def generate():
        data = request.get_json()
        prompt = data.get('prompt')
        if prompt:
            generated_text = generate_text(prompt)
            return jsonify({"text": generated_text}), 200
        return jsonify({"error": "No prompt provided"}), 400


    @app.route('/api/fill-mask', methods=['POST'])
    def fill_mask():
        data = request.get_json()
        text = data.get('text')
        if text:
            result = predict_masked_word(text)
            return jsonify({"text": result}), 200
        return jsonify({"error": "No text provided"}), 400


    @app.route('/api/paraphrase', methods=['POST'])
    def paraphrase():
        data = request.get_json()
        text = data.get('text')
        if text:
            paraphrased_text = paraphrase_text(text)
            return jsonify({"text": paraphrased_text}), 200
        return jsonify({"error": "No text provided"}), 400


    @app.route('/api/summarize_and_classify', methods=['POST'])
    def summarize_and_classify_route():
        data = request.get_json()
        text = data.get('text')
        candidate_labels = data.get('candidate_labels')
        if text and candidate_labels:
            result = summarize_and_classify(text, candidate_labels)
            return jsonify(result), 200
        return jsonify({"error": "Text or candidate_labels missing"}), 400


    if __name__ == '__main__':
        app.run(debug=True)
