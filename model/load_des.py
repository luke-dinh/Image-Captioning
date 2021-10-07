import os
import string

main_path = "...."
# image_dir = os.listdir(main_path)

image_path = main_path + ""
cap_path = 'captions.txt'
train_path = main_path + ""
val_path = main_path + ""
test_path = main_path + ""

class prep_cap():

    def load_doc(filename):
        filename = open(cap_path, 'r')
        text = filename.read()
        filename.close

        return text

    def load_cap(doc):
        mapping = dict()

        for line in doc.split('\n'):
            token = line.split()
            if len(line)<2:
                continue
            
            image_id, image_desc = token[0], token[1:]
            image_id = image_id.split(".")[0]
            image_desc = ' '.join(image_desc)

            if image_id not in mapping:
                mapping[image_id] = list()
            mapping[image_id].append(image_desc)

        return mapping    

    def clean_des(descriptions):

        table = str.maketrans('','',string.punctuation)  
        
        for key, desc_list in descriptions.items():
            for i in range(len(desc_list)):
                desc = desc_list[i]
                desc = desc.split()
                desc = [word.lower() for word in desc]
                desc = [w.translate(table) for w in desc]
                desc = [word for word in desc if len(word)>1]
                desc_list[i] = ' '.join(desc)

    def to_vocab(desc:dict):
        words = set()

        for key in desc.keys():
            for line in desc[key]:
                words.update(line.split())
        return words

# # Test 
# doc = prep_cap.load_doc(cap_path)
# # print(doc[:3000])
# descriptions = prep_cap.load_cap(doc)
# # print(descriptions)
# new_des = prep_cap.clean_descriptions(descriptions)
# # print(new_des)
# vocab = prep_cap.to_vocab(descriptions)
# print(vocab)