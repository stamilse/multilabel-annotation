import spacy
from spacy import displacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

text = ("She saw a secret little clearing, and a secret little hot made of rustic poles. And she had never been here before! She realized it was the quiet place where the growing pheasants were reared; the keeper in his shirt‑sleeves was kneeling, hammering. The dog trotted forward with a short, sharp bark, and the keeper lifted his face suddenly and saw her. He had a startled look in his eyes.")

doc = nlp(text)

#numbered sentences
for num,sentence in enumerate(doc.sents):
    print(f'{num}: {sentence}')

#parts of speech
for word in doc:
    print(word.text, word.pos_)

#parts of speech detailed
for word in doc:
    print(word.text, word.pos_, word.tag_)

#spacy.explain('VBP')

#syntactic dependancy
for word in doc:
    print(word.text, word.pos_, word.tag_, word, word.dep_)

#dependancy visualisation
displacy.render(doc,style='dep')

