# LicensePlate_Ollama-DeepseekOcr
A Python program that reads car license plates from an image folder using Ollama with the deepseek-ocr model and processes the received text to retrieve the license plate number. It runs locally and does not require any API key.

Requirements:

In addition to having a local version of Ollama that allows you to select the deepseek-ocr model, the program must have at least 6.0 GB of free RAM, which the deepseek-ocr model requires.

Download the project to a disk folder and extract the Test.zip file, which contains a set of 25 Roboflow test images.

If Ollama is not already installed, you can download it from:

Ollama downloads page: https://docs.ollama.com/quickstart

And

Run the downloaded OllamaSetup.exe, which provides a graphical interface for running queries to Ollama.

In the project runtime environment, install the Ollama module:

pip install ollama

Test:

Run the program:

python GetNumberLicensePlate_Ollama-DeepseekOcr.py

The console will display messages indicating the image being processed, the text response from Ollama, and the extraction of the license plate number from the text, indicating whether the prediction was correct or not. The test images are named with the car's license plate number to allow for verification.

The console appears:

= RESTART: C:\LicensePlate_Ollama-DeepseekOcr\GetNumberLicensePlate_Ollama-DeepseekOcr.py
Reading images from C:\LicensePlate_Ollama\Test\
Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\01CC1A0001.png
Ollama response: The text on the license plate is "CC1A0001".
After cleaning text, returns: CC1A0001
FAILURE the License Plate is 01CC1A0001


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\067RAF.png
Ollama response: The license plate number is "067RAF".
After cleaning text, returns: 067RAF
HIT the License Plate is 067RAF


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\12682011.png
Ollama response: The license plate number is "12682011".
After cleaning text, returns: 12682011
HIT the License Plate is 12682011


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\172TMJ.png
Ollama response: The license plate number is "172TMJ".

The license plate is from a car, and the image is a screenshot of the car's dashboard. The license plate is located in the center of the image, and the text is clearly visible.
After cleaning text, returns: 172TMJ
HIT the License Plate is 172TMJ


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\8544.png
Ollama response: The license plate number is "8544".

The license plate is from a car, and the image is a screenshot of the car's dashboard. The license plate is located on the front of the car, and the image is taken from a slightly elevated angle, showing the entire license plate.
After cleaning text, returns: 8544
HIT the License Plate is 8544


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\BAD231.png
Ollama response: The license plate number is "Ollama" and the text is "Test".
After cleaning text, returns: Ollama
FAILURE the License Plate is BAD231


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\BMW.png
Ollama response: The license plate number is "BMW".

The image shows a white car with a black and white license plate. The license plate is from a BMW car, as indicated by the text "BMW" at the top of the plate. The license plate number is "BMW" and is located in the center of the plate. The plate is rectangular in shape and has a black background with white lettering. The text is in a standard font and is easy to read. The license plate is mounted on the front of the car and is visible to other drivers on the road.
After cleaning text, returns: BMW
HIT the License Plate is BMW


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\CRAIG.png
Ollama response: The license plate reads "CRAIG" and is located on a car in the image.
After cleaning text, returns: CRAIG
HIT the License Plate is CRAIG


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\DRUNK.png
Ollama response: The license plate number is "DRUNK" and the text is "Test".
After cleaning text, returns: DRUNK
HIT the License Plate is DRUNK


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\EWWPOOP.png
Ollama response: The text on the license plate is "EWWPOOP".
After cleaning text, returns: EWWPOOP
HIT the License Plate is EWWPOOP


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\G526JHD.png
Ollama response:  The license plate number is "G526JHD".
After cleaning text, returns: G526JHD
HIT the License Plate is G526JHD


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\HR26BC55I4.png
Ollama response:  The text on the license plate is "HR26BC5".
After cleaning text, returns: HR26BC5
FAILURE the License Plate is HR26BC55I4


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\KA03MG2784.png
Ollama response:  The text on the license plate is "KA03".
After cleaning text, returns: KA03
FAILURE the License Plate is KA03MG2784


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\LR33TEE.png
Ollama response:  The license plate reads "LR33TEE".
After cleaning text, returns: LR33TEE
HIT the License Plate is LR33TEE


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\MH12NE8922.png
Ollama response:  The text on the license plate is "MH12NE8922".
After cleaning text, returns: MH12NE8922
HIT the License Plate is MH12NE8922


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\MH149239GN.png
Ollama response:  The license plate number is "MH149239GN".
After cleaning text, returns: MH149239GN
HIT the License Plate is MH149239GN


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\MH14LC35B7.png
Ollama response:  The text on the license plate is "MH14LC3B7".
After cleaning text, returns: MH14LC3B7
FAILURE the License Plate is MH14LC35B7


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\MH20EE7596.png
Ollama response:  The license plate of a car in the image C:\LicensePlate_Ollama\Test\MH20text of license plate from car in image C:\LicensePlate_Ollama\Test\MHtext of license plate from car in image C:\LicensePlate_Ollama\Test\MH2
After cleaning text, returns: 
FAILURE the License Plate is MH20EE7596


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\OX65AWD.png
Ollama response:  The text on the license plate is "OX65AWD".
After cleaning text, returns: OX65AWD
HIT the License Plate is OX65AWD


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\P3RVP.png
Ollama response:  The text on the license plate is "P3RVP".
After cleaning text, returns: P3RVP
HIT the License Plate is P3RVP


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\PETE1.png
Ollama response:  The license plate number is "PETE1".

The license plate is from a car, and the image is a screenshot of the car's dashboard. The license plate is located in the center of the image, and the text is clearly visible.
After cleaning text, returns: PETE1
HIT the License Plate is PETE1


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\RK977AF.png
Ollama response:  The license plate reads "RK977AF".
After cleaning text, returns: RK977AF
HIT the License Plate is RK977AF


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\SGQ51JU.png
Ollama response:  The license plate number is "SGQ51JU".
After cleaning text, returns: SGQ51JU
HIT the License Plate is SGQ51JU


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\SKIPGAS.png
Ollama response:  The license plate reads "SKIPGAS" and is from a car in the image.
After cleaning text, returns: SKIPGAS
HIT the License Plate is SKIPGAS


Asking Ollama: text of license plate from car in image C:\LicensePlate_Ollama\Test\VIPER.png
Ollama response:  The license plate number is "Ollama" and the text is "VIPER".
After cleaning text, returns: Ollama
FAILURE the License Plate is VIPER


HITS=18
FAILURES=7
 Time in seconds 47.75436210632324
>>> 

An Excel spreadsheet, comparisons.xls, is attached with the comparison performed with other systems:

GEMINI 3.15Flash

https://gemini.google.com/app?is_sa=1&is_sa=1&android-min-version=301356232&ios-min-version=322.0&campaign_id=bkws&utm_source=sem&utm_medium=paid-media&utm_campaign=bkws&pt=9008&mt=8&ct=p-growth-sem-bkws&gclsrc=aw.ds&gad_source=1&gad_campaignid=21109724629&gbraid=0AAAAApk5BhmDjTo4XpkVXFQbsaie5ghxv&gclid=Cj0KCQjww8rQBhDjARIsAE43KPMA9JbdHp2L-u_sng5le5CmmfF_xD8iZdC8TANsiOOTQH4jgrF7ONoaAgiSEALw_wcB

https://www.doubango.org/webapps/alpr/	

https://huggingface.co/spaces/ankandrew/fast-alpr	

https://github.com/ablanco1950/LicensePlate_Yolov8_Filters_PaddleOCR	

Note:
The program will need to be modified to account for all of Ollama's possible responses, which don't appear to be many.
The system's excessive sensitivity has been verified: changing the directory where an image is located causes Ollama DeepSeek-OCR to fail to recognize it, for no apparent reason.


