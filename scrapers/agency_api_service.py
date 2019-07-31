import requests
from scrape_data import scrape_data

class AgencyApiService:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api/agencies"

    def get_all_agencies(self):
        try:
            agency_list = self._get(self.base_url)
            # I was not able to find a way to get the count of the agencies. so first making a call to get the count and then passing the count to get all the agencies
            # Instead of getting everything, get the agencies 20 at a time (pagesize)
            agency_count = len(agency_list)
            all_agency_url = f"{self.base_url}?limit={agency_count}"
            all_agency_list = self._get(all_agency_url)
            return all_agency_list
        except Exception as ex:
            print(f"Error while retrieving all the agency information: {str(ex)}")

    def _get(self, url):
        response = requests.get(url,headers={'Content-type': 'application/json'})
        return response.json()

if __name__=="__main__":
    svc = AgencyApiService()
    agens = svc.get_all_agencies()
    scraped = scrape_data(agens)
    import pdb;pdb.set_trace()
    print ("SCRAPED")

