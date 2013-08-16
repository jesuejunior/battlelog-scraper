from core.action.extractor import _extract
from core.action.stats import updater, create

__author__ = 'jesuejunior'

from splinter import Browser
from lxml import etree

profile_player_xpath = {

            #Stats de classes
            'level' : "//div[@class='profile-venicestats-overview-highlight-rank-info profile-venicestats-overview-highlight-bottom']/h1[@class='profile-venicestats-overview-highlight-stat-title']",
            'score_assault' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tbody/tr[1]/td[2]/div[@class='profile-venicestats-overview-table-cell-border']",
            'score_engineer' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tbody/tr[2]/td[2]/div[@class='profile-venicestats-overview-table-cell-border']",
            'score_support' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tbody/tr[3]/td[2]/div[@class='profile-venicestats-overview-table-cell-border']",
            'score_recon' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tbody/tr[4]/td[2]/div[@class='profile-venicestats-overview-table-cell-border']",
            'score_vehicles' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tbody/tr[5]/td[2]/div[@class='profile-venicestats-overview-table-cell-border']",
            'score_combat' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tbody/tr[6]/td[2]/div[@class='profile-venicestats-overview-table-cell-border']",
            'score_award' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tbody/tr[7]/td[2]/div[@class='profile-venicestats-overview-table-cell-border']",
            'score_unlocks' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tbody/tr[8]/td[2]/div[@class='profile-venicestats-overview-table-cell-border']",
            'score_total' : "//table[@class='profile-venicestats-overview-boxnarrowclean-table nocompare']/tfoot/tr/td[2]/div[@class='profile-venicestats-overview-table-cell-border profile-venicestats-overview-total-score']",

            #Primeira coluna stats
            'kills' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[1]/td[2]",
            'deaths' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[2]/td[2]",
            'kd_ratio' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[3]/td[2]",
            'kill_assists' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[4]/td[2]",
            'score_min' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[5]/td[2]",
            'quits' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[6]/td[2]",
            'mcom_defend_kills' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[7]/td[2]",
            'mcom_destroyed' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[8]/td[2]",
            'flags_captured_conquest' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[9]/td[2]",
            'flags_defended_conquest' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][1]/tbody/tr[10]/td[2]",
            #Prmeira coluna acaba aqui
            'vehicles_destroyed' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[1]/td[2]",
            'vehicles_destroyed_assists' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[2]/td[2]",
            'avg_weapon_accuracy' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[3]/td[2]",
            'longest_headshot' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[4]/td[2]",
            'highest_kill_streak' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[5]/td[2]",
            'skill' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[6]/td[2]",
            'avenger_kills' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[7]/td[2]",
            'savior_kills' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[8]/td[2]",
            'dogtags_taken' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[9]/td[2]",
            'flags_captured_ctf' : "//table[@class='profile-venicestats-overview-boxwideclean-table'][2]/tbody/tr[10]/td[2]",
            #segunda coluna acaba aqui
            'squad_score_bonus' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[1]/td[2]",
            'repairs' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[2]/td[2]",
            'revives' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[3]/td[2]",
            'heals' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[4]/td[2]",
            'resupplies' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[5]/td[2]",
            'shots_fired' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[6]/td[2]",
            'highest_nemesis_streak' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[7]/td[2]",
            'nemesis_kills' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[8]/td[2]",
            'suppression_assists' : "//table[@class='profile-venicestats-overview-boxwideclean-table last']/tbody/tr[9]/td[2]",
        }



user = {'username' : 'bombaCM',
        'url_stats' : 'http://battlelog.battlefield.com/bf3/soldier/bombaCM/stats/370974436/ps3/',
        'url_weapons' :  'http://battlelog.battlefield.com/bf3/soldier/bombaCM/weapons/370974436/ps3/',
        'url_vehicles' :  'http://battlelog.battlefield.com/bf3/soldier/bombaCM/vehicles/370974436/ps3/',
        }


user_old = {'username' : 'Juninn3k6',
        'url_stats' : 'http://battlelog.battlefield.com/bf3/soldier/Juninn3k6/stats/327539077/ps3/',
        'url_weapons' :  'http://battlelog.battlefield.com/bf3/soldier/Juninn3k6/weapons/327539077/ps3/',
        'url_vehicles' :  'http://battlelog.battlefield.com/bf3/soldier/Juninn3k6/vehicles/327539077/ps3/',
        }

create(user)

html = ""

parser = etree.HTMLParser(remove_comments=True, encoding='utf-8')

def catch_metadata(xpath, tree):
    go_return = None

    elements = tree.xpath(xpath)
    for el in elements:
        for text in el.itertext(with_tail=True):
            clean_text = str(text)
            if clean_text:
                go_return = clean_text

    return go_return

with Browser() as browser:
     # Visit URL
     browser.visit(user['url_profile'])

     # Pagina pronta
     html = browser.html

tree = etree.fromstring(html, parser)

profile = {}
profile['username'] = user['username']

for key,value in profile_player_xpath.iteritems():
     profile[key] = _extract(catch_metadata(value, tree))

updater(profile)

print "profile atualizado com sucesso."