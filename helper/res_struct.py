def res_str(msg, data):
    switcher = {
        'wait': 'لطفا صبر کنید',
        'internal_server_error': 'خطای داخلی سرور',
        'incorrect_username_or_password': 'نام کاربری یا رمز عبور نامعتبر',
        'invalid_email_address': 'آدرس ایمیل نامعتبر',
        'duplicate_username': 'نام کاربری تکراری',
        'duplicate_email': 'آدرس ایمیل تکراری',
        'username_required': 'عدم شناسایی نام کاربری',
        'password_required': 'عدم شناسایی رمز عبور',
        'email_required': 'عدم شناسایی آدرس ایمیل',
        'registered': 'ثبت نام موفقیت آمیز',
        'logged': 'ورورد موفقیت آمیز',
        'symbol_sign_required': 'عدم شناسایی کد نماد',
        'favorite_duplicate': 'نماد در لیست موجود است',
        'favorite_added': 'به علاقه مندی ها اضافه شد',
        'favorite_not_found': 'علاقه مندی موجود نیست',
        'explorer_not_found': 'نماد مورد تائیدی یافت نشد'
    }
    msg = switcher.get(msg, 'خطای سرور')
    return dict(
        msg=msg,
        data=data
    )