import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_page(self):
        """Fetches the web page content."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check for HTTP errors
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching the page: {e}")
            self.soup = None

    def find_elements(self, tag, class_name=None):
        """Finds and returns elements by tag and optional class."""
        if self.soup:
            if class_name:
                return self.soup.find_all(tag, class_=class_name)
            return self.soup.find_all(tag)
        return []

    def extract_text(self, tag, class_name=None, first_only=False):
        """Extracts and returns text from elements by tag and optional class."""
        elements = self.find_elements(tag, class_name)
        if first_only and elements:
            return elements[0].text.strip().replace('\n                            ', ' ')
        return [elem.text.strip().replace('\n                            ', ' ') for elem in elements]

    def extract_teams(self):
        """Extracts team data from the page and returns a list of dictionaries."""
        teams = []
        if self.soup:
            for team in self.soup.find_all('tr', class_='team'):
                name = team.find('td', class_='name').text.strip()
                wins = team.find('td', class_='wins').text.strip()
                losses = team.find('td', class_='losses').text.strip()
                teams_dict = {
                    'Team': name,
                    'Wins': wins,
                    'Losses': losses,
                }
                teams.append(teams_dict)
        return teams

if __name__ == "__main__":
    url = 'https://www.scrapethissite.com/pages/forms/'
    scraper = WebScraper(url)
    
    scraper.fetch_page()

    # Example usage
    divs = scraper.find_elements('div', 'col-md-12')
    print(f"Found {len(divs)} divs with class 'col-md-12'.")

    lead_paragraphs = scraper.find_elements('p', 'lead')
    print(f"Found {len(lead_paragraphs)} paragraphs with class 'lead'.")

    lead_text = scraper.extract_text('p', 'lead', first_only=True)
    print(f"Lead paragraph text: {lead_text}")

    teams = scraper.extract_teams()
    print("Extracted teams:")
    for team in teams:
        print(team)
