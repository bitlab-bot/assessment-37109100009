import requests


class RickAndMortyClient:

    ENDPOINT = "https://rickandmortyapi.com/api/episode/"

    def fetch_and_sort_episodes(self):
        episodes = self.get_episodes(self.ENDPOINT)
        self.sort_episodes_by_air_date(episodes)
        return episodes

    def get_episodes(self, url, data=[]):
        response = requests.get(url)

        if response.status_code >= 200 and response.status_code < 300:
            # success
            response_data = response.json()
            next_page = response_data['info']['next']

            if len(next_page) > 0:
                # has more data, fetch it!
                return self.get_episodes(next_page, response_data['results'])
            else:
                return data + response_data['results']
        else:
            raise Exception('Error: {}'.format(response.text))

    def sort_episodes_by_air_date(self, episodes):
        return episodes.sort(key=lambda x: x['air_date'][-4:])
