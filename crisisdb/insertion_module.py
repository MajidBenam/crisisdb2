# let's create a magic dictionary as discussed above:

# helping dics:
MYDECIMAL = {'model_type': 'DecimalField', 'widget_type': 'NumberInput', }
MYINT = {'model_type': 'IntegerField', 'widget_type': 'NumberInput', }
MYSELECT = {'model_type': 'CharField', 'widget_type': 'Select', }
MYFOREIGNSELECT = {'model_type': 'ForeignKey', 'widget_type': 'Select', }
MYFOREIGNSELECTMULTIPLE = {
    'model_type': 'ForeignKey', 'widget_type': 'Select', }
MYCHAR = {'model_type': 'CharField', 'widget_type': 'TextInput', }
# not forms.Textarea !!
MYTEXT = {'model_type': 'TextField', 'widget_type': 'Textarea', }

# repeated key_value pairs (to be gladly_overwritten using the technique above):
REPEATED_DICS = {
    'polity': MYFOREIGNSELECT,
    'section': MYFOREIGNSELECT,
    'subsection': MYFOREIGNSELECT,
    'citations': MYFOREIGNSELECTMULTIPLE,
    'year_from': MYINT,
    'year_to': MYINT,
    'description': MYTEXT,
    'tag': MYSELECT,
    # everythin will have: created_date and modified_date
}

# maybe a general name for __str__(self):
# something like:
# return "%s for %s from %s" % (self.full_var_name, self.polity, self.predecessor, self.year_from to self.year_to)

# main magic dic
magic_dic = {
    'Wages': {
        'file_name': 'Qing - Datasets.xls',
        'sheet_name': 'Qing Wages',
        'full_var_name': 'Wages',
        'polity': 'CnQingL',
        # 'section': everything has that and it s the smae everywhere
        # 'subsection': everything has that
        'general_description': "AVAILABLE IN THE FILE",
        'wages': MYDECIMAL,
        # 'year_from' everything has that and it s the smae everywhere
        # 'year_to' everything has that
        'citation': 'de Zwart, Van Leeuwen and van Leeuwen-Li 2015',
        'data_source': ['https://clio-infra.eu/Indicators/LabourersRealWage.html', ],
    },

    'FamineOutbreak': {
        'file_name': 'Qing - Datasets.xls',
        'sheet_name': 'Qing Famine',
        'full_var_name': 'Famine Outbreak',
        'polity': 'CnQingE',
        'general_description': "UNAVAILABLE IN THE FILE",
        'longitude': MYDECIMAL,
        'latitude': MYDECIMAL,
        'elevation': MYDECIMAL,
        'event': MYINT,
        'main_category': 35,
        'sub_category': MYSELECT,
        'magnitude': MYSELECT,
        'duration': MYSELECT,
        'data_source': ['https://clio-infra.eu/Indicators/LabourersRealWage.html', ],
    },

    'DiseaseOutbreak': {
        'file_name': 'Qing - Datasets.xls',
        'sheet_name': 'Qing Disease',
        'full_var_name': 'Disease Outbreak',
        'polity': 'CnQingE',
        'general_description': "UNAVAILABLE IN THE FILE",
        'longitude': MYDECIMAL,
        'latitude': MYDECIMAL,
        'elevation': MYDECIMAL,
        'event': MYINT,
        'main_category': 34,
        'sub_category': MYSELECT,
        'magnitude': MYSELECT,
        'duration': MYSELECT,
        'data_source': ['https://clio-infra.eu/Indicators/LabourersRealWage.html', ],
    },

    'Conflict': {
        'file_name': 'Qing - Datasets.xls',
        'sheet_name': 'Qing Conflicts - COW',
        'full_var_name': 'Conflict',
        'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",
        'war_num': MYINT,
        'war_name': MYCHAR,
        'war_type': MYSELECT,
        'side': MYSELECT,
        'ccode': 710,
        # start days and months, not of interest at the moment
        'deaths': MYINT,
        'deaths_per_side': MYINT,
        'total_combat_deaths': MYINT,
    },

    'IncomeInequality': {
        'file_name': 'China_IncomeInequality_TerritorialRef_1949_2012_CCode_156.xls',
        'sheet_name': 'Data',
        'full_var_name': 'Income Inequality',
        'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",
        'inequality_value': MYDECIMAL,
        'citation': 'Moatsos, Michalis, Jan Luiten van Zanden, Joerg Baten, et al. (2015). Income Inequality. http://hdl.handle.net/10622/6OHMDS, accessed via the Clio Infra website.',
        'data_source': ['https://www.clio-infra.eu/IndicatorsPerCountry/China_IncomeInequality_TerritorialRef_1949_2012_CCode_156.xlsx', ],
    },

    'LabourersRealWage': {
        'file_name': 'China_LabourersRealWage_TerritorialRef_1949_2012_CCode_156.xls',
        'sheet_name': 'Data',
        'full_var_name': 'Labourers Real Wage',
        'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",
        'labourors_real_wage_value': MYDECIMAL,
        'citation': 'Zwart, Pim de, Bas van Leeuwen and Jieli van Leeuwen-Li (2015). Labourers Real Wage. http://hdl.handle.net/10622/QK8VRF, accessed via the Clio Infra website.',
        'data_source': ['https://www.clio-infra.eu/IndicatorsPerCountry/China_LabourersRealWage_TerritorialRef_1949_2012_CCode_156.xlsx', ],

    },

    'PriceTrend': {
        'file_name': 'Document 3 Price Trends, Climate Cycles, and Harvest Conditions in the Yangzi Delta, 1653_1920.xls',
        'sheet_name': 'Sheet1',
        'full_var_name': 'Price Trend',
        # 'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",
        'price_trend': MYSELECT,
        'citation': 'Thomas, G. Rawski; Lillian M. Li. 1992. Chinese History in Economic Perspective. University of California Press.',

    },

    'ClimateCycle': {
        'file_name': 'Document 3 Price Trends, Climate Cycles, and Harvest Conditions in the Yangzi Delta, 1653_1920.xls',
        'sheet_name': 'Sheet2',
        'full_var_name': 'Climate Cycle',
        # 'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",
        'climate_cycle': MYSELECT,
        'citation': 'Thomas, G. Rawski; Lillian M. Li. 1992. Chinese History in Economic Perspective. University of California Press.',

    },

    'HarvestCondition': {
        'file_name': 'Document 3 Price Trends, Climate Cycles, and Harvest Conditions in the Yangzi Delta, 1653_1920.xls',
        'sheet_name': 'Sheet3',
        'full_var_name': 'Harvest Condition',
        # 'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",
        'number_of_normal_harvests': MYINT,
        'number_of_good_harvests': MYINT,
        'number_of_deficient_harvests':	MYINT,
        'average_deviation_of_harvests': MYINT,
        'citation': 'Thomas, G. Rawski; Lillian M. Li. 1992. Chinese History in Economic Perspective. University of California Press.',

    },


    'PercentageOfPurchasedDegrees': {
        'file_name': 'Document 4 percentage of purchased degrees.xls',
        'sheet_name': 'Sheet1',
        'full_var_name': 'Percentage Of Purchased Degrees',
        # 'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",
        'number_of_officials': MYINT,
        'examination': MYDECIMAL,  # percent_sign
        'yin_privilege_parantheses_hereditary_parantheses':	MYDECIMAL,  # percent_sign
        'purchase': MYDECIMAL,  # percent_sign
        'other': MYDECIMAL,  # percent_sign
        'citation': 'Ho, Ping-ti. 1962. The ladder of success in imperial China. Columbia University Press. ',
    },


    'TaxBurdenPerCapita': {
        'file_name': 'Tax burdens (per capita).xls',
        'sheet_name': 'Sheet1',
        'full_var_name': 'Tax Burdens (per Capita)',
        # 'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",
        'tax_type': MYSELECT,
        'revenue_parantheses_1000_taels_parantheses':	MYDECIMAL,
        'percent_of_total': MYDECIMAL,  # percent_sign
        'per_capita_parantheses_taels_parantheses': MYDECIMAL,
        'citation': 'Wang, Yeh-chien. 1973. Land Taxation in Imperial China, 1750-1911. Cambridge, MA: Harvard University Press.',
    },


    'PowerTransition': {
        'file_name': 'Document 1 Qing power transitions.xls',
        'sheet_name': 'Sheet1',
        'full_var_name': 'PowerTransition',
        # 'polity': 'CnQingL',
        'general_description': "UNAVAILABLE IN THE FILE",

        'conflict_name': MYCHAR,
        'ruler_name': MYCHAR,
        'reign_number': MYINT,
        'overturn': MYSELECT,
        'assassination': MYSELECT,
        'intra_elite': MYSELECT,
        'military_revolt': MYSELECT,
        'popular_uprising': MYSELECT,
        'separatist_rebellion': MYSELECT,
        'external_invasion': MYSELECT,
        'external_interference': MYSELECT,
        # 'overthrow': MYSELECT,
        'citation': 'John E Morby. 2018. Dynasties of the World. A Chronological and Genealogical Handbook. Oxford University Press. Oxford.',
    },


    'PopulationTrend': {
        'file_name': 'Document 2 Trends of Population, Silver Stocks, and Rice Prices in China, 1650_1930.xls',
        'sheet_name': 'Sheet1',
        'full_var_name': 'Power Transition',
        # 'polity': 'CnQingL',
        'general_description': "AVAILABLE IN THE FILE",
        'population_parantheses_tot_millions_parantheses': MYINT,
        'population_growth': MYINT,  # percent_sign
        'citation': 'Thomas, G. Rawski; Lillian M. Li. 1992. Chinese History in Economic Perspective. University of California Press.',
    },

    'SilverStock': {
        'file_name': 'Document 2 Trends of Population, Silver Stocks, and Rice Prices in China, 1650–1930.xls',
        'sheet_name': 'Sheet2',
        'full_var_name': 'Silver Stock',
        # 'polity': 'CnQingL',
        'general_description': "AVAILABLE IN THE FILE",

        'silver_stocks_parantheses_total_in_millions_of_silver_yuan_parantheses_lower_limit': MYINT,
        'silver_stocks_parantheses_total_in_millions_of_silver_yuan_parantheses_higher_limit': MYINT,
        'silver_stocks_parantheses_annual_growth_parantheses': MYDECIMAL,  # percent_sign
        'citation': 'Thomas, G. Rawski; Lillian M. Li. 1992. Chinese History in Economic Perspective. University of California Press.',
    },


    'RicePrice': {
        'file_name': 'Document 2 Trends of Population, Silver Stocks, and Rice Prices in China, 1650–1930.xls',
        'sheet_name': 'Sheet3',
        'full_var_name': 'Rice Price',
        # 'polity': 'CnQingL',
        'general_description': "AVAILABLE IN THE FILE",
        'rice_prices_paranteses_tael_per_shi_parantheses': MYCHAR,
        'rice_price_parantheses_annual_change_parantheses': MYDECIMAL,  # percent_sign
        'citation': 'Thomas, G. Rawski; Lillian M. Li. 1992. Chinese History in Economic Perspective. University of California Press.',
    },

    'ShipNumber': {
        'file_name': 'Document 5 Number of Ships from the Chinese Mainland Arriving in Nagasaki.xls',
        'sheet_name': 'Sheet1',
        'full_var_name': 'Ship Number',
        'polity': 'CnQingE',
        'general_description': "UNAVAILABLE IN THE FILE",
        'number_of_ships_from_mainland': MYINT,
        'additional_ships_from_unknown_ports': MYINT,
        'citation': 'Atwell, William S. “Some observations on the “Seventeenth-century crisis” in China and Japan.” The Journal of Asian Studies 45, no. 2 (1986): 223-244',
    },


    'SilverImport': {
        'file_name': 'Document 4 Estimated Imports of Silver into China, I60i_I700.xls',
        'sheet_name': 'Sheet1',
        'full_var_name': 'Silver Import',
        'polity': 'CnQingE',
        'general_description': "UNAVAILABLE IN THE FILE",
        'year_range': MYINT,  # year_range
        'japan_import_parantheses_metric_tons_parantheses': MYDECIMAL,
        'philippines_import_parantheses_metric_tons_parantheses': MYDECIMAL,
        'indian_ocean_import_parantheses_metric_tons_parantheses': MYDECIMAL,
        'total_import_parantheses_metric_tons_parantheses': MYDECIMAL,
        'citation': 'Richard von Glahn. Fountain of Fortune: Money and Monetary Policy in China, 1000-1700, p. 232',
    },


    'AgriculturalProductionAndPopulation': {
        'file_name': 'agricultural production.xls',
        'sheet_name': 'Sheet3',
        'full_var_name': 'Agricultural Production and Population',
        # 'polity': 'CnQingE',
        'general_description': "UNAVAILABLE IN THE FILE",
        'total_population': MYINT,
        'arable_land_per_capita_parantheses_mu_parantheses': MYDECIMAL,
        'citation': 'Li, Huaiyin. The Making of the Modern Chinese State: 1600-1950. New York: Routledge.',
    },

    'AgriculturalProductioPerPopulation': {
        'file_name': 'agricultural production.xls',
        'sheet_name': 'Sheet2',
        'full_var_name': 'Agricultural Production per Population',
        # 'polity': 'CnQingE',
        'general_description': "UNAVAILABLE IN THE FILE",

        'total_population_parantheses_1000_parantheses': MYINT,
        'agricultural_population_parantheses_1000_parantheses': MYINT,
        'arable_land_parantheses_1000_mu_parantheses': MYINT,
        'arable_land_per_farmer_parantheses_mu_parantheses': MYDECIMAL,
        'gross_grain_shared_per_agricultural_population_parantheses_catties_per_capita_parantheses': MYINT,
        'net_grain_shared_per_agricultural_population_parantheses_catties_per_capita_parantheses': MYINT,
        'surplus': MYINT,

        'citation': 'Li, Huaiyin. The Making of the Modern Chinese State: 1600-1950. New York: Routledge.',
    },


    'AgriculturalProductivity': {
        'file_name': 'agricultural production.xls',
        'sheet_name': 'Sheet1',
        'full_var_name': 'Agricultural Productivity',
        # 'polity': 'CnQingE',
        'general_description': "UNAVAILABLE IN THE FILE",
        'total_amount_of_grain_yield_parantheses_in_1000_catties_parantheses': MYINT,
        'total_size_of_grain_land_parantheses_1000_mu_parantheses': MYINT,
        'grain_yield_per_mu': MYINT,
        'total_number_of_farmers_parantheses_1000_parantheses': MYINT,
        'grain_yield_per_farmer_parantheses_catty_parantheses': MYINT,
        'grain_number_per_farmer_parantheses_number_of_mouths_fed_parantheses': MYINT,
        'citation': 'Li, Huaiyin. The Making of the Modern Chinese State: 1600-1950. New York: Routledge.',
        'general_note': '1 catty = 1.1 pounds',
    },



























}
