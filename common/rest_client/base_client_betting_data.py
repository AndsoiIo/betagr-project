import os

from common.rest_client.base_client import BaseClient


class BaseClientBettingData(BaseClient):

    _host = os.getenv('BETTING_DATA_API_HOST')
    _port = int(os.getenv('BETTING_DATA_API_PORT'))

    async def get_all_links(self, params=None):
        url = '/links'
        if params:
            url = f'{url}?data={params}'
        response = await self.get(api_uri=url)
        return response

    async def put_all_links(self, params=None):
        url = '/links'
        if params:
            url = f'{url}?data={params}'
        response = await self.put(api_uri=url)
        return response

    async def get_by_link(self, link_id, params=None):
        url = '/links/{link_id}'.format(link_id=link_id)
        if params:
            url = f'{url}?data={params}'
        response = await self.get(api_uri=url)
        return response

    async def put_by_link(self, link_id, params=None):
        url = '/links/{link_id}'.format(link_id=link_id)
        if params:
            url = f'{url}?data={params}'
        response = await self.put(api_uri=url)
        return response

    async def delete_by_link(self, link_id, params=None):
        url = '/links/{link_id}'.format(link_id=link_id)
        if params:
            url = f'{url}?data={params}'
        response = await self.delete(api_uri=url)
        return response

    async def change_status_team(self, team_id, json):
        url = '/change-status-team/{team_id}'.format(team_id=team_id)
        if not isinstance(json, dict):
            json = {}
        response = await self.patch(api_uri=url, data=json)
        return response