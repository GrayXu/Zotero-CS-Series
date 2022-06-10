from pyzotero import zotero
import re
from tqdm import tqdm

library_id = '...'     # like 1234567
library_type = 'user'  
api_key = '...'        # like aaaaaaaaaaaaaaaaaaaaaaaa

zot = zotero.Zotero(library_id, library_type, api_key)

zot.key_info()

mapping = {
    "Transactions on Storage": "TOS",
    'Transactions on Knowledge and Data Engineering': 'TKDE',
    'Transactions on Parallel and Distributed Systems': 'TPDS',
    'Transactions on Computer-Aided Design of Integrated Circuits and Systems':'TCAD',
    'Transactions on Information Theory':'TIT',
    'Transactions on Computers':'TC',
    'Journal of Computer Science and Technology': 'JCST',
    "VLDB Journal" : 'VLDBJ',
    'VLDB Endowment' : "VLDB",
    'IEEE Access': 'Access',
    'Future Generation Computer Systems': 'FGCS',
    '计算机研究与发展':'计研发',
    'SOCC':'SoCC',
    
    # auto gen
    # ...
}

'''
auto gen mapping
'''
cont = "EuroSys,FAST,ATC,HPCA,ISCA,DAC,ICPP,ICCD,OSDI,SOSP,ASPLOS,SC,NSDI,CoNEXT,INFOCOM,ICDEW,MASCOTS,ICDCS,IPDPS,HotStorage,SIGMOD,MSST,ICCAD,CIDR,HotCloud,DSN,NAS,MICRO,SoCC,CLOUD,SYSTOR,SIGCOMM,MEMSYS,VLSI,DATE,ICDE,HiPC,ICOIN,IWQoS,NVMSA,ISPASS,APSys,PPoPP,ICS,HPDC,HPCAsia"
for c in cont.split(','):
    mapping[c] = c
    print("'%s' : '%s'," % (c,c))

reg = '\d{4}'
def getYear(date):
    if date == '':
        return None
    pattern = re.compile(reg)
    result = pattern.search(date)
    if result is not None:
        return result.group(0)
    else:
        return None
    
every_items = zot.everything(zot.top())

all_conf_set = set([])
exceptions = []
bad_target = []
for item in every_items:
    data = item['data']
    
    if 'series' not in data.keys():
        exceptions.append(data)
        continue
        
    if data['series'] == '':
        target = ''
        if 'conferenceName' in data.keys() and data['conferenceName'] is not '':
            target = data['conferenceName']
        elif 'proceedingsTitle' in data.keys() and data['proceedingsTitle'] is not '':
            target = data['proceedingsTitle']
        elif 'publicationTitle' in data.keys() and data['publicationTitle'] is not '':
            target = data['publicationTitle']
        else:
            exceptions.append(data)
            continue
            
        abbr = ''
        
        for key in mapping.keys():
            if key in target:
                abbr = mapping[key]
                break
        if abbr == '':
            bad_target.append(targer)
            exceptions.append(data)
            continue
        
        year = getYear(data['date'])
        if year is not None:
            abbr += ' \''+year[-2:]
        
        data['series'] = abbr
        zot.update_item(item)
        
print('num of exceptions: ' + len(exceptions))

print('pub names w/o abbrs:')
print(bad_target)