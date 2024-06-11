from duckduckgo_search import DDGS
import imageio 
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from term_image.image import from_url

#text search
# results = DDGS().text("birds", max_results = 5)
# print(results)

#image search
def images():
    results = DDGS().images(keywords="bird",max_results=10)
    #get url
    img_url = results[0].get("image")
    print(img_url)
    #headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(img_url,headers=headers)

    print(response.status_code)

    #read image
    image = imageio.imread(BytesIO(response.content))
    plt.imshow(image)
    plt.axis('off')
    plt.show()


def showImagesInTerminal():
    results = DDGS().images(keywords="bird",max_results=10)
    #get url
    urls = [img.get("image") for img in results]

    #get individual url and print
    for url in urls:
        try:
            response = requests.get(url=url)

            if response.status_code == 200:
                img_url = from_url(url)
            else:
                print((f"Failed to fetch image from {url}. Status code: {response.status_code}", "red"))
        except(ConnectionError, TimeoutError):
            print((f"Connection error or timeout occurred while fetching image from {url}. Retrying...", "yellow"))
    
    print(img_url)
    
showImagesInTerminal()