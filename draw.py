# Tidbyt Graph Generator
# Create a grid and plot a graph line on it.
# Author: Dean Abraham

from PIL import Image, ImageDraw
from io import BytesIO 
import random, json, requests, base64

#Device and API Key variables
deviceID = "moistly-triumphant-bewitching-grackle-e23"
Key = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjY1YzFhMmUzNzJjZjljMTQ1MTQyNzk5ODZhMzYyNmQ1Y2QzNTI0N2IiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJodHRwczovL2FwaS50aWRieXQuY29tIiwiZXhwIjoxNjg4NDk0NjQ5LCJpYXQiOjE2NTY5NTg2NDksImlzcyI6Imh0dHBzOi8vYXBpLnRpZGJ5dC5jb20iLCJzdWIiOiJ4MjBFbjEwbzhHVG5PRFRhWGRoQ0JoR0U3M1QyIiwic2NvcGUiOiJkZXZpY2UiLCJkZXZpY2UiOiJtb2lzdGx5LXRyaXVtcGhhbnQtYmV3aXRjaGluZy1ncmFja2xlLWUyMyJ9.VZRBqMza7T-McjBAeLqjFpz9i30bfG_OTQtEMqZOis3SpK2NBz-RcPtETJ6BJY9ASbbMiWeqa0qhHKHUkNTvcA"
#Options
Animate = False
RandomColor = True

def newGrid(): #Create an image with a grid
    img = Image.new('RGB', (64, 32))
    gridSize = random.randrange(4,15,1)
    draw = ImageDraw.Draw(img)
    for x in range(gridSize,64,gridSize):
        draw.line((x,0) + (x,img.height), fill=(0,155,0))
    for x in range(gridSize,32,gridSize):
        draw.line((0,x) + (img.width,x), fill=(0,155,0))
    return img

def toTheBase(myImage): #Convert to base64 string
    byte_io = BytesIO()
    if(Animate):
        myImage[0].save(byte_io,'GIF',save_all=True, append_images=myImage[1:], optimize=False, duration=40, loop=0)
        myImage[0].save('animated.GIF',save_all=True, append_images=myImage[1:], optimize=False, duration=40, loop=0)
    else:
        myImage.save(byte_io,'GIF')
    imgString = base64.b64encode(byte_io.getvalue())
    imgString = imgString.decode('utf-8')
    return imgString
    
def SendToTidbyt(b64Img): #Push image to Tidbyt
    jBody = json.dumps({'image': b64Img, 'installationID': 'Deans'})
    api_url = "https://api.tidbyt.com/v0/devices/" + deviceID + "/push"
    header = {"Content-Type":"application/json", "Authorization": "Bearer " + Key}
    response = requests.post(api_url,data=jBody,headers=header)
    if (response.status_code == 200):
        print("Succesfully sent image to Tidbyt")
    else:
        print("Something went wrong")
        print(response.json())
    return response.json()

def fakeData(Chart): #Create random datapoints and add to grid
    pointCount = random.randrange(3,15)
    dataPoints = [((0,random.randrange(0,32)))]
    #randColor = ((random.randrange(0,155)),(random.randrange(0,155)),(random.randrange(0,155)))
    randColor = (155,0,0)
    draw = ImageDraw.Draw(Chart)
    for x in range(1,64,pointCount):
        dataPoints.append((x,(random.randrange(0,32))))
    dataPoints.append((64,random.randrange(0,32)))
    for x in range(1,len(dataPoints),1):
        draw.line(dataPoints[x-1]+dataPoints[x], fill=randColor)
        if(Animate):
            animChart.append(Chart)
    #TODO: Size text and generate fake data name
    #draw.text((0,0),"Deans Grid", randColor)
    if(Animate):
        return animChart
    else:
        return Chart

#Main Run Steps
#TODO: Animate https://note.nkmk.me/en/python-pillow-gif/
myGrid = newGrid()
if(Animate):
    animChart = []
myData = fakeData(myGrid)
if(Animate):
    myImg = toTheBase(animChart)
    myImg = Image.open(BytesIO(base64.decodebytes(bytes(myImg, "utf-8"))))
    myImg = base64.b64decode(myImg)
    myImg = myImg.decode('utf-8')
    #myImg.show()
else:
    myData.show()
response = SendToTidbyt(myData)