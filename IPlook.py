# IP Look Up Service 

from simple_geoip import GeoIP

API_KEY = ""  #grab from https://ip-geolocation.whoisxmlapi.com

def main():
    IP = input("Enter target's IP address: ")
    #initiate geoip components
    geoip = GeoIP(API_KEY)
    response = geoip.lookup(IP)
    print(response)

if __name__ == "__main__":
    main()
