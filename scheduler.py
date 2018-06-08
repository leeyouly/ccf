
if __name__ == '__main__':
    import urllib
    import urllib2
    import logging
    import time
    import json
    logging.basicConfig(level=logging.DEBUG)

    def fetch(url):
        response = urllib2.urlopen(url)
        data = json.loads(response.read())
        return data
    while True:
        try:
            host = 'http://localhost:6800/'
            projects = fetch(host + 'listprojects.json')
            
            for project in projects['projects']:
                try:
                    project_jobs = fetch(host + 'listjobs.json?project=%s' %(project,))
                    
                    if len(project_jobs['pending'])>0 or len(project_jobs['running'])>0:
                        continue
                        
                    project_spiders = fetch(host + 'listspiders.json?project=%s' % (project,))
                    for spider in project_spiders['spiders']:
                        print project, spider
                        
                        data = urllib.urlencode({'project' : project, 'spider' : spider})
                        req = urllib2.Request(host + 'schedule.json', data)
                        response = urllib2.urlopen(req)
                        the_page = response.read()
                        logging.info(the_page)
                except Exception as e:
                    print e
                    pass
                
                
        except Exception as e:
            print e
            pass
        
        time.sleep(10*60)
