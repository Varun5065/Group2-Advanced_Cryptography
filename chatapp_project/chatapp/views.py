from django.http import HttpResponse
from django.shortcuts import render
from chat.models import Chat
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from cryptography.fernet import Fernet
import base64
import hashlib
from Crypto.Cipher import AES
import os
from Crypto.Random import get_random_bytes


def encrypt(plain_text, key, iv): # encryption
    cipher = AES.new(key, AES.MODE_CBC, iv) # creating AES cipher object
    padded_text = plain_text + (AES.block_size - len(plain_text) % AES.block_size) * chr(AES.block_size - len(plain_text) % AES.block_size) # padding the input text
    encrypted_text = cipher.encrypt(padded_text.encode()) # encryption of text
    return base64.b64encode(encrypted_text).decode('utf-8') # returning cihertext in str format

def decrypt(cipher_text, key, iv): # decryption
    cipher_text = base64.b64decode(cipher_text) # converting str to bytes format
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(cipher_text) # decryption
    return decrypted_text[:-decrypted_text[-1]].decode('utf-8') # removing padding and returning the text

def get_data(request):
    data = Chat.objects
    data_l = list(data.values())
    print(data_l)
    return JsonResponse(data_l, safe=False)

key = b'\xa2g\xb4\xfbx\xf3\xa6\xb4\xdd\xd0\xf6\xc6\x1b|X\x02\x0c\x96fY]\xf1R\x7f\x1b\x8bM\xcer\x9f\xb3\xea' # key for excryption and decryption
iv = b'\x02##\xfd\xdeai\xd3Z\xd4}\x88\xa5d\xdb7' # initilaization vector

def homepage(request):
    return render(request, 'user1.html')

def user2(request):
    return render(request, 'user2.html')


def send(request):
    t1 = request.POST['text1'] # getting ddta from html page
    t2 = request.POST['user1']
    e_t1 = encrypt(t1, key, iv) # encryption of data
    t = Chat() # creating a instance of the model
    t.summary = e_t1 # 
    t.person = t2
    t.save() # saving the data into database
    p = Chat.objects.all() # calling the data to show
    data = []
    for i in p:
        i.summary = decrypt(i.summary, key, iv) # decrypting the data 
        data.append((i.person, i.summary))
    if t2 == 'John':
        return render(request, 'user1.html', {'data':data}) # sending the data into respective html pages.
    else:
        return render(request, 'user2.html', {'data':data})

def send1(request):
    print("here user2")
    t1 = request.POST['text2']
    t2 = request.POST['user2']
    # e_t1 = cipher.encrypt(t1.encode())
    t = Chat()
    #t.summary = e_t1.decode()
    t.person = t2
    t.save()
    p = Chat.objects.all()
    data = []
    for i in p:
        # i.summary = cipher.decrypt(i.summary.encode()).decode()
        data.append((i.person, i.summary))
    return render(request, 'user2.html', {'data':data})