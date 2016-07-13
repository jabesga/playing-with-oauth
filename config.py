WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

DELEGAUTH_PROVIDERS = {
    'facebook': {
        'app_id': '910282312434799',
        'app_secret': '147620079f74362e3bcae28484d15a5a',
        'scope': 'public_profile,email',
        'redirect_uri': 'http://localhost:5000/callback/facebook'
    },
    # 'twitter':{
    #     'consumer_key': 'IxdbF9n5XSPiK9w97sN1Hkuft',
    #     'consumer_secret': 'T1fL96PTTLZTyWIl58kYzbc2Ah8TqAHsC4fixpXKrhBSSiz3X6',
    #     'redirect_uri': 'http://localhost:5000/callback/twitter'
    # }
}
