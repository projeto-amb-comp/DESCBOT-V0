import requests

class SupabaseClient:
    def __init__(self, project_url, api_key):
        self.project_url = project_url
        self.api_key = api_key
        self.headers = {'apikey': api_key}

    def execute_query(self, sql):
        url = f"{self.project_url}/rest/v1/query"
        payload = {"type": "run_sql", "args": {"sql": sql}}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()
