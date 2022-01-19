# -*- coding: utf-8 -*-
"""Fine tune BERT for text classification with tensor flow

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11DlAZ8mF20E4aCza6hTY9YPiDGKhfJlP

![image.png](data:image/png;base64,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0YHnVJcuXYp8DwtXXHHFggULFD0jthWe0X7wIeKhW5YuXWowGPhHvV6/dOlSFcsD3fLggw/KP44fPz4w9COK9oMPF01Ctygq8qjChxeTyfTb3/6Wf4zwKjxpMuIVZ5ZRi4fuWrp06fDhw4lo+PDhqMKHnQcffJD93o1GIyJeg8G3devW9evX84+Btfjdu3cvX75chZJBmIiOjs7MzCSizMxMVOHDzkUXXcQ3n9plGQAkmaA9w9GECRMuueSSp556SpKkP/7xj0Q0f/58SZJeeOGFGTNmENE777yjdhnhOy+88MLKlStnz549evRo1X4G4WD06NGzZ89euXLlCy+8oPZGG+gaGxtjY2NPnDihdkHUp82ILywsZAuSmJh4xx13EJHZbL7hhhtYTxb3oLqWlpb58+f3f1ZqwPz581taWtTegANaXl6e2kUYEM65Lr7TG6XCyOjRoz/77LOgX9XV1U2YMKGfywMKpaWlixYt+uijj9QuSLgaN27cH/7wh5tuuqk/Z3r8+PGampqampqTJ0/253x74PTp0+xhZAPNkCFDJk+enJycPHLkyN5PrfObmeR5n3OWOv9uQmrjxo3yxeSnWxcsWKB20UBqaWkZN24c3zqLFi3auXPn0aNH1S7XgPbRRx8999xzixYt4uvtkksu6be6fHFx8fjx43sfScCNHz++uLi4l9uFT63dAXo5g4Es6B75/vvvq10ukHj7zODBg3fu3Kl2ccLMzp07ef20H1odm5ub77nnnn6IvMh0zz33NDc393jr8Om0N4CWH0O2YcMGxSVTixYt+sMf/qBWeYB58cUX//d//5d179y585ZbblG3POFo165dP/vZz1j3Cy+8MHv27L6b17Rp0/7973+zbqPRmJycLIpiVFRU381R27766ivW2NXY2Mj63HDDDRUVFT2bWuet6z3+7xEWLr74YvnCfvDBB2qXCKSVK1eyzbFo0SK1yxLGeIvNypUr+24uq1ev5j+f3/zmN6dOneq7eUWUU6dO/eY3v+HrdvXq1T2bTqdJ3lenIw4cOFBTU/Phhx/20fS76PLLL//kk09Y99VXX71t2zZ1y9OesWPHJicnJyUlqV2Q/lBTU8M62AWs0DMzZsxgJ5z4+gy5/fv3Z2dns+4nnnhCftdo7xUWFq5YsYKIli9ffs8998TFxVmt1j179vj9fj6MxWK56667brrppqKiIqvVKh/3kUceOXz4MJuIfBRBEBobG41Go9/vN5lMM2fOXLVqVVxcnGLuPp/v6quv3rBhw6xZs3w+36WXXiqfCJ/UX/7yl9mzZwuCIP+2tra29z/VwYMHb9iwISEhYcmSJUSUnZ194403pqSk9HKyQfT0n1C7Nm/ejLtFeiY6Onrz5s0h3yIDDb/+/aOPPlK7LGGMX4w0evToPpoFr8LfdNNNoZ2y0+mU7/kWi0WSJLPZrPhFWCwWNqQgCLW1tYrRKysrFdNhQ1ZWVir6yMdlLBYLETkcDkmSvF6vIAiBv0dBEEpKSgL7B06tN/g1UT2ryPNStTdAiO9u/eUvf3nfffe1tbWFdrIRoq2t7b777vvlL3+pdkH61qeffso6xo4dq25Jwhpfe3x9hlx1dTXruPPOO0M42aqqqqysLJbFDQ0NZrPZZDLxb+XxVFxcfM011xCR3++/9dZbfT5f0AlWVlbyUXgDt9PpbGhocDqdbFz58MXFxSy72QImJCQ0NjbyxHQ6nXxSF110kbwPE9qjbb5u+doOrVA21KxYseLZZ59l3VdccYUoirjKqou8Xm9NTc3BgweJ6Nlnn12xYsXatWvVLlR4iPDj/T7Fm4AmT54cwsmySx4qKirY4u/evVv+rfxZI6WlpeypnyaTyev1pqen7969O3ArpKWl8W6Hw/HTn/6UdcfFxWVmZjY3N69Zs6aqqio1NZWIfD6f3W4XRTEuLq68vLwrBc7KysrKymLdoiju37+/m0vcEb5u+6jBLWQRv3fv3nXr1rFuh8MhP0sDXZSdnb1mzRoiWrdu3Y033jh9+nS1SzTQ5efn899eVlZWTU1NcXFxU1NTYM6+8847RGS32ydOnMiDtbm52ev1VlVVNTc3B45SVVXFenq9XpfLVVxczFOJW7RokdfrffXVV2fNmtXc3NxeOb/88ksiCpzFAMfPpV166aWhmqbP5yspKbHZbEePHl27dq3b7fZ6vUTkcDg6GGvDhg05OTlut5ulfNdn5/F49uzZQ0T8vbsPP/yw3+9/4oknXnvttfLycvZ6Xvkoe/fu7c+H2/B127Mzl52+9Slktz7df//9bIJWq7UHo3dRQ0NDe61mXq9XkiSv18ta2YjIZDKxgzVJkgoKCgRBYBOpra0VBKG0tLS2tpaNK59UbW2tKIqiKLIROUEQioqK+m7RGF7HvP/++/t6XmoJuu/1AGtylR/vs6ZV1qQbdGC2V/Atq2jSlR/v81H48T4bVz5AUVERm6bZbA5cRvnRPZ9ULxc5cC4hWZP9OX2+KhS/u9LSUrPZHLgm2fBsE7NXs4qiyP4f8A0XdBQ5tmNIsk3GFRQUKBZZXgY+9xCugUB9uh1D9oyaqVOnsnH37dsXorIF0cGJEa/Xy7Jb8ZXNZpPO/pils/nOhg/cFYiI5T4fkQv6Sw65ffv2sblPnTq1r+elllDt0Ox/eeC5r8CzdqWlpWxbszZf/v+7g7N2DodDkcs8VthHVtsQRTHofxQKFvFyoij2cvGlcI54/uMqLS0VBIH97+w44iVJ4inPdDHi2blcJnDfUPzM2QYNOve+06fbMWSnW/uo2U6hgxMjCQkJt956q9/v5zV3r9criqLL5eJnaTwez7Rp04iooqIiISGB9Qw8l8L2A5fLxR9n1m/6umFOM+TH+1arNTExUafT6XQ6fpFfUBs2bBBFkR3vt3fuLqgOjvdZe5rH41GMsnfv3u4tUmRITU0VBMHlcrHtxa4n+cc//sG+LS8v18mUlZWxE1RMXFzc7t275SnPyEfhO4DT6WRHBiUlJSkpKR6Px+PxlJeXyxPcZDIVFxfL94TAhn4iSktL49Pvk+sa+1So/pn0ZtyeoXPTubS0lALyWlFNY/V3Xu9rr24lP8XPG2eoX2rxkoae99mekCwgjvel8KzFS5LE2kLZlC0Wi/z3KI9v1gTHftesGZZpaGiwWCyCIDQ0NMgbZvmGYAdYfItUVlaaTCaHw8EmJd8K7BhCPnGLxcK3MmOz2eT7mPyYIFT6dDuGd8TLf0XsV6poQGc9vV4vPxKXb+AOIt5sNvOfMUt5QsSHSEgWEMf7UthGPCj06XrW4FufOJ/Pt3nzZpPJxNtkiGjJkiWKI3T5D09+OZTVamUpP3fu3OLi4n4rNnQFjvcBuiKMI17xE42JiSGiRYsW1dfXE1F9fX16errX673vvvv4MEVFRd1qh5WnfCiLDqFQUVEhP97nVzQ+9NBDiuN9g8HAnlbE7mShsynPjvcnTpw4Z84cxfH+2LFjJ06cKAhCTEzMrFmzdu/eXVlZ6ff7//73vx89epTNhQ+8YcMGIpJfNBkbG5ucnMw/pqamKo735Tf7APShUB0v9GbcnlEcjyuOvhl+3QI/EmeRbTKZ+FUWgcMLgiCfcgfXxvWF/l+T/UzzC9hv+npNYkv1jz5dz2Fci1dUlFi9zOl0svqRIAhOp5PfJRETE8PqUFarlZ11+fOf/9xe3UrRtsNGEQQB9yIBwICSe1Z7A5zzvPjO3xHVPi29FFBdml+Tml/AftPXaxJbqn/0Zj13Ou45tfhO/yEAAHSLx+MxGrVi4AAAACAASURBVI3yU9l2u72srEyn0ymuYigsLExMTCSi9PR0flK6qqqKiHw+n9FoZN1cYmJiYWEhH1ihrKxMPnBVVVXQwVJSUoxGo/x2ivr6ep1OxwrDhrFarewMn8fj0el0isUJvCViQAnjhhoACAuKh/MIgsAfGSTPR/7IIP50MLfbnZaWVlVVVVdX5/f7X3vtNfl0vF5vc3NzFy+daGlpae+rKVOmsOeUsY+PPvooEcXExLCH5xBRSUmJKIo+n6+1tTVwcQY4RDwA9KGkpCTp7J0B7Hak1atXd/qIYHZpAzttxpNd/vRpPtb+/fvZeUXF9RezZs2ST3DWrFmsv+Iehf3792/atEkQBPZqjvr6epfLZbPZ4uPj6dwnEtfV1bFJ9emzhUMOEQ8A/eSKK66Qf+SPCG6vJs5f2caw2GV44PZeQkICe+Zlfn4+q8Lffvvt8gEUz4DMysoKo/sbEPEAoI6gjwxitxewm9cWLlwoCMKcOXMCxz1y5AgRsaMBrovPfyfZkQGzYMECs9mclZXlcrnMZnNqaipr2MnKyhoxYoTL5RJFkT1uPuxoKuKLi4sV51KKi4vZaRa73a44V8Pl5+ez8yfs3sV+LjNAxDIYDOw2Y5byLNz5Cwvp7B1t/ApmeS6/8sorRDRx4sRQFYY119DZm9rY2QIiEgTBZrPJH1Lf3v3wA5OmIj7wnQwGg4HtFi6XKy0tLTExUXGe3W63Z2VlsfMnbrf773//e7+VFgD4wyTcbjd7Hw7DYrS4uJi1dLPnVWzevJld2VJcXOxyuSwWi/xBEfK7ZDrQwX8Fv9/PqvC8jyRJjY2NmzZtCvpEirCgqYhfsGCBdPZGVvb4On7KpaioqKCggIhuuukmu93OelZVVblcLofDwR9ehpdVDUB2u11xcFZfX5+SkpKSkqJowzUajcXFxWVlZeywjF0Mx4ZJT0/Pz89XTNZqtXZwLV17heFf1dfXG41GxWSZwsLCwCkEHi8WFhYajUb2Lbu4UFEF0QB2oSF79x57Sk92dnZXHhmksHz5cq/XazKZdDrd3LlzBUGQ/0ugs48w6VR7Yc0eOyp/LkV7BtSzhvh7nNodQn5quDdvfQo6QVUonhqoeKEP+8jO7CseYCCKYmjfrd4zA2dN9pHuLqDi6THs6a+sO+hrWxTv92BXWVDA8yfYBRjsmo1AQV/Z0dDQwL5l+wmrNAQOyd8qI3/uqc1mk0+fPbE26JtqurhapDB5gAFfG/Jl7+ARwdXV1fInfss5HA7WlmI2mwMHKCgo6OKLVthL3xQ92QOH+Ud2Q3vguH3xbOE+3Y5h/Iya9nQc8ZIkiaLI39DGH3jA40PxOOL+N3DWZB/p2QKazWb5T44/zlf+oHaSRXxlZSV/mDj7qvfP++X/D9jzpfn/HsVgfI/iU2MTlx8vMvyIU/Emgy4Ki4iHTvXpetZUQ03X8WpgZmbm4cOH2bpQXP0KA82UKVPkH1mSLly4sINHPfMNTUTjxo2Tf+V2u7tbAH4K7u233yYi9h4oOveVT/n5+V6vlx31Ky7bWLNmzYgRIwJP7PM3kQ3wK6whHEVKxLNLoHw+X35+vtvttlgsrCGV37hcVlb27LPPqlpG6J7ExMSgD/RnZ93T0tJMJpPb7WZpq8DO2gU+V04RygrPPvusyWQSRbG6urqsrIydnSPZNdr19fVZWVlms5md1OFvZ0xNTZUfL7rd7mnTpvETCX6///nnn0e+Q58I1fFCb8YNFdY2KldaWhr45mV2RMzbVeX653HBHRsIa7JP9WwBFfcu8o/yl3OxLcjbcEwmE78RUbFx2cDyBlnFy7gDsR3GZrOx/xmsbZ01NLMmoMDHWQdtzJWCvRacvzG8W/p6V9H8rjhA9Ol61n4t3mw28zMkgiDwd0fExcWVlpby36QoigUFBfKrXyEsBH1tC0vzw4cPZ2Zmsj4Wi6W8vJzdG+HxeOx2uyAI8nvcO73C+qWXXiKi2bNnX3vttUTELtpLSkoSRZG12NTV1Skaf/x+f319fafHi919Uw1AN4Tqn0lvxgU5za/J7i5g0CtqOnhtSwfvbpULvKaCOqzF8/cA80VgJ13ZsWNtbS0rJz/FyorEHnIS+LtjJQz6ppourhYpImvxgS9GLyoq4i/ybe9sOX+N+wC5ak6hT9ez9mvxoEkdvLYlOTk5NjZWMXxqampRURF/5UtpaaniMVVEJAjClVde2d4cY2JiRFFkM3U4HKIoWq1WIrrxxhtZfHi9XvmNM1arVRTF5ubmDo4Xg76ppjerRfNwe2O3heqfSW/GBTnNr0nNL2C/6es1OWC3lPz2Rv6R3d7I/ovzC2Tbu1x1QOnNeu70ZqbB8rjv6BYpAICBRHENUnx8vNVqXbBgQX5+flZWVlJS0oIFC9hXa9asYbfCiqK4ZcsWLV28lJeXxzrae5UT3voEAJqSmZkpiuIjjzxCnV2uGglC1hbP7yt5//33QzXNCMTXnuI+HQDoFtzeyIQs4vlj3p544olQTTMC8bXXxcfmAQCD2xuD6+EJggD8GY2CILz55puhmmxEefPNN/kTjlavXq12cfpKyPe9iNXXa3IAbilt3N6o0Jv13Om4IavFOxyOq666is4+c9lut6PFpuvef/99u91uNpvZpV1XXXVV0NvutWH06NGs4+OPP1a3JGGNrz2+PkMuKiqKdbS1tfXRLEIirG9v5OuWr+0Q68X/HqWKioo+KWLkqaioCOF2GWhmz57NFvO5555Tuyxh7LnnnmOrcfbs2X00i6lTp7JZ7Nu3r49mAfv27WMreerUqT0YnYdGewOE8tanG264oaKigtXloWeuuuqqioqKG264Qe2C9KHJkyezjpdfflndkoQ1vvb4+gw5fkLoySef7KNZAF+3fXT6bXDng3THDTfcUFNTs2bNmpqamurqasWby6E948aNS05Onjx5sobbZzj+opyNGzfeeOONt9xyi7rlCUe7du3auHEj6+67Fw/xfx67du06dOjQhAkT+mhGEevQoUO7du1i3T37V935zUzyKn1v3vo0MAUuIwwE8+fPZ5tm8ODBO3fuVLs4YWbnzp2DB39XOZs/f36fzuu6665jMxoxYkRdXV2fzivS1NXVjRgxgq3e6667ro/mopNkrTk6nY5nYg/+nwxAbIk0szia0dra+qMf/eijjz5iHxctWjRjxozk5OSxY8eqW7CB7OOPP66urn755Zd5/X3cuHEHDhzQ6/V9N9Pq6mp+uvK888675ZZbHnjggcmTJ0dHR/fdTLWtra2tpqbmySef3LVr17fffst6ut3uvrpOWp73QXuGNY0tjpa8+OKLuL2rNy655JIXX3yxH7bUY489pvayatxjjz3Wd5sPEQ+qaWlp4S020C3z589vaWnpty3ldrt5iw2E0HXXXed2u/t026GhBlT24osv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)
"""

!nvidia-smi

import tensorflow as tf
print(tf.version.VERSION)

!git clone --depth 1 -b v2.3.0 https://github.com/tensorflow/models.git

# install requirements to use tensorflow/models repository
!pip install -Uqr models/official/requirements.txt
# here you may have to restart the runtime afterwards
#https://github.com/tensorflow/models/blob/master/official/requirements.txt

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import sys
sys.path.append('models')
from official.nlp.data import classifier_data_lib
from official.nlp.bert import tokenization
from official.nlp import optimization

print("TF Version: ", tf.__version__)
print("Eager mode: ", tf.executing_eagerly())
print("Hub version: ", hub.__version__)
print("GPU is", "available" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE")

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Transformers/Fine-tuning using transformers /train.csv' #dataframe
                )
df.shape
df.info()

"""qid - unique question identifier
question_text - Quora question text
target - a question labeled "insincere" has a value of 1, otherwise 0
https://www.kaggle.com/c/quora-insincere-questions-classification/data
"""

df.tail(20)

df.target.plot(kind='hist',title='Target distribution'); #need a sample distribution

##Create tf.data.Datasets for training and evaluation

train_df,remaining=train_test_split(df,random_state=42,train_size=0.0075,stratify=df.target.values)
valid_df, _= train_test_split(remaining,random_state=42,train_size=0.00075,stratify=remaining.target.values)
train_df.shape,valid_df.shape

with tf.device('/cpu:0'):
    train_data=tf.data.Dataset.from_tensor_slices((train_df['question_text'].values,train_df['target'].values)) ##tensor for training data
    valid_data=tf.data.Dataset.from_tensor_slices((valid_df['question_text'].values,valid_df['target'].values))

    #first entry:
    for text, label in train_data.take(1):
        print(text)
        print(label)

"""Usage model here https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/2"""

##Download a pre-trained BERT model from TensorFlow Hub

"""
Each linea of dataset is composed by text and its label
Data preprocessing consists of transforming text to BERT input feautures: input_word_id,input_mask, segment_ids
In this process, tokening the text is done with provided BERT model tokenizer
""" 
#Para diseñar el head o cabeza extra para el modelo de BERT es necesario conocer el número de unidades en el head
label_list=[0,1] #labels 
max_seq_length=128 #maximum lenght of token input sequences
train_batch_size=32

bert_layer = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/2",
                            trainable=True)
vocab_file=bert_layer.resolved_object.vocab_file.asset_path.numpy() #donde se almacena el vocabulario
do_lower_case=bert_layer.resolved_object.do_lower_case.numpy() #crea el objeto y se indica el modelo uncased de BERT 
tokenizer=tokenization.FullTokenizer(vocab_file,do_lower_case)

tokenizer.convert_tokens_to_ids(tokenizer.wordpiece_tokenizer.tokenize("Hi BERT, how are u today?"))

tokenizer.wordpiece_tokenizer.tokenize("Hi BERT, how are u today?")
#Los tensores deben de tener la misma longitud, pregunta: max_len a nivel de data o de batch?

##Tokenize and Preprocess text for BERT
#input mask pone atención a los tokens_ids diferentes del padding, en estos se obtiene un valor de cero. Sirve para diferenciar las palabras de una sentencia u oración 



def to_feature(text, label, label_list=label_list, max_seq_length=max_seq_length, tokenizer=tokenizer):
  example = classifier_data_lib.InputExample(guid = None,
                                            text_a = text.numpy(),  #texto que queremos clasificar, numpy para conseguir el valor del tensor
                                            text_b = None,  #la siguiente sentencia para predecir
                                            label = label.numpy())  #valores de las etiquetas
  feature = classifier_data_lib.convert_single_example(0, example, label_list,
                                    max_seq_length, tokenizer)
  
  return (feature.input_ids, feature.input_mask, feature.segment_ids, feature.label_id)

#Use dataset.map to apply the function to each element of the dataset 
#to wrap it in a tf.py.function 
##Wrap a Python Function into a tf op for eager execution:

def to_feature_map(text, label): #nos permite ejecutar una función dentro de otra función 
  input_ids, input_mask, segment_ids, label_id = tf.py_function(to_feature, inp=[text, label], 
                                Tout=[tf.int32, tf.int32, tf.int32, tf.int32]) #tensores de salida 

  # py_func doesn't set the shape of the returned tensors. 
  input_ids.set_shape([max_seq_length])
  input_mask.set_shape([max_seq_length])
  segment_ids.set_shape([max_seq_length])
  label_id.set_shape([])

  x = {
        'input_word_ids': input_ids,
        'input_mask': input_mask,
        'input_type_ids': segment_ids
    }
  return (x, label_id)

###Create a TensorFlow Input Pipeline with tf.data
with tf.device('/cpu:0'):
  # train
  train_data = (train_data.map(to_feature_map,
                              num_parallel_calls=tf.data.experimental.AUTOTUNE) #la GPU puede usar múltiples recursos para transformar elementos de datos en paralelo, mejorando así la eficiencia computacional
                          #.cache() #permitiendo la paralelización de los datos 
                          .shuffle(1000)
                          .batch(32, drop_remainder=True) #batch size, 
                          .prefetch(tf.data.experimental.AUTOTUNE)) #nos permite habilitar la carga previa de los datos por parte de la CPU antes de que comience en el entrenamiento

  # valid
  valid_data = (valid_data.map(to_feature_map,
                            num_parallel_calls=tf.data.experimental.AUTOTUNE)
                          .batch(32, drop_remainder=True)
                          .prefetch(tf.data.experimental.AUTOTUNE))

#train data looks like
train_data.element_spec

#valid data looks like
valid_data.element_spec

## Fine tuning: Add a Classification Head to the BERT Layer 768 embedding dimension 
#pooled output shape [batch size,768]
#sequence output shape [batch size, max_seq_length,768]

def create_model():

    input_word_ids=tf.keras.layers.Input(shape=(max_seq_length),dtype=tf.int32,
                                         name="input_word_ids")
    input_mask=tf.keras.layers.Input(shape=(max_seq_length),dtype=tf.int32,
                                     name="input_mask")
    input_type_ids=tf.keras.layers.Input(shape=(max_seq_length),dtype=tf.int32,
                                      name="input_type_ids")
    
    pooled_output,sequence_output=bert_layer([input_word_ids,input_mask,input_type_ids])
    drop=tf.keras.layers.Dropout(0.4)(pooled_output)
    output=tf.keras.layers.Dense(1,activation='sigmoid',name="output")(drop)

    model=tf.keras.Model(
        inputs={
            'input_word_ids': input_word_ids,
            'input_mask': input_mask,
            'input_type_ids': input_type_ids
        },
        outputs= output)
    

    return model

#Fine Tune BERT 
model=create_model()
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=2e-5),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy()])
model.summary()

tf.keras.utils.plot_model(model=model, show_shapes=True,dpi=76)

#Train model
epochs=4
history= model.fit(train_data,
                    validation_data=valid_data,
                    epochs=epochs,
                    verbose=1)

##Evaluate BERT text classification Model 

import matplotlib.pyplot as plt

def plot_graphs(history,metric):
    plt.plot(history.history[metric])
    plt.plot(history.history['val_'+ metric], '')
    plt.xlabel("Epochs")
    plt.ylabel(metric)
    plt.legend([metric,'val_'+ metric])
    plt.show()

plot_graphs(history, 'loss')

plot_graphs(history, 'binary_accuracy')

sample_example=["Are you gay?",
                "Why Donald Trump would make the most boring social media site ever?",
                "Why Colombia is the most corrupt country?",
                "Why is important to know programming? ",
                ]
                

test_data = tf.data.Dataset.from_tensor_slices((sample_example, [0]*len(sample_example)))
test_data = (test_data.map(to_feature_map).batch(1))
preds = model.predict(test_data)

preds

['Toxic' if pred >=0.005 else 'Sincere' for pred in preds]