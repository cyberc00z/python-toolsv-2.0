###
  # url: https://web-and-mobile.readthedocs.io/en/latest/user-manual/sniffing.html:wq

#  Date : 13-March-2021
#  Author: Adhrit
#  Description: A python script for detecting if a user is using mobile phone or not.
###
try:
    from mobile.sniffer.wurfl.sniffer import WurlfSniffer

    #wrapper sniffer instance
    #All start-up delay goes up on this line
    sniffer = WurlfSniffer()

except ImportError , e:
    import traceback
    traceback.print_exc()
    logger.exception(e)
    logger.error("Could not import Wurlf sniffer... add pywurfl and python lehvenstein")
    sniffer = None


def sniff_request(req):
    
    """
   @param request: Request can be Django, WSGI or ZOPE HTTPRquest Object
   WSGI (web server gateway interface)  : Apporach for running Python web applications
   ZOPE HTTP REQ: zope http project
    """
    if not sniffer:
        # we failed to initialize Wurfl
        return None

    user_agent = sniffer.sniff(request)

    if user_agent == None:
        #no match in the mobile database
        return None
    else:
        return user_agent  #mobile.sniffer.wurlf.sniffer.UserAgent object


def web_or_mobile(req):
    ua = sniff_request(req)

    #search algorithm specified User Agent search
    certainty_threshold = 0.7

    if ua.get("is_wireless_device") and ua.getCertainty() > certainty_threshold:
        pass  #mobile browser
    else:
        pass #web browser




    
   


