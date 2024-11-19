from flask import Flask, jsonify, request

app = Flask(__name__)

def register_routes(app: Flask):
    
    @app.route('/api/summarize', methods=['POST'])
    def summarize():
        data = request.get_json()
        text = data.get('text')
        if text:
            summary = summarize_text(text)
            return jsonify({"summary": summary}), 200
        return jsonify({"error": "No text provided"}), 400


    @app.route('/api/entities', methods=['POST'])
    def entities():
        data = request.get_json()
        text = data.get('text')
        if text:
            entities = extract_entities(text)
            return jsonify({"entities": entities}), 200
        return jsonify({"error": "No text provided"}), 400


    @app.route('/api/classify', methods=['POST'])
    def classify():
        data = request.get_json()
        text = data.get('text')
        candidate_labels = data.get('candidate_labels')
        if text and candidate_labels:
            classification = classify_text(text, candidate_labels)
            return jsonify({"classification": classification}), 200
        return jsonify({"error": "Text or candidate_labels missing"}), 400


    @app.route('/api/qa', methods=['POST'])
    def qa():
        data = request.get_json()
        context = data.get('context')
        question = data.get('question')
        if context and question:
            answer = answer_question(context, question)
            return jsonify({"answer": answer}), 200
        return jsonify({"error": "Context or question missing"}), 400


    @app.route('/api/generate', methods=['POST'])
    def generate():
        data = request.get_json()
        prompt = data.get('prompt')
        if prompt:
            generated_text = generate_text(prompt)
            return jsonify({"generated_text": generated_text}), 200
        return jsonify({"error": "No prompt provided"}), 400


    @app.route('/api/fill-mask', methods=['POST'])
    def fill_mask():
        data = request.get_json()
        text = data.get('text')
        if text:
            result = predict_masked_word(text)
            return jsonify({"result": result}), 200
        return jsonify({"error": "No text provided"}), 400


    @app.route('/api/paraphrase', methods=['POST'])
    def paraphrase():
        data = request.get_json()
        text = data.get('text')
        if text:
            paraphrased_text = paraphrase_text(text)
            return jsonify({"paraphrased_text": paraphrased_text}), 200
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
