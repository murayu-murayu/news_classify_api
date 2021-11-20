from rest_framework import serializers
import torch
from transformers import BertForSequenceClassification, BertJapaneseTokenizer



class BertPredictSerializer(serializers.Serializer):
    news_path = "./model/"

    sc_model = BertForSequenceClassification.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking", num_labels=9)
    tokenizer = BertJapaneseTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")

    loaded_model = BertForSequenceClassification.from_pretrained(news_path) 
    loaded_tokenizer = BertJapaneseTokenizer.from_pretrained(news_path)

    input_text = serializers.CharField()

    genre = serializers.SerializerMethodField()


    def get_genre(self, obj):
        news_path = "/Users/yu/Dropbox/development/app/042_bert_colab/drf_2/model/"

        loaded_tokenizer = BertJapaneseTokenizer.from_pretrained(news_path)
        loaded_model = BertForSequenceClassification.from_pretrained(news_path)

        input_text = obj['input_text']
        input_text = input_text.translate(str.maketrans({"\n":"", "\t":"", "\r":"", "\u3000":""})) 

        max_length = 512
        words = loaded_tokenizer.tokenize(input_text)
        word_ids = loaded_tokenizer.convert_tokens_to_ids(words)
        word_tensor = torch.tensor([word_ids[:max_length]])
        
        x = word_tensor
        y = loaded_model(x)
        
        # 最大値のインデックス
        pred_num = y[0].argmax(-1)  
        
        category=['it_mobile',
        'movie',
        'others_for_men',
        'others_for_wemen',
        'home_appliance',
        'sports',
        'fashion',
        'it_life-hack',
        'topic_news']
        
        pred_genre = category[pred_num]
        pred = (pred_num[0], pred_genre)

        return pred
