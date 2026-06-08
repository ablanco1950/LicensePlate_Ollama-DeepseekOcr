# Asking IA de Bing
# how call ollama from a python program
#  Modified by Alfonso Blanco
#
# https://john-tucker.medium.com/ollama-by-example-part-1-22f01acc1821
# Quickstart - Ollama 
# https://docs.ollama.com/quickstart

#dirname="C:\LicensePlate_Ollama\Test"
dirname="Test"


import time
Ini=time.time()



import ollama

def query_ollama(model: str, prompt: str) -> str:
    """
    Query an Ollama model and return the generated text.
    """
    try:
        # Send request to Ollama
        response = ollama.chat(model=model, messages=[
            {"role": "user", "content": prompt}
        ])
        
        # Extract and return the model's reply
        return response['message']['content']
    
    except Exception as e:
        return f"Error: {e}"

import os
import re
def loadimages (dirname):

     imgpath = dirname + "\\"
     
     #images = []
     TabLicenses=[]
     TabFilePath=[]
    
     print("Reading imagenes from ",imgpath)
     NumImage=-2
     
     Cont=0
     for root, dirnames, filenames in os.walk(imgpath):
        
         NumImage=NumImage+1
         
         for filename in filenames:
             
             if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                 
                 
                 filepath = os.path.join(root, filename)
                 License=filename[:len(filename)-4]
                 
                 TabFilePath.append(filepath)
                 TabLicenses.append(License)
                 
                 Cont+=1
     
     return  TabFilePath, TabLicenses
     
# MAIN


TabFilePath, TabLicenses= loadimages (dirname)
    

model_name = "deepseek-ocr"  

user_prompt_fix ="text of license plate from car in image "



ContHits=0
ContFailures=0

for i in range(len(TabFilePath)):
    user_prompt=user_prompt_fix + TabFilePath[i]

    print("Asking Ollama: " + user_prompt)
    
    result = query_ollama(model_name, user_prompt)
    
    print("Ollama response: ", result)

    cadena=""

    
    posicion=result.find("and is from a car in the image")
    if posicion != -1 :
           #print(posicion) 
           result= result[:posicion ]
   
    posicion=result.find("and is located on a car in the image")
    if posicion != -1 :
            
           result= result[:posicion ]


    posicion=result.find("The image shows")
    if posicion != -1 :
           
           result= result[:posicion ]

    posicion=result.find("and the text is")
    if posicion != -1 :
            
           result= result[:posicion ]
           
    posicion=result.find("The license plate is from a car, and the image is a screenshot of the car's dashboard.")
    if posicion != -1 :
           result= result[:posicion ]
                         
    posicion=result.find("The license plate in the image is from a car and reads")
    if posicion != -1 :
        
       cadena= result[posicion +len("The license plate in the image is from a car and reads")+1:]
       result=cadena
       
       cadena = cadena.replace('"', '')
       
       cadena = cadena.replace('.', '')
       
    posicion=result.find("and it is located on a car in the image")
    if posicion != -1 :
       result=result[:posicion]
       
    posicion=result.find('is')
    if posicion != -1 :
       
       cadena= result[posicion+3:]
       
       cadena = cadena.replace('"', '')
       
       cadena = cadena.replace('.', '')
     

    posicion=result.find("The license plate reads")
    if posicion != -1 :
        
       cadena= result[len("The license plate reads")+1:]
       
       cadena = cadena.replace('"', '')
       
       cadena = cadena.replace('.', '')
  
    
    cadena=cadena.strip()
    print("After cleaning text, returns: " +cadena)
    if cadena==  TabLicenses [i]:
        print ("HIT the License Plate is " + cadena)
        ContHits=ContHits+1
    else:
        print ("FAILURE the License Plate is " + TabLicenses [i])
        ContFailures=ContFailures+1
    print("")
    print("")
    
print ( "HITS=" + str(ContHits))
print("FAILURES=" + str(ContFailures))

print( " Time in seconds "+ str(time.time()-Ini))
