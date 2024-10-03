def validate_email(email):
    import re
    pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.match(pattern, email)

result = validate_email('Ralph.Kemperdick@RaKeTeTechnology.com')
print(result)