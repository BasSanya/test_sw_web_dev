
class LocatorsLoginPage():
    #XPATH Selectors for all elements
    LOGIN_FIELD = '/html/body/div[1]/form/div[4]/table[1]/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td/div/div/div/div[2]/table/tbody/tr/td/table/tbody/tr/td[2]/input'
    PASS_FIELD = '/html/body/div[1]/form/div[4]/table[1]/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/input'
    LOGIN_BUTTON = '/html/body/div[1]/form/div[4]/table[1]/tbody/tr/td/div/div/div[2]/table/tbody/tr[3]/td/div/div/div/ul/li/a'
    LOGIN_ON_LOGGED_PAGE = '//*[@id="Vertical_CallbackPanel_SAC_Menu_DXI2_T"]/span'
    ERROR_LOGIN_TEXT = '/html/body/div/form/div[4]/table[1]/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td/div/div/div/table/tbody/tr[1]/td[2]/div[1]/span'
    ERROR_LOGIN_SUPPORT = '/html/body/div/form/div[4]/table[1]/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td/div/div/div/table/tbody/tr[1]/td[2]/div[3]/a'

class LocatorsMainPage():
    # XPATH Selectors for all elements
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