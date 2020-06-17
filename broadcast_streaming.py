# Importing the required third-party libraries
import requests
from bs4 import BeautifulSoup

# Browser information we send in order not to be blocked by the site
headers = requests.utils.default_headers()
headers.update({
'User-Agent': 'Chrome Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36,gzip(gfe)',
})

# Specifies the field to request and html / lxml conversion.
print("Please wait... Channels download...\n")
url = "https://canlitv.com/yayin-akisi/"
my_request = requests.get(url)
soup = BeautifulSoup(my_request.content, "lxml")

# Printing the channels
print("**********CHANNEL LIST**********")
print("1)Trt 1\n2)Star Tv\n3)Ntv\n4)Show Tv\n5)Fox\n6)Kanal D\n7)360 Tv\n8)CNN Turk\n9)Tv8\n10)Yaban Tv\n11)TLC\n"
      "12)Disney Channel\n13)Cartoon Network\n14)Trt Belgesel\n15)Trt Spor\n")

# HANDLING EXCEPTION PART
# Input will be taken as an integer by user. If user enters a string or something else,
# the programs catch the mistake, and print that not correct
while True:
    try:
        choice = int(input("\nPlease enter a number to see broadcast stream.."))
        break

    except ValueError:
        print("Oops! That was no valid number. Try again...")


# In this part, the channels' broadcast streams' paths are specified
# Broadcast streams are procured their own class and every channel has different path, so they are written separate
# find(): It allows you to draw a special value in the page source
# First access to li label, then access to class and channel's url address, the attrs dictionary as a parameter
# Text method was used to remove html tags and just access the text

trt = soup.find("li", attrs={"class":"yayin-akisi-5"}).text                 # url address with li class = ”yayin-akisi-5” is fetched for TRT 1
star = soup.find("li", attrs={"class":"yayin-akisi-99"}).text               # url address with li class = ”yayin-akisi-99” is fetched for STAR TV
ntv = soup.find("li", attrs={"class":"yayin-akisi-6"}).text                 # url address with li class = ”yayin-akisi-6” for NTV is fetched
show = soup.find("li", attrs={"class":"yayin-akisi-4"}).text                # url address with li class = ”yayin-akisi-4” for SHOW TV is fetched
fox = soup.find("li", attrs={"class":"yayin-akisi-11221"}).text             # url address with li class = ”yayin-akisi-11221” for FOX is fetched
kanald = soup.find("li", attrs={"class":"yayin-akisi-2"}).text              # url address with li class = ”yayin-akisi-2” for KANAL D is fetched
threesixzero = soup.find("li", attrs={"class":"yayin-akisi-15"}).text       # url address with li class = ”yayin-akisi-15” for 360 is fetched
cnn = soup.find("li", attrs={"class":"yayin-akisi-11222"}).text             # url address with li class = ”yayin-akisi-11222” for CNN TURK is fetched
tv8 = soup.find("li", attrs={"class":"yayin-akisi-10924"}).text             # url address with li class = ”yayin-akisi-10924” for TV 8 is fetched
yabantv = soup.find("li", attrs={"class":"yayin-akisi-12044"}).text         # url address with li class = ”yayin-akisi-12044” for YABAN TV is fetched
tlc = soup.find("li", attrs={"class":"yayin-akisi-11219"}).text             # url address with li class = ”yayin-akisi-11219” for TLC is fetched
disney = soup.find("li", attrs={"class":"yayin-akisi-12440"}).text          # url address with li class = ”yayin-akisi-12440” for DISNEY CHANNEL is fetched
cartoon = soup.find("li", attrs={"class":"yayin-akisi-11233"}).text         # url address with li class = ”yayin-akisi-11233” for CARTOON NETWORK is fetched
trtdoc = soup.find("li", attrs={"class":"yayin-akisi-11106"}).text          # url address with li class = ”yayin-akisi-11106” for TRT BELGESEL is fetched
trtsport = soup.find("li", attrs={"class":"yayin-akisi-893"}).text          # url address with li class = ”yayin-akisi-893” for TRT SPOR is fetched


# USER'S CHOICE PART
# According to input, intended channel's broadcast stream prints

if choice == 1:
    print("\n\n\n\n\n\n\n TRT 1 BROADCAST STREAM")
    print(trt)
elif choice == 2:
    print("\n\n\n\n\n\n\n STAR TV BROADCAST STREAM")
    print(star)
elif choice == 3:
    print("\n\n\n\n\n\n\n NTV BROADCAST STREAM")
    print(ntv)
elif choice == 4:
    print("\n\n\n\n\n\n\n SHOW TV BROADCAST STREAM")
    print(show)
elif choice == 5:
    print("\n\n\n\n\n\n\n FOX BROADCAST STREAM")
    print(fox)
elif choice == 6:
    print("\n\n\n\n\n\n\n KANAL D BROADCAST STREAM")
    print(kanald)
elif choice == 7:
    print(threesixzero)
    print("360 TV BROADCAST STREAM")
elif choice == 8:
    print("\n\n\n\n\n\n\n CNN TURK BROADCAST STREAM")
    print(cnn)
elif choice == 9:
    print("\n\n\n\n\n\n\n TV 8 BROADCAST STREAM")
    print(tv8)
elif choice == 10:
    print("\n\n\n\n\n\n\n YABAN TV BROADCAST STREAM")
    print(yabantv)
elif choice == 11:
    print("\n\n\n\n\n\n\n TLC BROADCAST STREAM")
    print(tlc)
elif choice == 12:
    print("\n\n\n\n\n\n\n DISNEY CHANNEL BROADCAST STREAM")
    print(disney)
elif choice == 13:
    print("\n\n\n\n\n\n\n CARTOON NETWORK BROADCAST STREAM")
    print(cartoon)
elif choice == 14:
    print("\n\n\n\n\n\n\n TRT BELGESEL BROADCAST STREAM")
    print(trtdoc)
elif choice == 15:
    print("\n\n\n\n\n\n\n TRT SPOR BROADCAST STREAM")
    print(trtsport)
else:                     # If user enters a number which is not between 1 and 15, program requests to enter a new value
    int(input("Invalid value..Please enter a number between 1 - 15...."))


"""
channels = soup.find_all("div", {"id": "yayin-akislari"})

channel_list = channels[0].contents[len(channels[0].contents) - 2]

channel_list = channel_list.find_all("li")

for channel in channel_list:                                    ...this part shows all channels' broadcast stream...
    channel_name = channel.find_all("span")               
    broadcast_streaming = channel_name[0].text
    print(broadcast_streaming)
    print("******************")
"""
