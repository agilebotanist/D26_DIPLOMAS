Scraping: https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand
  Consent dismissed via: text-match:accept
  Settled (dom-quiet, 2525ms)
  Extracting content...
  Extracted 14733 characters

--- Content ---

## Introduction

The United States is in the middle of an unprecedented build-out of AI infrastructure. No project illustrates the scale of that effort more than Stargate, a $500 billion endeavor involving AI developer OpenAI, cloud provider Oracle, and investment company SoftBank.

Stargate has seven locations across the US, all of which are now showing active development. The most advanced—in Abilene, Texas—is already operating at an estimated capacity of 0.3 gigawatts (GW). The six other sites include two more in Texas, as well as facilities in New Mexico, Wisconsin, Michigan, and Ohio. Together, the seven sites add up to over 9 GW of planned capacity, which is comparable to the peak power demand of New York City.[^1] This will be enough to power the equivalent of 20 million Nvidia H100 GPUs, which was the *total* amount of AI compute in the world by the end of 2025.[^2]

| Site | Current   capacity (GW) | Projected   capacity (GW)[^3] | Construction   began | Projected   completion | Power   sources |
| --- | --- | --- | --- | --- | --- |
| [Abilene, Texas](/data/data-centers/satellite-explorer/OpenAIStargateAbilene) | 0.3 | 1.2 | Q2 2024 | Q4 2026 | On-site gas, Grid |
| [Shackelford County, Texas](/data/data-centers/satellite-explorer/OpenAIStargateShackelford) | 0 | 2.0 | Q3 2025 | Q4 2028 | On-site gas |
| [Doña Ana County, New Mexico](/data/data-centers/satellite-explorer/OpenAIStargateNewMexico) | 0 | 2.2 | Q4 2025 | Q4 2028 | On-site gas |
| [Milam County, Texas](/data/data-centers/satellite-explorer/OpenAIStargateMilam) | 0 | 1.2 | Q3 2025 | Q4 2028 | On-site (unknown type) |
| [Port Washington, Wisconsin](/data/data-centers/satellite-explorer/OpenAIStargateWisconsin) | 0 | 1.3 | Q1 2026 | Q4 2028 | Grid |
| [Saline Township, Michigan](/data/data-centers/satellite-explorer/OpenAIStargateMichigan) | 0 | 1.4 | Q4 2025 | Q4 2028 | Grid |
| [Lordstown, Ohio](/data/data-centers/satellite-explorer/OpenAIStargateLordstown) | 0 | <0.3 | Q4 2025 | Unknown | Grid |

Stargate’s design choices reveal how builders are navigating the key challenges of gigawatt-scale AI data centers in the US. To sidestep lengthy queues for connecting to energy grids, at least three of the seven sites will make use of on-site natural gas plants. To address public concerns about water usage, at least six sites will use closed-loop liquid cooling systems, which do not evaporate water.[^4] These decisions will likely save the project time but raise the cost of the facilities.

Based on [announcements](https://openai.com/index/five-new-stargate-sites/) [from](https://openai.com/index/expanding-stargate-to-michigan/) 2025, SoftBank will own the hardware at the Milam County and Ohio sites, while Oracle will own the hardware at the remaining sites. All sites will serve OpenAI’s workloads.

## The sites

### Abilene, Texas

![](/assets/images/posts/2026/openai-stargate-where-the-us-sites-stand/abilene.png)

Satellite image of the Abilene, Texas Stargate site. Image © Airbus DS 2026, captured 2026-03-24.

**Current capacity:** 0.3 GW | 250,000 H100-equivalents[^5]

**Projected capacity:** 1.2 GW | 1.0 million H100-equivalents

**Projected completion:** Q4 2026

The Stargate project’s flagship location is in Abilene, Texas. Built by AI infrastructure company Crusoe, Abilene is the most complete Stargate site to date, with an estimated four of the eight buildings already operational. These buildings house state-of-the-art Nvidia Blackwell chips.

Power is currently supplied by a mix of on-site natural gas and [grid power](https://lancium.com/locations/), which includes local wind power.

OpenAI had planned to expand this site to 2.1 GW, but [recently reversed course](https://www.bloomberg.com/news/articles/2026-03-06/oracle-and-openai-end-plans-to-expand-flagship-data-center), deciding to direct that capacity to other locations. Microsoft has since [partnered](https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure) with Crusoe for the adjacent 900 MW site.

[View with satellite explorer](/data/data-centers/satellite-explorer/OpenAIStargateAbilene)

### Shackelford County, Texas

![](/assets/images/posts/2026/openai-stargate-where-the-us-sites-stand/shackelford.png)

Satellite image of the Shackelford County, Texas Stargate site. Image © 2026 Vantor, captured 2026-04-14.

**Current capacity:** 0 GW

**Projected capacity:** 2 GW | 4.2 million H100-equivalents

**Projected completion:** Q4 2028

Just across the county line from the Abilene site, data center developer Vantage is constructing a massive 1,200-acre (4.9-square-kilometer) [campus](https://vantage-dc.com/data-center-locations/north-america/shackelford-county-tx) with 10 buildings.

The campus will be [powered](https://arrington.house.gov/uploadedfiles/final_oracle_oai_data_center_fact_sheet_092225b.pdf) by an onsite natural gas microgrid.

Vantage has given a delivery date for the site’s first building of late 2026.[^6] Satellite imagery shows that roofing is underway for this building (visible in bright white).

[View with satellite explorer](/data/data-centers/satellite-explorer/OpenAIStargateShackelford)

### Doña Ana County, New Mexico

![](/assets/images/posts/2026/openai-stargate-where-the-us-sites-stand/new-mexico.png)

Satellite image of the Doña Ana County, New Mexico Stargate site. Image © Airbus DS 2026, captured 2026-02-06.

**Current capacity:** 0 GW

**Projected capacity:** 2.2 GW | 4.6 million H100-equivalents

**Projected completion:** Q4 2028

In New Mexico, STACK Infrastructure is developing Project Jupiter, which consists of four large buildings. Satellite imagery shows that foundation work is underway.

This site will be [powered](https://projectjupitertogether.com/) by two natural gas microgrids designed to limit impact on the local grid.

[View with satellite explorer](/data/data-centers/satellite-explorer/OpenAIStargateNewMexico)

### Milam County, Texas

![](/assets/images/posts/2026/openai-stargate-where-the-us-sites-stand/milam.png)

Satellite image of the Milam County, Texas Stargate site. Image © Airbus DS 2026, captured 2026-03-23.

**Current capacity:** 0 GW

**Projected capacity:** 1.2 GW | 2.5 million H100-equivalents

**Projected completion:** Q4 2028

SoftBank subsidiary SB Energy is [building and operating](https://sbenergy.com/openai-and-softbank-group-partner-with-sb-energy/) what is [described](https://www.constructiondive.com/news/stargate-5-new-data-center-sites/761424/) as a “fast-build” site in Milam County, Texas, around 70 miles (110 kilometers) northeast of Austin. A satellite image from March shows steel framing and roofing for the first building (visible as a blue rectangle). Regulatory filings indicate this building will be [delivered](https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026017746) by October.

SB [plans](https://openai.com/index/stargate-community/) to fund and build new energy generation and storage to supply the majority of the campus’s power.

[View with satellite explorer](/data/data-centers/satellite-explorer/OpenAIStargateMilam)

### Port Washington, Wisconsin

![](/assets/images/posts/2026/openai-stargate-where-the-us-sites-stand/wisconsin.png)

Satellite image of the Port Washington, Wisconsin Stargate site. Image © Airbus DS 2026, captured 2026-02-14.

**Current capacity:** 0 GW

**Projected capacity:** 1.3 GW | 2.6 million H100-equivalents

**Projected completion:** Q4 2028

Vantage, which is also the developer behind the Shackelford County site, has broken ground on a campus named “Lighthouse” in Port Washington, just north of Milwaukee. Foundation work can be seen in satellite imagery.

The site is [described](https://vantage-dc.com/data-center-locations/north-america/port-washington-wisconsin) as “sustainable-by-design,” with 70% of power drawn from solar, wind, and battery storage.

[View with satellite explorer](/data/data-centers/satellite-explorer/OpenAIStargateWisconsin)

### Saline Township, Michigan

![](/assets/images/posts/2026/openai-stargate-where-the-us-sites-stand/michigan.png)

Satellite image of the Saline Township, Michigan Stargate site. Image © 2026 Vantor, captured 2026-03-12.

**Current capacity:** 0 GW

**Projected capacity:** 1.4 GW | 2.9 million H100-equivalents

**Projected completion:** Q4 2028

Related Digital is [developing](https://www.related.com/press-releases/2025-10-30/openai-oracle-and-related-digital-announce-stargate-data-center-site) a campus dubbed “The Barn” in Saline Township, southwest of Detroit. Satellite imagery shows foundation work underway for the first building.

DTE Energy will provide 100% of the power, augmented by a battery storage system financed by the project.

[View with satellite explorer](/data/data-centers/satellite-explorer/OpenAIStargateMichigan)

### Lordstown, Ohio

![](/assets/images/posts/2026/openai-stargate-where-the-us-sites-stand/ohio.png)

Satellite image of the Lordstown, Ohio Stargate site. Image © Airbus DS 2026, captured 2026-02-27.

**Current capacity:** 0 GW

**Projected capacity:** <0.3 GW | <0.3 million H100-equivalents

**Projected completion:** Unknown

The seventh site is in Ohio, where some land has been cleared, but no large-scale data center construction is visible. The site is [primarily](https://www.wfmj.com/archives/data-center-to-occupy-small-part-of-lordstown-ai-hub-feature-advanced-design/article_533f268a-ec1d-5378-9ccb-ceec7d6d343e.html) a manufacturing facility for AI servers and data center equipment, operated as a [joint venture](https://www.manufacturingdive.com/news/foxconn-softbank-joint-data-center-equipment-factory-apple-ai-lordstown-ohio/757995/) between SoftBank and Foxconn. The capacity of the data center will likely be no more than 0.3 GW, with OpenAI [announcing](https://openai.com/index/five-new-stargate-sites/) that the Milam County and Lordstown sites could scale to a combined 1.5 GW by 2027.

The Lordstown data center will likely draw power from the grid, as the Foxconn plant already has a [substation connected](https://openinframap.org/#14.86/41.15027/-80.87213).

[View with satellite explorer](/data/data-centers/satellite-explorer/OpenAIStargateLordstown)

## The road ahead

At this point, the full $500 billion Stargate project is more than pure ambition. The build-out has started all over the US, leaving enough time to finish by 2029. However, there is a long road ahead for all seven sites. Plans can change even after construction begins, as shown by OpenAI pulling out of the Abilene expansion. Financing and procuring equipment will also be challenging at this unprecedented scale. Finally, political opposition is a real factor, as evidenced by a [ban](https://www.datacenterdynamics.com/en/news/data-centers-now-banned-in-lordstown-ohio/) on future data centers in Lordstown and [local opposition](https://www.datacenterdynamics.com/en/news/planned-stargate-data-center-encounters-opposition-in-saline-township-michigan/) to the Michigan site. Epoch AI will be following the Stargate project and the broader data center build-out closely to see how this all pans out.

## Updates

## About the authors[Elliot Stewart](/about/team/elliot-stewart)

[

Elliot Stewart is Head of Communications at Epoch AI. He has a background in AI governance, national security, and international policy.

](/about/team/elliot-stewart)[

Ben Cottier

Ben Cottier is a senior researcher at Epoch AI. He leads the AI data centers project. Besides data centers, Ben is interested in AI cost trends and the diffusion of AI capabilities. He previously worked as a software engineer, and has a masters degree in AI from the University of Edinburgh.

](/about/team/ben-cottier)

[^1]: The NYISO 2025 [Gold Book](https://www.nyiso.com/documents/20142/2226333/2025-Gold-Book-Public.pdf) (p.30) forecasts about 11 GW of peak summer demand for New York City (Zone J) from 2026 through 2030. This represents the single highest hour of demand annually.

[^2]: The H100 is just an example: the actual chips in these data centers will probably be Nvidia Blackwell, and later Nvidia Rubin. The total amount of compute in the world is based on the [AI Chip Sales](/data/ai-chip-sales?view=graph&tab=h100_equivalents) database, which estimates about 20 million H100-equivalents worth of AI chips sold by Q4 2025. The projected compute for the Stargate sites is estimated from the power capacities and the trend in energy efficiency for leading [machine learning hardware](/data/machine-learning-hardware) —except for Abilene, which was [disclosed](https://cdn.prod.website-files.com/6855c1aa175582ee23e0aa19/68710273a71bb7c11049ba28_Crusoe_Impact_Report_2024.pdf#page=19) by Crusoe to have 50,000 Blackwell GPUs per building.

[^3]: All stated power capacities refer to total facility power, including power for GPUs, cooling, lighting, etc. Power capacities for the Stargate sites have not been reported consistently as total facility power or IT power. For some sites, we estimated the total facility power based on the reported IT power. For example, Vantage [reports](https://vantage-dc.com/data-center-locations/north-america/port-washington-wisconsin) Shackelford County as 1.4 GW of IT power. Given the hot summer climate of Texas and closed-loop cooling (which is less energy-efficient than evaporative cooling), we estimated the total facility power to be about 2 GW.

[^4]: Sources: [Abilene](https://www.texasmonthly.com/news-politics/abilene-stargate-artificial-intelligence/), [Shackelford County](https://arrington.house.gov/uploadedfiles/final_oracle_oai_data_center_fact_sheet_092225b.pdf), [Doña Ana County](https://www.datacenterdynamics.com/en/news/oracle-revealed-as-tenant-of-project-jupiter-data-center-campus-in-new-mexico/), [Port Washington](https://vantage-dc.com/news/openai-oracle-and-vantage-data-centers-announce-stargate-data-center-site-in-wisconsin/), [Saline Township](https://openai.com/index/expanding-stargate-to-michigan/), and [Lordstown](https://www.wfmj.com/archives/data-center-to-occupy-small-part-of-lordstown-ai-hub-feature-advanced-design/article_533f268a-ec1d-5378-9ccb-ceec7d6d343e.html). We did not find direct confirmation of a closed-loop system for Milam County, but it is [designed](https://openai.com/index/stargate-sb-energy-partnership/) to minimize water usage.

[^5]: One H100-equivalent is the computing power equivalent to one Nvidia H100 GPU, measured in operations/second. The H100-equivalent unit uses a chip’s highest 8-bit operations/second specification to convert between chips.

[^6]: This is when the completed building is handed over to the tenant, not when the data center is fully operational.
