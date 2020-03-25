profile = {
    "Jun": {
        "assets":{
            # organize assets by financial institution
            "Chase": {
                "checking": 0, 
                "savings": 0,
            }, 
            "Citibank": {
                "checking": 100, 
                "savings": 0,
            }, 
            "PayPal": {
                "balance": 10, 
                "account_status": "activated",
            }
        },
        "biometrics": {
            "sex": "male", 
            "eye-color": "brown",
        },
        "contact-info": {   
            "cell": 1234567890,
            "email": "tech@ascendbaruch.org",
        }
    }
}

print(profile["Jun"]["assets"]["Citibank"]["checking"])
