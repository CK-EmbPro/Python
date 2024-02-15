def reverse_transformation(ciphertext):
    plaintext = ""

    for i in range(len(ciphertext)):
        if i < 8:
            plaintext += ciphertext[i]
        elif i % 2 == 0:
            plaintext += chr(ord(ciphertext[i]) - 5)
        else:
            plaintext += chr(ord(ciphertext[i]) + 2)

    return plaintext

# Read the content from "rev_this" file
ciphertext = "picoCTF{w1{1wq85jc=2i0<}"
# Reverse the transformation
original_content = reverse_transformation(ciphertext)

# Print the original content
print("Original Content:", original_content)
