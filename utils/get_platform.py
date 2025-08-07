def get_platform(capabilities):
    lt_options = capabilities.get("LT:Options", {})
    device_name = lt_options.get("deviceName", "").lower()
    platform_name = lt_options.get("platformName", "").lower()
    is_real_mobile = str(lt_options.get("isRealMobile", "")).lower() == "true"

    TREAT_AS_DESKTOP_TABLETS = [
        "galaxy tab s8+", 
        "galaxy tab a8", 
        "ipad air 11 (2024)", 
        "ipad pro 13 (2024)", 
        "ipad 10.9 (2022)", 
        "ipad (9th generation)",

    ]

    TREAT_AS_MOBILE_DEVICES = [
        "galaxy tab s9", 
        "galaxy tab s8", 
        "ipad mini (2021)"
    ]
    TREAT_AS_MOBILE_DEVICES = [
    ]
    device_name_clean = device_name.lower()


    if device_name_clean in [d.lower() for d in TREAT_AS_MOBILE_DEVICES]:
        platform = "mobile"
    elif device_name_clean in [d.lower() for d in TREAT_AS_DESKTOP_TABLETS]:
        platform = "desktop"
    elif is_real_mobile or platform_name in ("android", "ios"):
        platform = "mobile"
    else:
        platform = "desktop"

    return is_real_mobile,platform


