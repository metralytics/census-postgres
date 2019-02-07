# Census files overview and notes

The main products from the census that you'll want to work with are the decennial survey ("the US Census") and the
American Community Survey (the "ACS"). The ACS is a yearly published data set that updates, using extrapolated estimates,
data in the base decennial survey.

N.B., the U.S. Census is mandated by the U.S. Constitution in Article I, Section 2 with the intent that the People of the
United States should have the proper proportional representation in the House of Representatives and 
within the Electoral College.

## The Decennial Census

To be revisited at a later time.

## The American Community Survey

As an analyst, you are going to be most interest in the "Summary Files" which are summarizations of the individual responses. Summary files are further anonymized by rolling them into 5-year moving averages for geographic areas when there's a need to further obscure the population. Frankly, just ignore the American Fact Finder for now but we'll use it later to perform some error checking on our results.

[Link](https://www.census.gov/programs-surveys/acs/data/summary-file.html)


### Some ACS Terminology

#### Top points to know
* There are several geographic hierchies available and that overlap
* Data can be released in 1-year and 5-year summary frequencies
* 1-year data is only guaranteed available at at state leve, but some counties have 1-year data
* 5-year data is available down to the level of a "block group" which in size sits between a "block" and a "census tract" or "block numbering area"
* [Topic areas](https://www.census.gov/programs-surveys/acs/guidance/subjects.html) comprise
    * **Social:** Ancestry, Citizen Voting-Age Population, Citizenship Status, Disability Status, Educational Attainment, Fertility, Grandparents as caregivers, Language spoken at home, Marital history, Marital Status, Migration (residence 1-year ago), Place of birth, School enrollment, Undergraduate field of degree, Veteran status (and period of military service), Year of entry
    * **Housing:** Bedrooms, computer and internet use, House Heating Fuel, Kitchen facilities, Occupancy/Vacancy status, Occupants per room,
    Plubming facilities, Rent, Rooms, Selected monthly owner costs, Telephone service available, Units in structure, Value of home, Vehicles available,
    Year householder moved into unit, year structure built
    * **Economic:** Class of worker, Commuting and place of work, Employment status, Food stamps (SNAP), Health insurance coverage, Income and earnings, Industry and occupation, Poverty status, Work status last year
    * **Demographic:** Age, Sex, Group Quarters Population, Hispanic or Latino origin, Race, Relationship to householder, Total population

#### Deeper dive

* What is a block group? [According to Wikipedia](https://en.wikipedia.org/wiki/Census_block_group) "A Census Block Group is a geographical unit used by the United States Census Bureau which is between the Census Tract and the Census Block. It is the smallest geographical unit for which the bureau publishes sample data." See also [the glossary page](https://www.census.gov/geo/reference/gtc/gtc_bg.html?cssp=SERP). Block groups contain between 600 and 3,000 people. A census tract itself has between 2,00 and 8,000 residents and by definition, the tract boundaries ["follow visible features"](https://www2.census.gov/geo/pdfs/reference/GARM/Ch10GARM.pdf) so they can be identified easily from the ground by workers in the field.

Too, the boundaries will always follow at least state and county boundaries, with cities boundaries being sometimes followed. But for privacy reasons, not all data is published at all geographic levels at a yearly granularity. In fact, yearly estimates are only 100% published at the level of state or "higher."

So, the classical geographic [hierarchy looks like this](https://www.census.gov/programs-surveys/acs/geography-acs/concepts-definitions.html):
- Individual (technically, available in PUMS, but immediate rolls up into a state)
- Block
- Block group (smallest size reported in summary files, 5-year estimates only)
- Tract /or/ block numbering area (5-year estimates only, 100% coverage)
- County (low coverage in 1-year estimates, moderate coverage in 1-year supplemental, 100% coverage in 5-year survey)
- States 
- Divisions
- Regions
- National

There are some alternative hierarchies available as well such as:
- ZIP Code Tabulation Area (5 year estimates only starting with the 2012 release)
- National

Or a legislatively driven hierarchy:
- Congressional districts
- State
- Division
- Region
- Nation

Finally, an example of a statistically-driven hierarchy:
- Metropolitan and micropolitan areas
- National

For publishing coverage, there is a [handy table](https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html) that shows the number 
of geographic regions and publishing availability of 1, 1-year supplment, and 5-year data.

* What is a sequence? 

