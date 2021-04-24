class LocatorsLoginPage():
    # XPATH Selectors for all elements
    LOGIN_FIELD = '/html/body/div[1]/form/div[4]/table[1]/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td/div/div/div/div[2]/table/tbody/tr/td/table/tbody/tr/td[2]/input'
    PASS_FIELD = '/html/body/div[1]/form/div[4]/table[1]/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/input'
    LOGIN_BUTTON = '/html/body/div[1]/form/div[4]/table[1]/tbody/tr/td/div/div/div[2]/table/tbody/tr[3]/td/div/div/div/ul/li/a'
    LOGIN_ON_LOGGED_PAGE = '//*[@id="Vertical_CallbackPanel_SAC_Menu_DXI2_T"]/span'
    ERROR_ENTERED_MESSAGE = '//td[@class="ErrorLabel"]'


class LocatorsMainPage():
    # MP - Main page
    MP_USERS = '//*[@id="Vertical_NC_NB_GHC0"]/span'
    MP_OTHER_CATALOGS = '//*[@id="Vertical_NC_NB_GHC1"]/span'
    MP_SALES_STUCTURE = '//*[@id="Vertical_NC_NB_GHC2"]/span'
    MP_OUTLETS = '//*[@id="Vertical_NC_NB_GHC3"]/span'
    MP_PRODUCTS = '//*[@id="Vertical_NC_NB_GHC4"]/span'
    MP_DOCUMENTS = '//*[@id="Vertical_NC_NB_GHC5"]/span'
    MP_PLAN_AND_ANALYSE = '//*[@id="Vertical_NC_NB_GHC6"]/span'
    MP_REPORTS = '//*[@id="Vertical_NC_NB_GHC7"]/span'
    MP_REPORTS_ID = 'Vertical_NC_NB_GHC7'
    MP_DATA_EXCHANGE = '//*[@id="Vertical_NC_NB_GHC8"]/span'

    # Help block
    HP_BUTTON = '//*[@id="Vertical_CallbackPanel_SAC_Menu_DXI1_T"]'
    HP_MESSAGE = '//*[@id="UserGuideMessage"]/span/p'
    HP_LINK = '//*[@id="UserGuideMessage"]/span/a'

    # Users dir in side menu
    US_DROP_MENU_USERS = '//*[@id="Vertical_NC_NB_GHC0"]/img[1]'
    US_DROP_MENU_SUB_USERS = '//*[@id="Vertical_NC_NB_ITC0i0_TL_CD"]/ul/li[1]/span/img'
    US_USERS_SUBDIR = '//*[@id="Vertical_NC_NB_ITC0i0_TL_N0"]/span'
    US_USERS_TYPE = '//*[@id="Vertical_NC_NB_ITC0i0_TL_N0_0"]/span'
    US_MM_USERS = '//*[@id="Vertical_NC_NB_ITC0i0_TL_N0_1"]/span'
    US_MM_USERS_PROFILES = '//*[@id="Vertical_NC_NB_ITC0i0_TL_N0_2"]/span'
    US_ABOUT_USER = '//*[@id="Vertical_NC_NB_ITC0i0_TL_N0_3"]/span'
    US_LOGIN_TYPES = '//*[@id="Vertical_NC_NB_ITC0i0_TL_N1"]/span'
    US_CLOSE_SUB_MENU = '//*[@id="Vertical_NC_NB_ITC0i0_TL_CD"]/ul/li[1]/span/img'
    US_CLOSE_MENU = '//*[@id="Vertical_NC_NB_GHE0"]/img[1]'

    # Other catalogs in side menu
    OT_OPEN_DROP_MENU_BTN = '//*[@id="Vertical_NC_NB_GHC1"]/img[1]'
    OT_CLOSE_DROP_MENU_BTN = '//*[@id="Vertical_NC_NB_GHE1"]/img[1]'
