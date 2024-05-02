from transformers import BertTokenizer, BertForSequenceClassification
import torch
from torch.nn.functional import softmax

class BERTModel:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

    def evaluate_answer(self, question, user_answer, correct_answer):
        encoded = self.tokenizer.encode_plus(question + " " + user_answer,
                                             question + " " + correct_answer,
                                             return_tensors='pt')
        output = self.model(**encoded)
        probabilities = softmax(output.logits, dim=-1)
        is_correct = probabilities[:, 1] >= 0.5  # Assuming class 1 is 'correct'
        return is_correct.item(), probabilities[:, 1].item()
