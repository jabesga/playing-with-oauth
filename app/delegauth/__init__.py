from app import app
from flask import redirect
import requests
from requests_oauthlib import OAuth1Session

class Delegauth():
    def login_with(self, provider):
        if provider == 'facebook':
            app_id = app.config['DELEGAUTH_PROVIDERS'][provider]['app_id']
            scope = app.config['DELEGAUTH_PROVIDERS'][provider]['scope']
            redirect_uri = app.config['DELEGAUTH_PROVIDERS'][provider]['redirect_uri']

            url = 'https://www.facebook.com/dialog/oauth?client_id={0}&redirect_uri={1}&scope={2}'.format(
            app_id, redirect_uri, scope)
            return redirect(url)
        # elif provider == 'twitter':
        #     consumer_key = app.config['DELEGAUTH_PROVIDERS'][provider]['consumer_key']
        #     consumer_secret = app.config['DELEGAUTH_PROVIDERS'][provider]['consumer_secret']
        #     redirect_uri = app.config['DELEGAUTH_PROVIDERS'][provider]['redirect_uri']
        #     url = 'https://api.twitter.com/oauth/request_token'
        # 
        #     oauth = OAuth1Session(consumer_key, consumer_secret)
        #     json_response = oauth.fetch_request_token(url)
        #     #response = requests.post(url, headers={'Authorization': auth_data})
        #
        #     if json_response['oauth_callback_confirmed']:
        #         oauth_token = json_response['oauth_token']
        #         json_response['oauth_token_secret']
        #         url = 'https://api.twitter.com/oauth/authenticate?oauth_token={0}'.format(oauth_token)
        #         return redirect(url)

    def callback(self, request, provider):
        if provider == 'facebook':
            code = request.args.get('code')
            app_id = app.config['DELEGAUTH_PROVIDERS'][provider]['app_id']
            app_secret = app.config['DELEGAUTH_PROVIDERS'][provider]['app_secret']
            redirect_uri = app.config['DELEGAUTH_PROVIDERS'][provider]['redirect_uri']

            url = 'https://graph.facebook.com/v2.3/oauth/access_token?client_id={0}&redirect_uri={1}&client_secret={2}&code={3}'.format(
            app_id, redirect_uri, app_secret, code)
            response = requests.get(url)

            return response.json()
