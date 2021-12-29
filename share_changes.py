#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:58:14 2021

@author: ridhingr
"""

import streamlit as st
import pandas as pd
from datetime import date
from nsetools import Nse
nse = Nse()
print (nse)
# q = nse.get_quote('sbicard')
# pprint(q['lastPrice'])


st.write("""

Daily Stock tracker

""")

my_range=range(1,800)

number=int(st.select_slider('Number of Stocks to be displayed', options=my_range,value=10))

st.write('Result for  {} stocks is displayed:'.format(number))

today = date.today()
d1 = today.strftime("%d/%m/%Y")
st.subheader('The latest info on stock on {date} is'.format(date=d1))

stock_symbols=['RELIANCE','TCS','HDFCBANK','INFY','HINDUNILVR','HDFC','ICICIBANK','KOTAKBANK','SBIN','BAJFINANCE','BHARTIARTL','ITC','HCLTECH','ASIANPAINT','WIPRO','AXISBANK','MARUTI','LT','ULTRACEMCO','DMART','ADANIGREEN','BAJAJFINSV','SUNPHARMA','ADANIPORTS','HDFCLIFE','TITAN','ONGC','HINDZINC','ADANIENT','JSWSTEEL','POWERGRID','SHREECEM','BAJAJ-AUTO','ATGL','NTPC','TATAMOTORS','ADANITRANS','M&M','DIVISLAB','TECHM','DABUR','GRASIM','BPCL','PIDILITIND','TATASTEEL','SBILIFE','BRITANNIA','SBICARD','IOC','VEDL','COALINDIA','DRREDDY','GODREJCP','BERGEPAINT','INDUSINDBK','HINDALCO','EICHERMOT','DLF','LTI','INDUSTOWER','HAVELLS','CIPLA','SIEMENS','ICICIGI','ICICIPRULI','MOTHERSUMI','INDIGO','HDFCAMC','AMBUJACEM','GAIL','TATACONSUM','HEROMOTOCO','NAUKRI','BANDHANBNK','MARICO','AUROPHARMA','BIOCON','UPL','MUTHOOTFIN','LUPIN','CHOLAFIN','CADILAHC','TORNTPHARM','COLPAL','HONAUT','APOLLOHOSP','BOSCHLTD','IDBI','PGHH','GLAND','MCDOWELL-N','NMDC','PEL','GODREJPROP','YESBANK','JUBLFOOD','PNB','AUBANK','BANKBARODA','GUJGASLTD','BAJAJHLDNG','CONCOR','SRTRANSFIN','IGL','ACC','JINDALSTEL','GICRE','MRF','HINDPETRO','MINDTREE','3MINDIA','PIIND','PAGEIND','PETRONET','ASHOKLEY','HAL','MPHASIS','VOLTAS','ALKEM','TATAPOWER','UBL','ADANIPOWER','BALKRISIND','SAIL','ASTRAL','KANSAINER','SRF','IDFCFIRSTB','BEL','TATACOMM','PFC','IRFC','ABB','DALBHARAT','MFSL','VBL','ABCAPITAL','SUNDARMFIN','WHIRLPOOL','IRCTC','LTTS','TVSMOTOR','BHARATFORG','OFSS','TRENT','IDEA','IOB','SUPREMEIND','RECLTD','CUMMINSIND','NIACL','CANBK','CROMPTON','M&MFIN','NHPC','GLAXO','IPCALAB','L&TFH','RAMCOCEM','INDIAMART','TIINDIA','AARTIIND','COROMANDEL','DEEPAKNTR','LALPATHLAB','JKCEMENT','BANKINDIA','UNIONBANK','RELAXO','SYNGENE','LICHSGFIN','EMAMILTD','DIXON','ATUL','OBEROIRLTY','NAM-INDIA','PFIZER','POLYCAB','ENDURANCE','TORNTPOWER','MAXHEALTH','ZEEL','LAURUSLABS','AIAENG','GILLETTE','TATACHEM','AAVAS','RUCHI','APLLTD','SUNTV','GODREJIND','SANOFI','BATAINDIA','COFORGE','APLAPOLLO','ESCORTS','ABFRL','SCHAEFFLER','BHEL','SUNDRMFAST','TATAELXSI','THERMAX','HATSUN','EXIDEIND','AJANTPHARM','GSPL','LINDEINDIA','FEDERALBNK','NATCOPHARM','FORTIS','KAJARIACER','MINDAIND','PERSISTENT','GMRINFRA','AMARAJABAT','SUMICHEM','JSWENERGY','VINATIORGA','APOLLOTYRE','RAJESHEXPO','AFFLE','MAHABANK','NAVINFLUOR','PHOENIXLTD','CRISIL','OIL','BLUEDART','INDHOTEL','GLENMARK','INDIANB','SUVENPHAR','MANAPPURAM','ZYDUSWELL','VAIBHAVGBL','WABCOINDIA','RBLBANK','CASTROLIND','ISEC','PRESTIGE','ALKYLAMINE','SOLARINDS','MGL','CUB','METROPOLIS','INDIGOPNTS','CHOLAHLDNG','BAJAJELEC','AMBER','SKFINDIA','TANLA','HINDCOPPER','UCOBANK','IIFLWAM','JUBLPHARMA','VGUARD','ITI','IIFL','KEC','GRINDWELL','AEGISCHEM','AKZOINDIA','CREDITACC','QUESS','PGHL','SJVN','NATIONALUM','GODREJAGRO','TTKPRESTIG','ALOKINDS','GRAPHITE','IEX','INTELLECT','ORCHPHARMA','TIMKEN','JBCHEPHARM','CARBORUNIV','SFL','CENTRALBK','CHAMBLFERT','MOTILALOFS','IBULHSGFIN','GALAXYSURF','SHRIRAMCIT','BLUESTARCO','BASF','CGPOWER','RATNAMANI','DHANI','SYMPHONY','HUDCO','KIOCL','NBCC','NH','ERIS','CANFINHOME','ROUTE','WELSPUNIND','JMFINANCIL','DBL','HAPPSTMNDS','FSL','FINPIPE','POLYMED','CESC','DCMSHRIRAM','BBTC','STLTECH','STAR','IDFC','ASAHIINDIA','ASTRAZEN','GRANULES','RADICO','VTL','EPL','PVR','REDINGTON','UTIAMC','KPRMILL','BIRLACORPN','LAXMIMACH','JCHAC','TRIDENT','CYIENT','CENTURYPLY','BSOFT','KALYANKJIL','FINEORG','NLCINDIA','ASTERDM','EQUITASBNK','CDSL','MRPL','CGCL','PNCINFRA','ORIENTELEC','PRSMJOHNSN','AARTIDRUGS','TEAMLEASE','MMTC','FLUOROCHEM','INFIBEAM','PNBHOUSING','CEATLTD','GMMPFAUDLR','SUNCLAYLTD','ZENSARTECH','MAHINDCIE','BDL','RVNL','ELGIEQUIP','KNRCON','SEQUENT','VAKRANGEE','EDELWEISS','BRIGADE','FINCABLES','EIHOTEL','POWERINDIA','RITES','SIS','TATASTLBSL','BALAMINES','HEG','AVANTIFEED','EIDPARRY','KALPATPOWR','VMART','ROSSARI','SONATSOFTW','JUSTDIAL','HEIDELBERG','GARFIBRES','UJJIVANSFB','TATAINVEST','VSTIND','BEML','CENTURYTEX','INDIACEM','SCI','JKLAKSHMI','CERA','JYOTHYLAB','VIPIND','SOLARA','TV18BRDCST','COCHINSHIP','BURGERKING','VARROC','RALLIS','ANURAS','KPITTECH','FDC','NCC','RAIN','THYROCARE','GODFRYPHLP','KEI','GPPL','GNFC','MASFIN','LXCHEM','GESHIP','PRINCEPIPE','WOCKPHARMA','HATHWAY','BALRAMCHIN','IFBIND','NAZARA','RESPONIND','KARURVYSYA','LUXIND','ENGINERSIN','DELTACORP','MAZDOCK','RCF','JSWHL','SUZLON','KRBL','MAHLOG','IRCON','SWSOLAR','SOBHA','JUBLINGREA','SUNTECK','MAHSCOOTER','RAILTEL','CSBBANK','BHARATRAS','STARCEMENT','SUPPETRO','HOMEFIRST','HEMIPROP','SPANDANA','AGCNET','INDOSTAR','ADVENZYMES','SUPRAJIT','ECLERX','BAJAJCON','IRB','NETWORK18','FACT','SPARC','NESCO','IBREALEST','TASTYBITE','TCIEXP','GULFOILLUB','WELCORP','HGS','SUDARSCHEM','MOIL','PRAJIND','TATASTLLP','TECHNOE','PAISALO','PRIVISCL','MIDHANI','SWANENERGY','ITDC','JSL','TRITURBINE','PHILIPCARB','JINDALPOLY','GSFC','KSCL','IOLCP','HFCL','DHANUKA','INOXLEISUR','BORORENEW','DCBBANK','ICRA','MTARTECH','KSB','TCNSBRANDS','CCL','MASTEK','CAPLIPOINT','ALLCARGO','CHALET','CRAFTSMAN','EQUITAS','GET&D','MAGMA','MEGH','GREAVESCOT','JSLHISAR','GAEL','LEMONTREE','MAHLIFE','NILKAMAL','SURYODAY','NOCIL','ASHOKA','MHRIL','SAREGAMA','TTML','ESABINDIA','UFLEX','SHILPAMED','ORIENTREF','POLYPLEX','JAMNAAUTO','JKTYRE','NEULANDLAB','NFL','INDOCO','ALEMBICLTD','ICIL','SHARDACROP','TATAMETALI','BSE','UJJIVAN','JKPAPER','GPIL','GUJALKALI','HERANBA','LAOPALA','RUPA','RAYMOND','MINDACORP','HCG','ANGELBRKG','JINDALSAW','KIRLOSENG','SHOPERSTOP','DEN','DEEPAKFERT','BEPL','FRETAIL','PTC','HIL','IFCI','RELIGARE','GREENLAM','SCHNEIDER','EASEMYTRIP','TATACOFFEE','JPPOWER','RAMCOIND','GDL','BALMLAWRIE','MATRIMONY','VENKEYS','UNICHEMLAB','GHCL','INGERRAND','SUVIDHAA','GRSE','HUHTAMAKI','REPCOHOME','MSTCLTD','VRLLOG','GREENPLY','JTEKTINDIA','MARKSANS','TRIVENI','ATFL','SUBROS','NEOGEN','AHLUCONT','ORIENTCEM','SUBEXLTD','JBMA','BANARISUG','NEWGEN','BECTORFOOD','TCI','OAL','ASTEC','GREENPANEL','SHIL','NIITLTD','EVEREADY','VESUVIUS','RENUKA','HGINFRA','GEPIL','BOROLTD','KIRLOSBROS','KTKBANK','SURYAROSNI','DAAWAT','MAYURUNIQ','THOMASCOOK','MAHSEAMLES','NAVNETEDUL','DFMFOODS','J&KBANK','APARINDS','SOMANYCERA','CAMLINFINE','ADFFOODS','OLECTRA','SHRIPISTON','HIKAL','GMDCLTD','ACE','PILANIINVS','HSCL','PDSMFL','KOLTEPATIL','PFOCUS','DCAL','ARVIND','DISHTV','JPASSOCIAT','TINPLATE','SAGCEM','RKFORGE','PSPPROJECT','PURVA','AMRUTANJAN','JAGRAN','INEOSSTYRO','HESTERBIO','RAMCOSYS','WELENT','ANANTRAJ','AUTOAXLES','WSTCSTPAPR','SWARAJENG','TVTODAY','SHK','DBCORP','MAITHANALL','FMGOETZE','WABAG','VSTTILLERS','INOXWIND','DALMIASUG','JAICORPLTD','SARDAEN','TIDEWATER','LUMAXIND','SOUTHBANK','CHEMCON','STOVEKRAFT','CHENNPETRO','GABRIEL','ORISSAMINE','TEJASNET','FILATEX','JKIL','BOMDYEING','MOREPENLAB','HMT','HIMATSEIDE','IIFLSEC','KIRIINDUS','NUCLEUS','KSL','DIAMONDYD','SOTL','ARVINDFASN','CAPACITE','TIMETECHNO','HERITGFOOD','RSYSTEMS','TVSSRICHAK','SAFARI','ASHIANA','GTPL','ITDCEM','SASKEN','DOLLAR','APOLLOPIPE','INDIAGLYCO','GANECOS','HINDOILEXP','ACCELYA','PRAKASH','IGPL','PCJEWELLER','JMCPROJECT','RTNPOWER','GATI','OMAXE','GENUSPOWER','SANDHAR','PSB','JSWISPL','NBVENTURES','CONFIPET','IMFA','RPOWER','HCC','DHAMPURSUG','CARERATING','3IINFOTECH','KIRLOSIND','GEOJITFSL','QUICKHEAL','MMFL','FCONSUMER','MTNL','CENTRUM','MUKANDLTD','SHARDAMOTR','PFS','DIGISPICE','SUNDARMHLD','GIPCL','DPSCLTD','IFGLEXPOR','SUNFLAG','COSMOFILMS','ASTRAMICRO','NXTDIGITAL','SEAMECLTD','VOLTAMP','LUMAXTECH','BODALCHEM','PANACEABIO','MOLDTKPAC','SSWL','WHEELS','SHALBY','WONDERLA','JETAIRWAYS','ELECTCAST','GOCLCORP','KCP','PUNJABCHEM','SADBHAV','KKCL','SANGHIIND','YAARII','VIDHIING','EXCELINDUS','NRBBEARING','SMSPHARMA','OPTIEMUS','DREDGECORP','BFINVEST','MANINFRA','GALLISPAT','SESHAPAPER','MANALIPETC','BLISSGVS','TNPL','USHAMART','INDORAMA','BANCOINDIA','KESORAMIND','GTLINFRA','HSIL','BUTTERFLY','FLFL','INSECTICID','SHANTIGEAR','FAIRCHEMOR','ESTER','VINDHYATEL','HONDAPOWER','JINDWORLD','TIIL','LGBBROSLTD','SHAKTIPUMP','BLS','SHANKARA','PRABHAT','APCOTEXIND','BFUTILITIE','HBLPOWER','RELINFRA','ONMOBILE','OCCL','GLOBUSSPR','JISLJALEQS','ASHAPURMIN','SUVEN','RPSGVENT','TEXINFRA','GUFICBIO','PARAGMILK','CIGNITITEC','SHREDIGCEM','EKC','PANAMAPET','TIRUMALCHM','SIYSIL','ANDHRAPAP','PNBGILTS','ARSHIYA','SIRCA','POWERMECH','CLNINDIA','IGARASHI','TARC','MANGCHEFER','PRICOLLTD','IMPAL','RANEHOLDIN','SHAREINDIA','MPSLTD','INDNIPPON','INDIANHUME','MAXVIL','ACRYSIL','POKARNA','SATIA','RADIOCITY','MARINE','SRIPIPES','THANGAMAYL','GFLLIMITED','RAJRATAN','PGEL','ANDHRSUGAR','VISAKAIND','SMCGLOBAL','NCLIND','GMBREW','ASALCBR','APTECHT','GOLDIAM','EMAMIPAP','MANGLMCEM','KARDA','NACLIND','SNOWMAN','FIEMIND','GNA','FOSECOIND','FCL','XCHANGING','TEXRAIL','EIHAHOTELS','ELECON','KINGFA','AARTISURF','RTNINFRA','STERTOOLS','BAJAJHIND','TTKHLTCARE','KELLTONTEC','ENIL','SADBHIN','BHAGERIA','KICL','AVTNPL','TAJGVK','AWHCL','DCW','DATAMATICS','JAYNECOIND','TAKE','KITEX','SMLISUZU','APEX','VADILALIND','SUTLEJTEX','RPGLIFE','5PAISA','SPENCERS','BBL','WENDT','LIKHITHA','CEREBRAINT','GICHSGFIN','SKIPPER','GRAVITA','RBL','CANTABIL','ZENTEC','TIPSINDLTD','MUTHOOTCAP','NURECA','DYNAMATECH','PLASTIBLEN','SPIC','UNIENTER','DYNPRO','ALICON','KUANTUM','DBREALTY','SUMMITSEC','ANUP','DECCANCE','DWARKESH','BALAJITELE','HARITASEAT','NATHBIOGEN','KABRAEXTRU','VSSL','VHL','NELCAST','MUNJALSHOW','RGL','CENTENKA','KOKUYOCMLN','RIIL','MIRZAINT','PATELENG','NSIL','EXPLEOSOL','MUNJALAU','RAMKY','APCL','UNIDT','TWL','GAYAPROJ','EBIXFOREX','SHALPAINTS','BALAXI','ORIENTPPR','ARMANFIN','RML','AMBIKCO','SALASAR','TFCILTD','JAYBARMARU','INDRAMEDCO','DHFL','SANDESH','CENTUM','SUULD','HTMEDIA','ALLSEC','NBIFIN','RICOAUTO','STEELXIND','THEINVEST','RCOM','MONTECARLO','NAVKARCORP','BINDALAGRO','TDPOWERSYS','MANINDS','KOPRAN','NITINSPIN','LINCOLN','EVERESTIND','PRECWIRE','SATIN','STCINDIA','ASIANTILES','VISHWARAJ','HMVL','RSWM','TNPETRO','UNIVCABLES','SANGHVIMOV','SORILINFRA','HITECH','GULPOLY','UNITECH','NELCO','V2RETAIL','INDSWFTLAB','REPRO','SHREEPUSHK','BCG','AJMERA','NECLIFE','BLKASHYAP','RUSHIL','TBZ','THEJO','HEXATRADEX','JAYAGROGN','ADORWELD','PILITA','MADRASFERT','ORIENTHOT','TCPLPACK','SRHHYPOLTD','JAIBALAJI','NRAIL','KANORICHEM','MAHEPC','CONTROLPR','SPAL','ATULAUTO','HINDCOMPOS','SHRIRAMEPC','KAYA','ROSSELLIND','ZUARI','ASAHISONG','IFBAGRO','SAKSOFT','PRECAM','NAGAFERT','NAHARSPING','KAMDHENU','DHANBANK','DLINKINDIA','PARSVNATH','SCHAND','PGIL','AVADHSUGAR','SASTASUNDR','TI','NDTV','HLVLTD','FEL']

df=pd.DataFrame(columns=['Company_Name','Tickr','LTP','Prev Closing Price','Absolute change','% Change'])
arr=[]
for i in range(0,number):
    
    try:
        q=nse.get_quote(stock_symbols[i])
        arr.append([q['companyName'],stock_symbols[i],q['lastPrice'],q['previousClose'],q['change'],q['pChange']])
    except Exception as e:
        print(e)
        
df=pd.DataFrame(arr,columns=['Company_Name','Tickr','LTP','Prev Closing Price','Absolute change','% Change'])
df['Absolute change'] = df['Absolute change'].astype(float)
df['% Change']=df['% Change'].astype(float)



df.index=df.index+1

st.table(df.style.set_precision(2))
   
    

# exchange="BSE"
# stock_symbol="SBICARD"

# url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SBICARD.NSE&interval=5min&apikey=NC8MB7116HC50NQ"
# url2="http://localhost:3000/nse/get_quote_info?companyName={}".format(stock_symbol)
# r = requests.get(url2)
# print(url2)
# data = r.json()
# print(data)
# print([i for i in data['Time Series (5min)'].keys()])



# url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}.{}&outputsize=full&apikey=NC8MB7116HC50NQ".format(stock_symbol,exchange)
# r = requests.get(url)
# data = r.json()
# ###`print(data)



# ###arr=[i for i in data]
# ###print(arr)
# print(data['Time Series (Daily)']['2021-12-24'])



