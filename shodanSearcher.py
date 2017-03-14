import shodan
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

api = shodan.Shodan("PLACE YOUR API KEY HERE")


def complete_search(p1):
    try:
        results = api.search(p1)
        f = open('results.txt', 'w')
        f.write("Results found: %s" % results['total'])
        print ("Results found: %s" % results['total'])
        for result in results['matches']:
            try:
                f.write(' ')
                f.write('IP: %s' % result['ip_str'])
                f.write(' ')
                f.write(result['ip_str'])
                f.write(' ')
                f.write(result['data'])
                f.write(' ')
                """print ('IP: %s' % result['ip_str'])
                print (result['ip_str'])
                print (result['data'])
                print ('')"""
            except:
                print "error"
                pass
        f.close()
        print "DONE, see the results file"
    except shodan.APIError, e:
        print ('Error: %s' % e)


def basic_search(p2):
    try:
        result = api.search(p2)
        f = open('results.txt', 'w')
        print ("Results found: %s" % result['total'])
        f.write("Results found: %s" % results['total'])
        for service in result['matches']:
            try:
                print (service['ip_str'])
                f.write(service['ip_str'])
            except:
                pass
        f.close()
        print "DONE, see the results file"
    except Exception as e:
        print ('Error: %s' % e)
        sys.exit(1)


def specific_search(p3):
    host = api.host(p3)
    f = open('results.txt', 'w')
    try:
        f.write("""
                IP: %s
                Organization: %s
                Operating System: %s
                """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        # print ("""
        #         IP: %s
        #         Organization: %s
        #         Operating System: %s
        #         """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        # Print all banners
        for item in host['data']:
             f.write ("""
                        Port: %s
                        Banner: %s

                        """ % (item['port'], item['data']))
             # print ("""
             #            Port: %s
             #            Banner: %s
             #
             #            """ % (item['port'], item['data']))
    except:
        pass
    f.close()
    print "DONE, see the results file"


def main():
    print """\
              /$$$$$$  /$$                       /$$
             /$$__  $$| $$                      | $$
            | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$$
            |  $$$$$$ | $$__  $$ /$$__  $$ /$$__  $$ |____  $$| $$__  $$
             \____  $$| $$  \ $$| $$  \ $$| $$  | $$  /$$$$$$$| $$  \ $$
             /$$  \ $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$
            |  $$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$
             \______/ |__/  |__/ \______/  \_______/ \_______/|__/  |__/
              /$$$$$$                                          /$$
             /$$__  $$                                        | $$
            | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$
            |  $$$$$$  /$$__  $$ |____  $$ /$$__  $$ /$$_____/| $$__  $$ /$$__  $$ /$$__  $$
             \____  $$| $$$$$$$$  /$$$$$$$| $$  \__/| $$      | $$  \ $$| $$$$$$$$| $$  \__/
             /$$  \ $$| $$_____/ /$$__  $$| $$      | $$      | $$  | $$| $$_____/| $$
            |  $$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$| $$  | $$|  $$$$$$$| $$
             \______/  \_______/ \_______/|__/       \_______/|__/  |__/ \_______/|__/

              By Dviros
    """
    print "Select search type:"
    print "1 = Comprehensive search (returned as JSON, can be used for IP's and keywords)"
    print "2 = Basic search (Used for keywords, can be used also with IPs)"
    print "3 = Specific known IP search"
    selection = input()

    if selection is 1:
        print ("What's the IP?")
        complete_search(raw_input())
    if selection is 2:
        print ("What's the IP \ keyword?")
        basic_search(raw_input())
    if selection is 3:
        print ("What's the IP?")
        specific_search(raw_input())
    if selection > 3 or selection < 1:
        print ("Invalid selection.")
        time.sleep(1)
        main()


main()
