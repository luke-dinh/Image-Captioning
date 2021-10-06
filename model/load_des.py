import os 

main_path = "...."
image_dir = os.listdir(main_path)

image_path = main_path + ""
cap_path = main_path + ""
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
