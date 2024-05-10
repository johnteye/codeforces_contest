import base64

encoded_string = "9pYLXRE47uBgJG450W62CYB" 
decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8') # if the data is a utf-8 string

print(decoded_string)
