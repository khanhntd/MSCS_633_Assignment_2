import qrcode

# generateQRCode will generate a QR code for a url link
def generateQRCode(urlString: str, fileName: str) -> None:
    img = qrcode.make(urlString)
    img.save(fileName)

if __name__ == "__main__":
    urlString = input("Enter your url: ")
    fileName = input("Enter file name: ")
    #urlString = 'https://help.blackboard.com/SafeAssign/Student/Originality_Report'
    #fileName = './blackboard.png'
    generateQRCode(urlString,fileName)