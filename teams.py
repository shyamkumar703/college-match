""" Personal Project """
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from bs4 import BeautifulSoup
import requests
division_one_links = []
d1_list = ['ABILENE CHRISTIAN', 'AIR FORCE', 'AKRON', 'ALABAMA', 'ALABAMA A&M', 'ALABAMA STATE', 'ALBANY', 'ALCORN STATE', 'AMERICAN', 'APPALACHIAN STATE', 'ARIZONA', 'ARIZONA STATE', 'ARKANSAS', 'ARKANSAS STATE', 'ARKANSAS-LITTLE ROCK', 'ARKANSAS-PINE BLUFF', 'ARMY WEST POINT', 'AUBURN', 'AUSTIN PEAY', 'BYU', 'BALL STATE', 'BAYLOR', 'BELMONT', 'BETHUNE-COOKMAN', 'BINGHAMTON', 'BOISE STATE', 'BOSTON COLLEGE', 'BOSTON U.', 'BOWLING GREEN', 'BRADLEY', 'BROWN', 'BRYANT', 'BUCKNELL', 'BUFFALO', 'BUTLER', 'CSU BAKERSFIELD', 'CAL BAPTIST', 'CAL POLY', 'CAL ST. FULLERTON', 'CAL ST. NORTHRIDGE', 'CALIFORNIA', 'CAMPBELL', 'CANISIUS', 'CENTRAL ARKANSAS', 'CENTRAL CONNECTICUT', 'CENTRAL MICHIGAN', 'CHARLESTON SOUTHERN', 'CHARLOTTE', 'CHATTANOOGA', 'CHICAGO STATE', 'CINCINNATI', 'CITADEL', 'CLEMSON', 'CLEVELAND ST.', 'COASTAL CAROLINA', 'COL. OF CHARLESTON', 'COLGATE', 'COLORADO', 'COLORADOST.', 'COLUMBIA', 'CONNECTICUT', 'COPPIN STATE', 'CORNELL', 'CREIGHTON', 'DARTMOUTH', 'DAVIDSON', 'DAYTON', 'DEPAUL', 'DELAWARE', 'DELAWARE STATE', 'DENVER', 'DETROIT MERCY', 'DRAKE', 'DUKE', 'DUQUESNE', 'EAST CAROLINA', 'EAST TENN. ST.', 'EASTERN ILLINOIS', 'EASTERN KENTUCKY', 'EASTERN MICHIGAN', 'EASTERN WASHINGTON', 'ELON', 'EVANSVILLE', 'FIU', 'FAIRFIELD', 'FAIRLEIGH DICKINSON', 'FLORIDA', 'FLORIDA A&M', 'FLORIDA ATLANTIC', 'FLORIDA GULF COAST', 'FLORIDA STATE', 'FORDHAM', 'FRESNO STATE', 'FURMAN', 'GARDNER-WEBB', 'GEORGE MASON', 'GEORGE WASHINGTON', 'GEORGETOWN', 'GEORGIA', 'GEORGIA SOUTHERN', 'GEORGIA STATE', 'GEORGIA TECH', 'GONZAGA', 'GRAMBLING', 'GRAND CANYON', 'HAMPTON', 'HARTFORD', 'HARVARD', 'HAWAII', 'HIGH POINT', 'HOFSTRA', 'HOLY CROSS', 'HOUSTON', 'HOUSTON BAPTIST', 'HOWARD', 'IUPUI', 'IDAHO', 'IDAHO STATE', 'ILLINOIS', 'ILLINOIS STATE', 'ILLINOIS-CHICAGO', 'INCARNATE WORD', 'INDIANA', 'INDIANA STATE', 'IONA', 'IOWA', 'IOWA STATE', 'JACKSON STATE', 'JACKSONVILLE', 'JACKSONVILLEST.', 'JAMES MADISON', 'KANSAS', 'KANSAS STATE', 'KENNESAW STATE', 'KENT STATE', 'KENTUCKY', 'LIU BROOKLYN', 'LSU', 'LA SALLE', 'LAFAYETTE', 'LAMAR', 'LEHIGH', 'LIBERTY', 'LIPSCOMB', 'LONG BEACH ST.', 'LONGWOOD', 'LOUISIANA TECH', 'LOUISVILLE',
           'LOYOLA (ILL.)', 'LOYOLA (MD.)', 'LOYOLA MARYMOUNT', 'MAINE', 'MANHATTAN', 'MARIST', 'MARQUETTE', 'MARSHALL', 'MARYLAND', 'MARYLAND-EASTERN SHORE', 'MCNEESE STATE', 'MEMPHIS', 'MERCER', 'MIAMI', 'MIAMI (OHIO)', 'MICHIGAN', 'MICHIGAN STATE', 'MID. TENN. STATE', 'MINNESOTA', 'MISS STATE', 'MISSISSIPPI VALLEY', 'MISSOURI', 'MONMOUTH', 'MONTANA', 'MONTANA STATE', 'MOREHEAD STATE', 'MORGAN STATE', "MOUNT ST. MARY'S", 'MURRAY STATE', 'N. CAROLINA A&T', 'N.C. CENTRAL', 'NAVY', 'NEBRASKA', 'NEW HAMPSHIRE', 'NEW JERSEY INSTITUTE', 'NEW MEXICO', 'NEW MEXICO ST.', 'NEW ORLEANS', 'NIAGARA', 'NICHOLLS STATE UNIVERSITY', 'NORFOLK STATE', 'NORTH ALABAMA', 'NORTH CAROLINA', 'NORTH CAROLINA ST.', 'NORTH DAKOTA', 'NORTH DAKOTA STATE', 'NORTH FLORIDA', 'NORTH TEXAS', 'NORTHEASTERN', 'NORTHERN ARIZONA', 'NORTHERN COLORADO', 'NORTHERN IOWA', 'NORTHERN KENTUCKY', 'NORTHWESTERN ST.', 'NOTRE DAME', 'OAKLAND', 'OHIO', 'OHIO STATE', 'OKLAHOMA', 'OKLAHOMA STATE', 'OLE MISS', 'ORAL ROBERTS', 'OREGON', 'OREGON STATE', 'PACIFIC', 'PENN', 'PENN STATE', 'PEPPERDINE', 'PITTSBURGH', 'PORTLAND', 'PORTLAND STATE', 'PRAIRIE VIEW', 'PRESBYTERIAN', 'PRINCETON', 'PROVIDENCE', 'PURDUE', 'PURDUE FORT WAYNE', 'QUINNIPIAC', 'RADFORD', 'RHODE ISLAND', 'RICE', 'RICHMOND', 'RIDER', 'ROBERT MORRIS', 'RUTGERS', 'SE LOUISIANA', 'SE MISSOURI', 'SIU EDWARDSVILLE', 'SMU', 'SACRAMENTO ST.', 'SACRED HEART', 'SAINT FRANCIS UNIVERSITY', 'SAINT LOUIS', 'SAM HOUSTON ST.', 'SAMFORD', 'SAN DIEGO', 'SAN DIEGO ST.', 'SAN FRANCISCO', 'SAN JOSE ST.', 'SANTACLARA', 'SAVANNAH STATE', 'SEATTLE U.', 'SETON HALL', 'SIENA', 'SOUTH ALABAMA', 'SOUTH CAROLINA', 'SOUTH CAROLINA ST.', 'SOUTH DAKOTA', 'SOUTH DAKOTA ST.', 'SOUTH FLORIDA', 'SOUTHERN', 'SOUTHERN ILLINOIS', 'SOUTHERN MISS.', 'SOUTHERN UTAH', 'ST. BONAVENTURE', 'ST. FRANCIS (N.Y.)', "ST. JOSEPH'S (PA.)", "ST. MARY'S (CAL.)", "ST. PETER'S", 'STANFORD', 'STEPHEN F. AUSTIN', 'STETSON', 'STONY BROOK', 'SYRACUSE', 'TCU', 'TEMPLE', 'TENNESSEE', 'TENNESSEE ST.', 'TENNESSEE TECH', 'TENNESSEE-MARTIN', 'TEXAS', 'TEXAS A&M', 'TEXAS A&M-CC', 'TCU', 'TEXAS SOUTHERN', 'TEXAS STATE', 'TEXAS TECH', 'TOLEDO', 'TOWSON', 'TROY', 'TULANE', 'TULSA', 'U. OF VICTORIA', 'UAB', 'UC DAVIS', 'UC IRVINE', 'UC RIVERSIDE', 'UC SANTA BARBARA', 'UCF', 'UCLA', 'UL-LAFAYETTE', 'UL-MONROE', 'UMBC', 'UMKC', 'UMASS AMHERST', 'UMASS LOWELL', 'UNC-ASHEVILLE', 'UNC-GREENSBORO', 'UNCW', 'UNLV', 'USC', 'USC UPSTATE', 'UT-ARLINGTON', 'CHATTANOOGA', 'UT-RIO GRANDE VALLEY', 'UTEP', 'UTSA', 'UTAH', 'UTAH STATE', 'UTAH VALLEY', 'VCU', 'VMI', 'VALPARAISO', 'VANDERBILT', 'VERMONT', 'VILLANOVA', 'VIRGINIA', 'VIRGINIA TECH', 'WAGNER', 'WAKE FOREST', 'WASHINGTON', 'WASHINGTON ST.', 'WEBER STATE', 'WEST VIRGINIA', 'WESTERN CAROLINA', 'WESTERN ILLINOIS', 'WESTERN KENTUCKY', 'WESTERN MICHIGAN', 'WICHITA STATE', 'WILLIAM AND MARY', 'WINTHROP', 'WIS.-GREEN BAY', 'WIS.-MILWAUKEE', 'WISCONSIN', 'WOFFORD', 'WRIGHT STATE', 'WYOMING', 'XAVIER (OHIO)', 'YALE', 'YOUNGSTOWN ST.']
university_list = {}
state_list = []
west_region = ['WA', 'OR', 'CA', 'ID', 'NV',
               'UT', 'AZ', 'MT', 'WY', 'CO', 'NM']
midwest_region = ['ND', 'SD', 'NE', 'KS', 'MN',
                  'IA', 'MO', 'WI', 'IL', 'IN', 'MI', 'OH']
south_region = ['TX', 'OK', 'AR', 'LA', 'KY', 'TN', 'MS',
                'AL', 'WV', 'MD', 'DE', 'DC', 'VA', 'NC', 'SC', 'GA', 'FL']
northeast_region = ['NY', 'PA', 'NJ', 'VT', 'NH', 'MA', 'CT', 'RI', 'ME']


def get_d1_links():  # Utilizes the track and field reporting website to obtain team links for all D1 teams
    page = requests.get("https://www.tfrrs.org/leagues/49.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    division_one_links_first = soup.find_all('td')
    for i in range(0, 695, 2):
        link1 = division_one_links_first[i].contents[1]
        exact_link = link1.attrs['href']
        division_one_links.append(
            'http://www.tfrrs.org/teams/xc/' + exact_link.split('/')[-1])


class University(object):  # Creates a class for all D1 schools with easily obtainable attributes
    def __init__(self, name, team_link):
        self.name = name
        self.team_link = team_link
        self.freshmen = get_freshmen(team_link)
        self.state = get_team_state(team_link)
        self.region = get_region(self)


# Obtains the region for a university, enabling users to pick a region they are most interested in
def get_region(University):
    if University.state in west_region:
        return 'WEST'
    elif University.state in midwest_region:
        return 'MIDWEST'
    elif University.state in south_region:
        return 'SOUTH'
    elif University.state in northeast_region:
        return 'NORTHEAST'


# Uses web scraping to obtain the links to all true freshmen for every university
def get_freshmen(team_link):
    page = requests.get(team_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    active_freshmen = []
    freshmen_links_first = soup.find_all('td')
    counter = 0
    for counter in range(0, len(freshmen_links_first), 2):
        link1 = freshmen_links_first[counter]
        if len(link1.contents) == 1:
            break
        link2 = link1.contents[1]
        exact_link = link2.attrs['href']
        if freshmen_links_first[counter+1].contents[0] == '\nFR-1\n':
            active_freshmen.append('http:' + exact_link)
    return active_freshmen


def get_team_name(team_link):
    page = requests.get(team_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    list1 = soup.find_all('h3')
    item = list1[0]
    team_name = item.contents[0]
    return team_name


def get_team_state(team_link):
    state_string = team_link.partition("teams/")[2]
    state_abbrev = state_string[0:2]
    if state_abbrev == 'xc':
        state_abbrev = state_string[3:5]
    return state_abbrev


def make_d1_list():
    i = 0
    while i < len(division_one_links):
        college_name = get_team_name(division_one_links[i])
        d1_list.append(college_name)
        i += 1
    return d1_list


def make_university_list():
    i = 0
    while i < len(division_one_links):
        university_list[d1_list[i]] = (
            University(d1_list[i], division_one_links[i]))
        i += 1


def make_state_list():
    i = 0
    while i < len(division_one_links):
        college_state = get_team_state(division_one_links[i])
        state_list.append(college_state)
        i += 1


def make_average(mile_mins, mile_secs, two_mins, two_secs, xc_mins=0, xc_secs=0):
    print((mile_mins + two_mins) * 60 + (mile_secs + two_secs))
    print((xc_mins * 60) + xc_secs)


def make_8k_secs(mins, secs):
    return (mins * 60) + secs


def linear_regression():
    x = [860, 914, 929, 884, 833, 861, 835,
         854, 823, 854, 822, 844, 854, 828, 835, 819, 864, 837, 862, 834, 881, 876, 868, 820, 842, 810]
    y = [1567, 1712, 1649, 1617, 1571, 1586, 1572,
         1561, 1597, 1605, 1550, 1579, 1523, 1577, 1509, 1531, 1746, 1619, 1555, 1555, 1617, 1664, 1657, 1534, 1660, 1550]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    m = len(x)
    numer = 0
    denom = 0
    for i in range(m):
        numer += (x[i] - mean_x) * (y[i] - mean_y)
        denom += (x[i] - mean_x) ** 2
    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)
    print(b1, b0)
    max_x = np.max(x) + 100
    min_x = np.min(x) - 100
    x = np.linspace(min_x, max_x, 1000)
    y = b0 + b1 * x
    plt.plot(x, y, color='#58b970', label='Regression Line')
    plt.scatter(x, y, c='#ef5423', label='Scatter Plot')
    plt.xlabel('High School Times')
    plt.ylabel('Projected 8k')
    plt.legend()
    plt.show()


def convert(hs_average):
    seconds = 519.9989341968696 + 1.2619350454266085*hs_average
    mins = seconds // 60
    real_secs = seconds - mins * 60
    print(str(int(mins)) + ":" + str(int(real_secs)))
